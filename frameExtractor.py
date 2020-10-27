import cv2

class FrameOps():
    currentFrameNum = 0

    def getNextFrame(self, vid, res):
        framesLeft = True
        for i in range(res):
            ret, frame = vid.read()
            if ret == False:
                framesLeft = False
                break

        ret, frame = vid.read()
        if ret == False:
            framesLeft = False
            
        return frame, framesLeft


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