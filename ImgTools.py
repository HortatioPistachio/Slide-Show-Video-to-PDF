from PIL import Image
import os

#this function takes a bunch of images and converts them to pdf
#path = directoryToImages/ImageName
#images that are added are in the form ImagesName{0} 
#where {0} is numbers starting from zero
#i.e. slide1, slide2, slide3, ....
def ConvertToPdf(path):
    images = []
    counter = 0

    while os.path.exists(path + str(counter) + ".jpeg"):
        fname = path + str(counter) + ".jpeg"
        im = Image.open(fname)
        images.append(im)
        os.remove(fname)
        counter = counter + 1

    images[0].save(r'Slides.pdf', save_all=True, append_images=images)
