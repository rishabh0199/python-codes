import cv2

webcam = cv2.VideoCapture(0)

while True:
    state, img = webcam.read()
    if state:
        print(state)
        print(img)
        cv2.imshow("mycam",img)
        if cv2.waitKey(1) == ord('r'):
            break
webcam.release()
cv2.destroyAllWindows()