import cv2 as cv 

cap = cv.VideoCapture("C:\Users\felipe\Videos\felipe.mp4")
rodando = True

ret, frame = cap.read()
cap.release()

cv.imshow('frame', frame)
cv.waitKey(1)
