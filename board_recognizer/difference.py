import numpy as np
import cv2
import msvcrt as m

def get_difference(name_of_img1 = 'img1.png', name_of_img2 = 'img2.png', red_xy = [[54,7], [270, 10], [270, 230], [47, 228]]) :
    red = red_xy
    cap = cv2.VideoCapture(0)

    grayA = cv2.imread('img1.png', 0)
    grayB = cv2.imread('img2.png', 0)

    res = cv2.absdiff(grayA, grayB)
    res = cv2.blur(res, (15, 10))
    val, res = cv2.threshold(res, 10,255,cv2.THRESH_BINARY)
    res = cv2.resize(res, None, fx = 0.5, fy = 0.5, interpolation = cv2.INTER_CUBIC)
    maxh = red[1][0]
    maxw = red[2][1]
    h = red[1][0] - red[0][0]
    w = red[2][1] - red[1][1]

    sth = red[0][0]
    stw = red[1][1]
    stepw = int(w/8)
    steph = int(h/8)
    #print(len(res), len(res[1]))
    #print(maxw, maxh)
    array = []
    for i in range (8) :
        for j in range(8) :
            cnt = 0
            for z in range(i * stepw + stw, (i + 1) * stepw + stw) :
                for z2 in range(j * steph + sth, (j + 1) * steph + sth) :
                    if z < maxw and z2 < maxh : 
                        if res[z][z2] > 0:
                            cnt += 1
            array.append(cnt)
    return array

array = get_difference()
print(array)