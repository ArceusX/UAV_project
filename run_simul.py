import simul1
from matplotlib import pyplot as plt
import numpy as np


im=simul1.createbackground(40,40)
im=simul1.noising(128,'gauss',im,100)
#print im
plt.imshow(im,cmap = cm.Greys_r)
