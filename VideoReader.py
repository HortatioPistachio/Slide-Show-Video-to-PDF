#this is a multithreading video reader using opencv that specifies the resoloution of the frames
#i.e. res = 20 means every 20th frame is taken
#based off imutils

from threading import Thread
import cv2
import queue
import threading
import time

class VideoReader:

    def __init__(self, path, res):
        self.vid = cv2.VideoCapture(path)
        self.framesLeft = True
        self.stopped = False
        self.res = res

        #may have to set a max size as not to destroy ram usage, depend of speed of other threads
        self.frameQ = queue.Queue(maxsize=100)

        #initializing the thread
        self.thread = Thread(target=self.update, args=())
        #having the daemon means itll always run in the background like we want
        self.thread.daemon = True

    def start(self):
        self.thread.start()
        return self


    def update(self):
        print("thread started")
        #infinitre loop to keep looping, we will break dependent on certain condiditons
        while (True):
            if (not self.frameQ.full()):
                #end loop if we are out of frames
                if (self.framesLeft == False):
                    break

                for i in range(self.res):
                    ret = self.vid.grab()
                    if ret == False:
                        self.framesLeft = False
                        break

                ret, frame = self.vid.read()

                self.frameQ.put(frame)
                if ret == False:
                    self.framesLeft = False
            else:
                print("sleeping")
                time.sleep(0.1)
        print("queueing complete")

    def getFrame(self):
        return self.frameQ.get()   


    #function return the remaining size of q
    #loop checks to make sure there arent any more frames
    #one the way
    def frameLeft(self):
        return self.framesLeft    