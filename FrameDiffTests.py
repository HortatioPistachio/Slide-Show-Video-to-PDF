import FrameOps
import numpy as np
import cv2


class FrameDiffTest:
    
    def __init__(self, initFrame):
        self.pastFrame= initFrame
        self.pastBWSum = 0
        self.preFrameSums = [0, 0]
        self.tolerance = 100

    #this is the testing funciton, run this an itll run the test and return true if all pass
    #future plans is to be able to add certain types of test types
    def test(self, currentFrame): 

        if np.sum( self.sumTest(currentFrame)) == 0:
           return False

        if self.videoTest(currentFrame):
            return False
        
        return True

    #this function returns an all black canvas
    def blank(self):
        return np.zeros(shape=[512,512,3], dtype = np.uint8)
        
    #this test, crops out the middle of the picture (gernerall the useful part)
    #and check whether or not it has changed since the last frame
    #doesnt work great becuase the video quality is so shotty it always changes
    #changed to b&W to reduce noise
    def frameMidChange(self,currentFrame):
        currentFrameCrop = cv2.cvtColor( FrameOps.cropFrame(currentFrame, 'mid'), cv2.COLOR_BGR2GRAY)
        prevCrop = cv2.cvtColor(FrameOps.cropFrame(self.pastFrame, 'mid'), cv2.COLOR_BGR2GRAY)
        self.pastFrame = currentFrame
        print( abs(np.sum(currentFrameCrop) - np.sum(prevCrop) ) )
        if ( abs( np.sum(currentFrameCrop) - np.sum(prevCrop) ) > 100000 ):
            return  currentFrame

        return self.blank()


    #this function converts to BW and then sum up all the pixels on the screen and then compare to the previous sum
    def sumTest(self, currentFrame):
        currentFrame = FrameOps.cropFrame(currentFrame, "mid")
        currentFrameBW = cv2.cvtColor( currentFrame, cv2.COLOR_BGR2GRAY)
        #prevFrameBW = cv2.cvtColor( self.pastFrame, cv2.COLOR_BGR2GRAY)

        self.pastFrame = currentFrame

        currentVal = np.sum(currentFrameBW) // 10000
        preVal = self.pastBWSum
        self.pastBWSum = currentVal
        

        #the constant value here is the tolerance to pick a slide to be save,  100 works well
        #too high you will miss slides, too low and you will get double ups
        if(abs(currentVal-preVal) > self.tolerance):
            return currentFrame
        return self.blank()
        
    #test if there is a video, stores frame sums for comparision
    #looks for frame sequaence in the form:
    # [A] [B] [C] where A,B and C are differnt
    #this indicates fast moving picture, hence video
    #sorta works sort doesnt, not to sure why, still outputs 2 or 3 video slides in each rep
    def videoTest(self, currentFrame):
        #can be a bit looser on this test we are testing 3 difference frame and if any are the same we pass
        currentFrame = FrameOps.cropFrame(currentFrame, "mid")
        localTolerance = 0.3*self.tolerance
        currentFrameBW = cv2.cvtColor( currentFrame, cv2.COLOR_BGR2GRAY)

        #this scaling may cause problems for different video sizes
        currentVal = np.sum(currentFrameBW) // 10000

        #test if sums are significantly differnt as expected in video

        AB  = abs(self.preFrameSums[1] - self.preFrameSums[0])
        BC = abs(self.preFrameSums[1] - currentVal)

        self.preFrameSums.append(currentVal)

        #cleans up so the list doesnt get too long
        del self.preFrameSums[0]

        if (AB > localTolerance and BC > localTolerance):
            print("in video")
            return False
        
        return True