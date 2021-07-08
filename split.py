import cv2 as cv
import os 
import shutil
import numpy as np
import random

root = 'AITEX/defectfree'
im_root = os.path.join(root,'image')
gt_root = os.path.join(root,'groundTruth')
targets = os.listdir(im_root)
num = int(len(targets)*0.2)

for i in range(2):
    path = 'AITEX/test'
    if i==1:
        path = 'AITEX/valid'
    for j in range(num):
        target = random.choice(targets)
        shutil.copy(os.path.join(im_root,target),os.path.join(path,'image'))
        shutil.copy(os.path.join(gt_root,target),os.path.join(path,'groundTruth'))
        targets.remove(target)
for target in targets:
    path = 'AITEX/unlabeled'
    shutil.copy(os.path.join(im_root,target),os.path.join(path,'image'))
    shutil.copy(os.path.join(gt_root,target),os.path.join(path,'groundTruth'))


# gts = os.listdir(gt_root)

# for gt in gts:
#     target = cv.imread(os.path.join(gt_root,gt))
#     if np.sum(target)==0:
#         ipt = 'AITEX/defectfree/image'
#         gpt = 'AITEX/defectfree/groundTruth'
#     else:
#         ipt = 'AITEX/defect/image'
#         gpt = 'AITEX/defect/groundTruth'
#     shutil.move(os.path.join(im_root,gt),ipt)
#     shutil.move(os.path.join(gt_root,gt),gpt)