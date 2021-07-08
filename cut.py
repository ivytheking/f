import cv2 as cv
import os
import numpy as np
size = 256
# root = 'crack/unlabeled'
# gt_root = os.path.join(root,'groundTruth')
# im_root = os.path.join(root,'image') 

# ims = os.listdir(im_root)

# for im in ims:
#     name = im[:-4]
#     im_pt = os.path.join(im_root,im)
#     gt_pt = os.path.join(gt_root,name+'.png')

#     img = cv.imread(im_pt)
#     gt = cv.imread(gt_pt)
#     idx = 0
#     for row in range(4):
#         for col in range(6):
#             0 = row*size
#             r2 = (row+1)*size
#             c1 = col*size
#             c2 = (col+1)*size
#             roi_im = img[0:r2,c1:c2]
#             roi_gt = gt[0:r2,c1:c2]
#             cv.imwrite(os.path.join(im_root,f'{name}_{idx}.jpg'),roi_im)
#             cv.imwrite(os.path.join(gt_root,f'{name}_{idx}.jpg'),roi_gt)
#             idx+=1
# root = 'AITEX'
# gt_root = os.path.join(root,'Mask_images')
# im_root = os.path.join(root,'Defect_images') 

# ims = os.listdir(im_root)

# for im in ims:
#     name = im[:-4]
#     im_pt = os.path.join(im_root,im)
#     img = cv.imread(im_pt)
#     if img.shape[1]!=4096:
#         continue

#     gt_pt = os.path.join(gt_root,name+'_mask.png')
#     if os.path.exists(gt_pt):
#         gt = cv.imread(gt_pt)
#     else:
#         g1 = cv.imread(f'{gt_pt[:-4]}1.png')
#         g2 = cv.imread(f'{gt_pt[:-4]}2.png')
#         if g1 is  None:
#             continue
#         gt = g1+g2
    
    
    
#     idx = 0
#     for col in range(16):
#         c1 = col*size
#         c2 = (col+1)*size
#         roi_im = img[:,c1:c2]
#         roi_gt = gt[:,c1:c2]
#         cv.imwrite(os.path.join(im_root,f'{name}_{idx}.jpg'),roi_im)
#         cv.imwrite(os.path.join(gt_root,f'{name}_{idx}.jpg'),roi_gt)
#         idx+=1

root = 'AITEX/NODefect_images'
im_root = 'AITEX/image'
gt_root = 'AITEX/groundTruth'
for froot,_,fnames in sorted(os.walk(root)):
    for fname in fnames:
        if fname[-4] == '.':
            name = fname[:-4]
            im = cv.imread(os.path.join(froot,fname))
            if im.shape[1]!=4096:
                continue
            idx = 0
            for col in range(16):
                c1 = col*size
                c2 = (col+1)*size
                roi_im = im[:,c1:c2]
                roi_gt = np.zeros(roi_im.shape)
                cv.imwrite(os.path.join(im_root,f'{name}_{idx}.jpg'),roi_im)
                cv.imwrite(os.path.join(gt_root,f'{name}_{idx}.jpg'),roi_gt)
                idx+=1
