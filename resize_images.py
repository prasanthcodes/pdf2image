
import os
import cv2

input_folder='input_dir2'
out_folder='out_folder'
folder_names=os.listdir(input_folder)

jpg_names=os.listdir('input_dir')

for i in range(len(folder_names)):
    jpg_names=os.listdir(os.path.join(input_folder,folder_names[i]))
    out_folder2=os.path.join(out_folder,folder_names[i])
    if os.path.exists(out_folder2)==False:
        os.mkdir(out_folder2)
        
    for j in range(len(jpg_names)):
        filename=os.path.join(input_folder,folder_names[i],jpg_names[j])
        outfilename=os.path.join(out_folder2,jpg_names[j])
        img=cv2.imread(filename)
        img2=cv2.resize(img,(0, 0), fx = 0.5, fy = 0.5)
        cv2.imwrite(outfilename, img2)
        print('now=%d/%d,%d/%d\n'%(i,len(folder_names),j,len(jpg_names)))

