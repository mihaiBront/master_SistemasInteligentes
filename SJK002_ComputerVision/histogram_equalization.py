import numpy as np
import cv2 as cv
import argparse as parser
from dataclasses import dataclass

@dataclass
class GlobalSettings(object):
    image_path: cv.Mat

GLOBAL_SETTINGS: GlobalSettings

def loadArgs():
    prs = parser.ArgumentParser()
    
    prs.add_argument("-i", "-image", help="Source image", type=str)
    
    args = prs.parse_args()
    
    return GlobalSettings(cv.imload(prs.image))

if __name__ == "__main__":
    pass