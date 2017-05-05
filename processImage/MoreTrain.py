import pickle
from PIL import Image
import os
from processI import ProcessI
from rules import Rules

rules = Rules().getrules()
data_train_root = os.getcwd() + "/SelectedTrainingSet"
data_train = {}
symbol_train = {}
image_train = {}


def gettrainsymbol():
    for f in os.listdir(data_train_root):
        if f.endswith(".png"):
            im1,im2 = ProcessI(data_train_root).processImage(f) #im1 is image data, im2 is image
            image_train[f] = im1
            symbol_train[f] = rules[f.split(".")[0].split("_")[3]]
    data_train["images"] = image_train
    data_train["labels"] = symbol_train
    pf = open("train2.pkl","wb")
    pickle.dump(data_train, pf)


def main():
    gettrainsymbol()

if __name__ == "__main__":
    main()
