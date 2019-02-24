#### Video processing by OpenCV:
---
##### This project will capture any moving object by the webcam and draw a rectangle aorund it. 
- how it works?

First it takes a photos of the background where there is no moving object. Then a photo with the moving object. then it converts the photo with the moving object into grayscale. After that, we define threshold for density of pixels and the pixels with less than a specific amout of density will be just ignored. This way, we will have the contour of the moving object found. Finally, We define if any areas that computer found as moving objects, was smaller than a specific size in pixels, ignore them.

Most of these codes happen inside the while loop in project 7 code called video-detection.py

##### Code steps:

we copy the code from project 7. We need to save the first frame somewhere. Outside the while loop, we define first_frame = None. 

__None variable:__: a datatype in Python that can be defined and left empty for later, without having Python return an error saying veriable undefined.

We defined a variable called gray and in the while loop we say, if the first frame was None, or empty, save the gray photo of the first frame. otherwise continue back to the loop.
 
 __Continue in While loop:__  It means the Python will get back to the beginning of the loop as soon as it sees continue command. We add continue to the code so that it gets back to the while loop again.
 
 We also need to apply GaussianBlur() function to gray. It makes the image smoother.
 
 now we will have to compare the two frames and return the difference. It is done by absdiff() function.
 
 
 
 
