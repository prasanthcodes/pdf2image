
import os
import cv2
import numpy as np
from skimage.metrics import structural_similarity


input_folder1='out3'
input_folder2='out4'
outfile='similarity.csv'

img_names=os.listdir(input_folder1)

fid1=open(outfile,'wt')
fid1.write('img1_0s,img1_1s,img2_0s,img2_1s,ratio1,ratio2 \n')

for j in range(len(img_names)):
    filename1=os.path.join(input_folder1,img_names[j])
    filename2=os.path.join(input_folder2,img_names[j])
    
    img1=cv2.imread(filename1,cv2.IMREAD_GRAYSCALE)
    #img1=img1[:,:,0]
    sz1=img1.shape
    img2=cv2.imread(filename2,cv2.IMREAD_GRAYSCALE)
    #img2=img2[:,:,0]
    sz2=img2.shape

    (score, diff) = structural_similarity(img1, img2, full=True)
    diff = (diff * 255).astype("uint8")
    cv2.imwrite(str(j)+'.png', diff)
    
    v1=np.count_nonzero(img1==0)
    v2=np.count_nonzero(img1==255)
    v3=np.count_nonzero(img2==0)
    v4=np.count_nonzero(img2==255)
    outstr=str(v1)+','+str(v2)+','+str(v3)+','+str(v4)+','+str(score)+'\n'
    fid1.write(outstr)
    print('now=%d/%d\n'%(j,len(img_names)))
    
fid1.close()
