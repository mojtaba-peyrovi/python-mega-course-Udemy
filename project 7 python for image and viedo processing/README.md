### Image and Video processing with OpenCV:
---

- openCV standsfor: Opensource Computer Vision

For installing it we just use pip:
```
pip install opencv-python
```

and the library name to import is called "cv2" (import cv2)

imread() method form cv2 opens the image, the second parameter is the color. we can pass 1 if we want color, 0 if we want grayscale, and -1 if we want color with alpha.

__IMPORTANT:__ This imread can give me the array of pixels density, etc. which are the stuff I was looking for, to do my deep learning analysis onn photos for my fashion project. Also when we change it to 1 to get the colored image, with the same command,we will get all pixel info of RGB values.

- in the first script called script-1.py we opened a photo, resized, and saved the re-sized version in the same folder.

__Hearcascade files:__ These are some xml files that include information about color, proportionality, and all aspects of a human, so that openCV uses them to recognize a human's photo. 
[here](https://github.com/opencv/opencv/tree/master/data/haarcascades) is a link to all heart_cascade files by openCV.

In order to use it we made a file called face_detector.py. 
In this file we import one of my photos and turned it to a gray-scaled photo because it is easier, faster, and more accurate for python to detect it.

When we print the rectangle with print(faces) it shows [106,  74, 188, 188] that means a rectangle tha starts from the top left corner, from [106,74] and makes a rectangle with the width of 188 and height of 188.

__Video Capturing:__ When we want to use cv2 for video capturing, first we need to make an object called cv2.VideoCapture(). Inside the bracket, we can pass a video from hard-drive like this:
```
video = cv2.VideoCapture("movie.mp4")
```

if we are going to use external video, for example webcam, we use 0 or 1 or 2 depending on how many cameras we have.

__Difference Between map() and flatmap() functions:

there is a one-to-one relationship between input and output of map() for example with map function we can make everything uppercase. Whereas in flatmap() the number of output can be different from the input, for example a text string can be split into words, so the output wouldn't be equal to the input.

