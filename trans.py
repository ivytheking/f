import scipy.io
from glob import glob
import cv2 as cv

mat_list = glob('./*.mat')
for mat in mat_list:
    data = scipy.io.loadmat(mat)
    name = mat.split('.')[-2]
    img = data['groundTruth'][0][0][0]
    img = (img-1)*255
    cv.imwrite('./%s.png'%name,img)