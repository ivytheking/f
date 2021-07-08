import cv2 as cv
import os
import numpy as np
from glob import glob
import shutil

lpt = './kol/label'
ipt = './kol/image'
labels = glob('%s/*bmp'%lpt)

for label in labels:
    # opt = os.path.join(lpt,label)
    name = (label.split('.')[-2]).split('/')[-1]

    rlabel = cv.imread(label,0)
    pix = np.sum(rlabel)

    if pix ==0:#OK
        npt = 'OK'
    else:
        npt = 'NG'
    
    shutil.move(label,os.path.join(lpt,npt,'%s.bmp'%name))
    shutil.move(os.path.join(ipt,'%s.jpg'%name),os.path.join(ipt,npt,'%s.jpg'%name))
