import cv2
import numpy as np
from cv2 import VideoWriter,VideoWriter_fourcc
import datetime
width = 800
height = 600
FPS = 24
seconds = 10

def showTime(frame):
    now = str(datetime.datetime.now())
    font = cv2.FONT_HERSHEY_COMPLEX
    new_frame = cv2.putText(frame, now, (10, 20), font, 0.5, (255, 255, 255), 2)
    return new_frame

def showInfo(frame):
    font = cv2.FONT_HERSHEY_COMPLEX
    name = 'Cai Xiangyu'
    id = '22021003'
    new_frame = cv2.putText(frame,name,(270,300),font,1,(0,0,0),2)
    new_frame = cv2.putText(new_frame,id,(270,400),font,1,(0,0,0),2)
    return new_frame

def drawTri(img):
    pts = np.array([[365,337],[330,399],[394,399]])
    cv2.polylines(img, [pts], True, (0, 0, 0), 5)
    return img

def drawRec(img):
    pts = np.array([[330,399],[394,399],[394,510],[330,510]])
    cv2.polylines(img, [pts], True, (0, 0, 0), 5)
    return img

def drawLine(img,pt1,pt2):
    cv2.line(img,pt1,pt2,(0,0,0),5)
    return img

def display(img,last,seconds):
    for _ in range(seconds):
        frame = img
        frame = showTime(frame)
        video.write(frame)
        cv2.imshow('1',frame)
        if cv2.waitKey(last) & 0xff == 32:
            cv2.waitKey(0)



def drawBeginning():
    img = cv2.imread('./resource/zju.jpg')
    title = "Shooting Star"
    for i in range(FPS*3):
        img = img*0.9
        frame = showTime(img)
        frame = showInfo(frame)
        font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
        frame = cv2.putText(frame, title, (200,100), font, 2, (205, 197, 0), 2)
        video.write(frame)
        cv2.imshow('1', frame)
        if cv2.waitKey(24) & 0xff == 32:
            cv2.waitKey(0)

def drawPainting():
    img = np.zeros((600,800,3),dtype=np.uint8)
    img[:] = 255
    img = drawTri(img)
    display(img,1000,1)
    img = drawRec(img)
    display(img,1000,1)
    img = drawLine(img,(330,515),(300,565))
    display(img,1000,1)
    img = drawLine(img,(362,515),(362,565))
    display(img,1000,1)
    img = drawLine(img, (392, 515), (422, 565))
    display(img, 1000, 1)


    for _ in range(seconds):
        frame = img
        frame = showTime(frame)
        video.write(frame)
        cv2.imshow('1',frame)
        if cv2.waitKey(1000) & 0xff == 32:
            cv2.waitKey(0)


if __name__ == "__main__":
    fourcc = VideoWriter_fourcc(*'MP42')
    video = VideoWriter('./resource/noise.avi', fourcc, float(FPS), (width, height))
    drawBeginning()
    drawPainting()
    video.release()

