import simul
from matplotlib import pyplot as plt
import numpy as np

im=simul.create_background(25,25)
x,im=simul.add_UAVs_write_to_file(2,120,1,'x',im,'/home/triet/Desktop/test_folder/img0.png')
print x
plt.imshow(im)

