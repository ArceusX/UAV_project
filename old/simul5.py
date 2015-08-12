import numpy as np

def add_UAVs(n,c,sz,shape,img):
	h,w=img.shape
	locy=np.random.randint(h,size=n)
	locx=np.random.randint(w,size=n)
	pts=np.empty(shape=(0,2))


	if shape=="cross":
		tile_pts=np.array([[0,0],[-1,0],[1,0],[0,-1],[0,1]])
		tile_size=np.shape(tile_pts)[0]

		for i,(y,x) in enumerate(zip(locy,locx)):
			for k,(c,d) in enumerate(zip(tile_pts[:,0],tile_pts[:,1])):
				for a in np.arange(sz):
					for b in np.arange(sz):
						pts=np.append(pts,[[y+b+c*sz,x+a+d*sz]], axis=0)

						#pts[b+a*sz+k*tile_size+i*sz*sz*tile_size,0]=y+b+c*sz
						#pts[b+a*sz+k*tile_size+i*sz*sz*tile_size,1]=x+a+d*sz

	elif shape=="square":
		tile_pts=np.array([[0,0]])
		tile_size=np.shape(tile_pts)[0]

		for i,(y,x) in enumerate(zip(locy,locx)):
			for k,(c,d) in enumerate(zip(tile_pts[:,0],tile_pts[:,1])):
				for a in np.arange(sz):
					for b in np.arange(sz):
						pts=np.append(pts,[[y+b+c*sz,x+a+d*sz]], axis=0)

	elif shape=="arrow":
		tile_pts=np.array([[0,0],[1,-1],[2,-2],[1,1],[2,2]])
		tile_size=np.shape(tile_pts)[0]

		for i,(y,x) in enumerate(zip(locy,locx)):
			for k,(c,d) in enumerate(zip(tile_pts[:,0],tile_pts[:,1])):
				for a in np.arange(sz):
					for b in np.arange(sz):
						pts=np.append(pts,[[y+b+c*sz,x+a+d*sz]], axis=0)

	elif shape=="x":
		tile_pts=np.array([[0,0],[1,1],[1,-1],[-1,-1],[-1,1]])
		tile_size=np.shape(tile_pts)[0]

		for i,(y,x) in enumerate(zip(locy,locx)):
			for k,(c,d) in enumerate(zip(tile_pts[:,0],tile_pts[:,1])):
				for a in np.arange(sz):
					for b in np.arange(sz):
						pts=np.append(pts,[[y+b+c*sz,x+a+d*sz]], axis=0)

	for (y,x) in zip(pts[:,0], pts[:,1]):
		if (y>=0) and (y<h) and (x>=0) and (x<w):
			img[y,x]=c

	return img