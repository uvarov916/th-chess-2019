import numpy as np
import cv2

def IsRed(*args):
    b, g, r = args[0]
    if (b <= r/1.5 and g <= r/1.5 and r>100):
        return True
    else:
        return False

def GetCenter(dots):
    summx = 0
    summy = 0
    lenght = len(dots)
    for temp in dots:
        summx = summx + temp[0]
        summy = summy + temp[1]      
    return[int(summx/lenght), int(summy/lenght)] 

def CoordRedDots(image):
    imageWidth = image.shape[1]
    imageHeight = image.shape[0]

    xPos, yPos = 0, 0

    redDots = []

    halfx = int(imageWidth/2)
    halfy = int(imageHeight/2)

    while xPos < imageWidth:
        while yPos < imageHeight:
            if IsRed(image[yPos, xPos]):
                redDots.append([xPos,yPos])
               # image[xPos,yPos] = [0,0,255]
            yPos = yPos + 1
        yPos = 0
        xPos = xPos + 1

    top_left = []
    top_right = []
    bottom_left = []
    bottom_right = []

    for temp in redDots:
        if temp[0] < halfx and temp[1] < halfy:
            top_left.append(temp)
        if temp[0] > halfx and temp[1] < halfy:
            top_right.append(temp)
        if temp[0] < halfx and temp[1] > halfy:
            bottom_left.append(temp)
        if temp[0] > halfx and temp[1] > halfy:
            bottom_right.append(temp)
    result = []
    result.append(GetCenter(top_left))
    result.append(GetCenter(top_right))
    result.append(GetCenter(bottom_left))
    result.append(GetCenter(bottom_right))
    return result

# field_edges = CoordRedDots(cv2.imread("img1.png"))
# print(field_edges)
