import cv2
#grayscaled:
img = cv2.imread("galaxy.jpg",0)
print(type(img))  # it is a numpy array
print(img)  # retuens the array of pixels with their density
print(img.shape)  # pritns the shape of the array
print(img.ndim)   # pritns the dimanesion of the array, which is 2 in this exmaple

#colored
img2 = cv2.imread("galaxy.jpg",1)

#resizing to fix size:
#resized_image = cv2.resize(img,(500,1000))
#resizing the image to half
resized_image2 = cv2.resize(img,(int(img.shape[1]/2), int(img.shape[0]/2)))
#show image and close it
cv2.imshow("Galaxy", resized_image2)
#save the resized image
cv2.imwrite("galaxy_resized2.jpg", resized_image2)
cv2.waitKey(0)
cv2.destroyAllWindows()
