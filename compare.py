
import os
import cv2

input_folder='out2'
out_folder='out4'
folder_names=os.listdir(input_folder)

jpg_names=os.listdir(input_folder)


for j in range(len(jpg_names)):
    filename=os.path.join(input_folder,jpg_names[j])
    outfilename=os.path.join(out_folder,jpg_names[j][0:-4]+'.png')
    img=cv2.imread(filename,cv2.IMREAD_GRAYSCALE)
    #img2=cv2.resize(img,(0, 0), fx = 0.5, fy = 0.5)
    img[img<200]=0;
    img[img>=200]=255;
    
    cv2.imwrite(outfilename, img)
    print('now=%d/%d\n'%(j,len(jpg_names)))
    
