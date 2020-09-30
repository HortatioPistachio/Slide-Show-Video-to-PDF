import cv2

def frameExtractor(vid):
    frameList = []
    tick = 0
    ret, frame = vid.read()
    while( ret == True):
        
        ret, frame = vid.read()
        if ret == True:
            if (tick == 10) :
                frameList.append(frame)
                tick = 0
            else:
                tick += 1
        else:
            break

    cv2.imshow('frame', frameList[10])
    print(len(frameList))
    input("Press Enter to continue...")
    vid.release()
    return frameList