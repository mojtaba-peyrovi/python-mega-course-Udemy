import cv2
import time
video = cv2.VideoCapture(0)
a = 0
while True:
    a += 1
    check, frame = video.read()
    print(check)
    print(frame)


    #time.sleep(3)

    cv2.imshow("Capture", frame)
    key = cv2.waitKey(1)

    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
print(a)
