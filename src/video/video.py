from threading import Thread
import cv2


class WebcamVideoStream:
	"""Threaded webcam video stream"""
	def __init__(self, src=0, win_w=400, win_h=300):
		self.stream = cv2.VideoCapture(src)
		self.stream.set(3,win_w)
		self.stream.set(4,win_h)
		(self.grabbed, self.frame) = self.stream.read()
		self.stopped = False

	def start(self):
		Thread(target=self.update, args=()).start()
		return self

	def update(self):
		while True:
			if self.stopped:
				return
			(self.grabbed, self.frame) = self.stream.read()

	def read(self):
		return self.frame

	def stop(self):
		self.stopped = True
