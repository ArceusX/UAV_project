#Random UAVs

import numpy as np

def add_UAVs_random(n,cls,szs,shps,img):
	h,w=img.shape
	colors=np.random.choice(cls,n)
	sizes=np.random.choice(szs,n)
	shapes=np.random.choice(shps,n)
	locy=np.random.randint(h,size=n)
	locx=np.random.randint(w,size=n)

	shape_pts={'cross':np.array([[0,0],[-1,0],[1,0],[0,-1],[0,1]]),
			'square':np.array([[0,0]]),
			'x':np.array([[0,0],[1,1],[1,-1],[-1,-1],[-1,1]]),
			'arrow':np.array([[0,0],[1,-1],[2,-2],[1,1],[2,2]])}

	for i,(cl,sz,shape,x,y) in enumerate(zip(colors,sizes,shapes,locy,locx)):
		tile_pts=shape_pts[shape]
		tile_size=np.shape(tile_pts)[0]

		for k,(c,d) in enumerate(zip(tile_pts[:,0],tile_pts[:,1])):
			for a in np.arange(sz):
				for b in np.arange(sz):
					pty=y+b+c*sz
					ptx=x+a+d*sz
					if (pty>=0) and (pty<h) and (ptx>=0) and (ptx<w):
						img[pty,ptx]=cl
	
	return img.astype('uint8')