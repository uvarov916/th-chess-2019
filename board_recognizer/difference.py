import numpy as np
import cv2
import msvcrt as m
import reddots

def get_difference(frame1, frame2, reddots) :
    res = cv2.absdiff(frame1, frame2)
    res = cv2.blur(res, (15, 10))
    res = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
    res = cv2.threshold(res, 10,255,cv2.THRESH_BINARY)[1]
    maxx = reddots[1][0]
    maxy = reddots[2][1]
    lengthx = reddots[1][0] - reddots[0][0]
    lengthy = reddots[2][1] - reddots[1][1]

    startx = reddots[0][0]
    starty = reddots[1][1]
    stepx = int(lengthx/8)
    stepy = int(lengthy/8)
    #print(len(res), len(res[1]))
    #print(maxw, maxh)
    array = []
    for i in range (8) :
        tempArr = []
        for j in range(8) :
            cnt = 0
            for z in range(i * stepx + startx, (i + 1) * stepx + startx) :
                for z2 in range(j * stepy + starty, (j + 1) * stepy + starty) :
                    if z < maxx and z2 < maxy : 
                        if res[z][z2] > 0:
                            cnt += 1
            tempArr.append(cnt)
        array.append(tempArr)
    return array

frame1 = cv2.imread("image1.jpg")
frame2 = cv2.imread("image2.jpg")

print(get_difference(frame1,frame2,reddots.CoordRedDots(frame1)))