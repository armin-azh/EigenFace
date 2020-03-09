import cv2
import os
path='dataset/'
images=os.listdir('dataset/')
pathSaved=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'/eigneface/gray_dataset/'

counter=1
for im in images:
    image=cv2.imread(path+im)
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    status=cv2.imwrite(os.path.join(pathSaved,'{}.jpeg'.format(counter)),gray)
    print('Picture {} Success'.format(status))
    counter+=1

print(pathSaved)

