import numpy as np
import simul1

#Stores the points.
def add_UAVs1(n,clr,sz,shape,img):

	h,w=img.shape
	locy=np.random.randint(h,size=n)
	locx=np.random.randint(w,size=n)
	pts=np.empty(shape=(0,2))

	shape_pts={'cross':np.array([[0,0],[-1,0],[1,0],[0,-1],[0,1]]),
			'square':np.array([[0,0]]),
			'x':np.array([[0,0],[1,1],[1,-1],[-1,-1],[-1,1]]),
			'arrow':np.array([[0,0],[1,-1],[2,-2],[1,1],[2,2]])}

	tile_pts=shape_pts[shape]
	tile_size=np.shape(tile_pts)[0]

	for i,(y,x) in enumerate(zip(locy,locx)):
		for k,(c,d) in enumerate(zip(tile_pts[:,0],tile_pts[:,1])):
			for a in np.arange(sz):
				for b in np.arange(sz):
					pts=np.append(pts,[[y+b+c*sz,x+a+d*sz]], axis=0)

	for (y,x) in zip(pts[:,0], pts[:,1]):
		if (y>=0) and (y<h) and (x>=0) and (x<w):
			img[y,x]=c

	return img.astype('uint8')

#About 2.5 times faster

def add_UAVs(n,clr,sz,shape,img):
	h,w=img.shape
	locy=np.random.randint(h,size=n)
	locx=np.random.randint(w,size=n)

	shape_pts={'cross':np.array([[0,0],[-1,0],[1,0],[0,-1],[0,1]]),
			'square':np.array([[0,0]]),
			'x':np.array([[0,0],[1,1],[1,-1],[-1,-1],[-1,1]]),
			'arrow':np.array([[0,0],[1,-1],[2,-2],[1,1],[2,2]])}

	tile_pts=shape_pts[shape]
	tile_size=np.shape(tile_pts)[0]

	for i,(y,x) in enumerate(zip(locy,locx)):
		for k,(c,d) in enumerate(zip(tile_pts[:,0],tile_pts[:,1])):
			for a in np.arange(sz):
				for b in np.arange(sz):
					pty=y+b+c*sz
					ptx=x+a+d*sz
					if (pty>=0) and (pty<h) and (ptx>=0) and (ptx<w):
						img[pty,ptx]=clr

	return img.astype('uint8')