from PIL import Image
import numpy as np
import math
import matplotlib.pyplot as plt
from copy import deepcopy

def getGrayColor(rgb):
    gray = int((int(rgb[0])+int(rgb[1])+int(rgb[2]))/3)
    return gray

def setGrayColor(color):
    color = int(color)
    return [color, color, color] 

size = 3
limit = int((size-1)/2)
midSize = size*size


file = input('Enter image name: ')
print('Hello', file)


d = input('Enter D : ') 
d = int(d)


#pepperNoise , SaltNoise , gaussianNoise

imgPep = Image.open('image/'+file+'.bmp')

imgPep = np.asarray(imgPep)
Alpha = deepcopy(imgPep)

for i in range(limit,len(imgPep)-limit):
    for j in range(limit,len(imgPep[i])-limit):
        
        c =0
        num = [0]*midSize

        for k in range(i-limit, i+limit+1):
            for l in range(j-limit, j+limit+1):
                exe = getGrayColor(imgPep[k][l])
                num[c] = exe
                c += 1

        num.sort()
        num.pop(0)
        num.pop(len(num)-1)
        num = sum(num)
        Alpha[i][j] = setGrayColor(num/((size*size)-d))

plt.subplot(2, 2, 1)
plt.imshow(imgPep)
plt.subplot(2, 2, 2)
plt.imshow(Alpha)
plt.show()
