#failed. inefficient
import numpy as np

def add_UAVs(n,color,shape,img):
	h,w=img.shape
	locy=np.random.randint(h,size=n)
	locx=np.random.randint(w,size=n)

	if shape=="cross":
			tile_pts=np.array([[0,0],[-1,0],[1,0],[0,-1],[0,1]])
			tile_size=np.shape(tile_pts)[0]
			pts=np.empty([tile_size*n,2])

			for i,(y,x) in enumerate(zip(locy,locx)):
				for k,(c,d) in enumerate(zip(tile_pts[:,0],tile_pts[:,1])):
					pts[k+i*tile_size,0]=y+c
					pts[k+i*tile_size,1]=x+d

	if shape=="square":
		tile_pts=np.array([[0,0]])
		tile_size=np.shape(tile_pts)[0]
		pts=np.empty([tile_size*n,2])

		for i,(y,x) in enumerate(zip(locy,locx)):
			for k,(c,d) in enumerate(zip(tile_pts[:,0],tile_pts[:,1])):
				pts[k+i*tile_size,0]=y+c
				pts[k+i*tile_size,1]=x+d

	if shape=="arrow":
		tile_pts=np.array([[0,0],[1,-1],[2,-2],[1,1],[2,2]])
		tile_size=np.shape(tile_pts)[0]
		pts=np.empty([tile_size*n,2])

		for i,(y,x) in enumerate(zip(locy,locx)):
			for k,(c,d) in enumerate(zip(tile_pts[:,0],tile_pts[:,1])):
				pts[k+i*tile_size,0]=y+c
				pts[k+i*tile_size,1]=x+d

	if shape=="x":
		tile_pts=np.array([[0,0],[1,1],[1,-1],[-1,-1],[-1,1]])
		tile_size=np.shape(tile_pts)[0]
		pts=np.empty([tile_size*n,2])

		for i,(y,x) in enumerate(zip(locy,locx)):
			for k,(c,d) in enumerate(zip(tile_pts[:,0],tile_pts[:,1])):
				pts[k+i*tile_size,0]=y+c
				pts[k+i*tile_size,1]=x+d

	pts=pts.astype('int8')

	for a,b in zip(pts[:,0], pts[:,1]):
		if (a>=0) and (a<h) and (b>=0) and (b<w):
			img[a,b]=color

		return img