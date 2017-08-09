# GPU (Garbage Processing Unit)
## Eco-friendly Compact Autonomous Cleaning Robot

GPU is an environmentally friendly compact autonomous cleaning robot.
This repo includes the main control program and object detection/measurement/tracking implementation.
For a need of immediate testing on Mac, it provides PC driver to demostrate object recognition on builtin webcam.

The object recognition model was built by the cascade classifier trainer of OpenCV.
The wrapper scripts to conduct training is also provided in another repo.
Please visit: https://github.com/HiroIshikawa/object-recognizer 

## Getting Started

### Installing

These were tested under
Python 3.5.3
OpenCV 3.1.0

### Recognition Module Test on Mac

Clone the repo
```
git clone https://github.com/HiroIshikawa/GPU
cd GPU
```

Then run the PC driver
```
python pc_driver.py 20 40 1.1 7 400 300
```
Each argument of calling script corresponds to:

- Arg 1: object width (i.e. 20)
- Arg 2: object height (i.e. 40)
- Arg 3: scale factor (i.e. 1.1)
- Arg 4: # of neighbors (i.e. 7)
- Arg 5: window width (i.e. 400)
- Arg 6: window height (i.e. 300)

At this point, your laptop camera activated and ready to detect a can (or any object that has similar shape).
Try find any object whose shape is similar to a can and capture in your recording.
If successfully captured, the object would be surrounded by a green regtangle.
Measurement of the position within the window would also be displayed on your terminal. 
Please watch the demo clips to feel how the demo should look like below.

## Demo

Demo 1 - Object Recognition (Youtube Video):

[![Alt text](https://img.youtube.com/vi/mdjVOoMc52M/0.jpg)](https://www.youtube.com/watch?v=mdjVOoMc52M)


Demo 2 - Autonomous Navigation (Youtube Video):

[![Alt text](https://img.youtube.com/vi/We3pcBQlCMg/0.jpg)](https://www.youtube.com/watch?v=We3pcBQlCMg)