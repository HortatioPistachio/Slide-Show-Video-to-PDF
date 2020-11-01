import cv2
import numpy
import math


def getNextFrame(vid, res):
    framesLeft = True
    for i in range(res):
        ret = vid.grab()
        if ret == False:
            framesLeft = False
            break

    ret, frame = vid.read()
    if ret == False:
        framesLeft = False
        
    return frame, framesLeft

def cropFrame( frame, type):
    (height, width, col) = frame.shape
    if type == "mid":
        y1 = math.floor(height/3)
        y2 = math.floor(2*height/3)

        x1= math.floor(width/3)
        x2 = math.floor(2*width/3)
        
        
    elif type == "bottomRight":
        y1 = math.floor(4*height/5)
        y2 = math.floor(height)

        x1= math.floor(4*width/5)
        x2 = math.floor(width)

        pass
    else:
        raise Exception("'type' was not found, must be one of 'mid', 'bottomRight' ")

    return frame[y1:y2, x1:x2]
