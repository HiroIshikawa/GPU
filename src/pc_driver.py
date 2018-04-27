from recognizer.detect import *
from recognizer.measure import *
from recognizer.preprocess import *
from interface.interface import *

from sys import argv
import sys
import cv2
import numpy as np
import time
import threading

from video.video import WebcamVideoStream

def command(avg_pos):
    if (avg_pos > 10):
        print("Turn Right: Rotate "+str(avg_pos)+" units")
    elif (avg_pos < -10):
        print("Turn Left: Rorate "+str(avg_pos)+" units")
    else:
        print("Go Straight")

def mean(l):
    if len(l) == 0:
        return 0.0
    return sum(l)/len(l)

def navigate(candidates):
    threading.Timer(0.5, navigate, args=[candidates]).start()
    global track_flag
    global avg_pos
    if candidates:
        avg_pos = mean(candidates)
        track_flag = True
        candidates[:] = []
    else:
        pass

# Inputs from command line
obj_w = int(argv[1])
obj_h = int(argv[2])
scale_factor = float(argv[3])
min_neighs = int(argv[4])
win_w = int(argv[5])
win_h = int(argv[6])

# Variable initiations for threading
track_flag = False
monitor_flag = False
avg_pos = 0.
candidates = []

# Initiate video stream thread
vs = WebcamVideoStream(0,win_w,win_h).start()
time.sleep(.1)

start_time = time.time()
monitor_start_time = 0.

# Main control logic
try:
    while(True):
        # Read img streams, apply obj detection, measure detected objs positions
        img = vs.read()
        imshape = img.shape
        rects, img = detect(img, scale_factor, min_neighs, obj_w, obj_h)
        img = box(rects, img)
        cv2.imshow("Cascaded", img)
        measure(img, rects, candidates)

        # Check detected candidates for every x. sec
        if (time.time() - start_time > .5):
            if candidates:
                avg_pos = mean(candidates)
                track_flag = True
                candidates[:] = []
                start_time = time.time()

        # If any candidate detected, activate tracking sequence
        if track_flag:
            print("Tracking activated")
            track(avg_pos)
            monitor_start_time = time.time()
            track_flag = False

        # Every time object detected, there's 5 secs window to keep runnning monitor()
        if time.time() - monitor_start_time < 5.:
            monitor(avg_pos)

        # Stop sequence from CLI input
        if cv2.waitKey(10) == 27:
            print("Stopping..")
            vs.stop()
            cv2.destroyAllWindows()
            break

except KeyboardInterrupt:
    vs.stop()
    cv2.destroyAllWindows()
