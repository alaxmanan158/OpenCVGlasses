import cv2
import cvzone
import keyboard
# import os
# from PIL import Image, ImageChops
cap = cv2.VideoCapture(0)
cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
num=1
# def trim(im):
#     bg = Image.new(im.mode, im.size, im.getpixel((0, 0)))
#     diff = ImageChops.difference(im, bg)
#     diff = ImageChops.add(diff, diff, 2.0, -100)
#     bbox = diff.getbbox()
#     if bbox:
#         return im.crop(bbox)
while True:
    k = cv2.waitKey(10)
    if k == ord('s'):
        num+=1
    if(num<=7):
            overlay = cv2.imread('Glasses/glasses{}.png'.format(num), cv2.IMREAD_UNCHANGED)
            #overlay = trim(overlay)


    _, frame = cap.read()
    gray_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = cascade.detectMultiScale(gray_scale)
    for (x, y, w, h) in faces:
        #cv2.rectangle(frame,(x, y), (x+w, y+h), (0, 255, 0), 2)
        overlay_resize = cv2.resize(overlay,(int(w * 0.9), int(h * 0.45)))
        frame = cvzone.overlayPNG(frame, overlay_resize, [x, y + 105])
    cv2.imshow('SnapLens', frame)
    if cv2.waitKey(10) == ord('q') or num>7:
        break
  
cap.release()
cv2.destroyAllWindows()
