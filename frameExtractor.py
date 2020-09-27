import cv2

def frameExtractor(vid):
    frameList = []
    tick = 0
    while( vid.isOpened()):
        
        ret, frame = vid.read()
#        if ret == True:
#            if (tick == 3) :
#                frameList.append(frame)
#                tick = 0
#            else:
#                tick += 1
#        else:
#            break

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    vid.release()
    return frameList