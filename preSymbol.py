import os
import pickle
import pprint
import random
from PIL import Image, ImageFilter
import cv2
import numpy as np
from processI import ProcessI
from skimage.transform import resize,warp,AffineTransform

class PreSymbol:

    def __init__(self):
        self.dataroot = os.getcwd() + "/data/test/"
        self.ps = ProcessI(self.dataroot)

    def getsymbol(self):
        # filelist = [ f for f in os.listdir(self.dataroot) if f.endswith(".png") ]
        # for f in filelist:
        #     os.remove(self.dataroot + f)
        for f in os.listdir(self.dataroot):
            if f.endswith(".png"):
                im1,im2 = self.ps.processImage(f) #im1 is image data, im2 is image
                im2.save(self.dataroot+f)

                # im3 = cv2.imread(self.dataroot+f)
                # print im3
                # im3 = self.ps.image_deformation(im3)
                # # print im3
                # im4 = Image.fromarray(np.uint8(im3))
                # im4.save(self.dataroot+"trans"+f)

if __name__ == "__main__":
    PreSymbol().getsymbol()
