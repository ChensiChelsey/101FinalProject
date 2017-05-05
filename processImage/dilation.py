from PIL import Image
import os
from processI import ProcessI
import random

data_mtrain_root = os.getcwd() + "/SelectedTrainingSet"

for subdir in os.listdir(data_mtrain_root):
     if not subdir.startswith("."):
         for f in os.listdir(data_mtrain_root + "/" +subdir):
             if f.endswith(".jpg"):
                 im1,im2 = ProcessI(data_mtrain_root + "/" +subdir+"/").processImage(f)
                 im2.save(data_mtrain_root + "/" +subdir+"/"+f)
