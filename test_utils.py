import cv2
import numpy as np


def colorchange(image):
    x=image
    #x=cv2.imread(x)
    x=cv2.cvtColor(x,cv2.COLOR_BGR2YUV)
    return x
def normalise(image):
    x=image/255
    return x

def preprocess(image):
    image=colorchange(image)
    image=image[60:140, :, :]
    image=normalise(image)
    return image                
