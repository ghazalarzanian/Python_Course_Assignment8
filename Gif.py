import os
import imageio
myfiles=os.listdir('Photos')
images=[]
for i in range(len(myfiles)):
    image=imageio.imread('Photos/'+myfiles[i])
    images.append(image)
imageio.mimsave('Gifs.gif',images)