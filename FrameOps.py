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

def cropFrame( frame, type, w = -1, h = -1):
    #320x 240
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

    elif type == "custom":
        if (h == -1 or w == -1):
            raise Exception("h or w were not set, please set as a positive integer, i.e. h=480, w=320")
        #if (type(h) != "<class 'int'>" or type(w) != "<class 'int'>"):
         #   raise Exception("integer was not passed into h or w")

        y1 = math.floor(height/2 - h/2)
        y2 = math.floor(height/2 + h/2)

        x1 = math.floor(width/2 - w/2)
        x2 = math.floor(width/2 + w/2)

    
    else:
        raise Exception("'type' was not found, must be one of 'mid', 'bottomRight', 'custom' then h=, w= ")

    return frame[y1:y2, x1:x2]
