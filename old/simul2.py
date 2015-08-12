#failed. inefficient

import numpy as np

def createbackground(h,w,px_val=None):
    if px_val is None:
    	img=np.empty([h,w], dtype='uint8')
    	img.fill(np.random.randint(256))
    else:
    	img=np.empty([h,w], dtype='uint8')
    	img.fill(px_val)
    return img.astype('uint8')

def noising(mu,method,img,sigma=None):
	h,w=img.shape

	if method=="gauss":
		img=img+(sigma*np.random.randn(h,w)+mu)

	elif method=="s_p":
		arr=np.arange(h*w)
		arr=np.random.permutation(arr)
		arr=np.reshape(arr,(h,w))
		gate=mu*h*w
		for (y,x), val in np.ndenumerate(arr):
			if val<gate:
				img[y,x]=np.random.choice([0, 255])

	return img.astype('uint8')

def add_UAVs(n,c,sz,shape,img):
	h,w=img.shape
	locy=np.random.randint(h,size=n)
	locx=np.random.randint(w,size=n)

	if shape=="cross":
		tile_pts=np.array([[0,0],[-1,0],[1,0],[0,-1],[0,1]])
		tile_size=np.shape(tile_pts)[0]
		pts=np.empty([sz*sz*tile_size*n,2])

		for k,(c,d) in enumerate(zip(tile_pts[:,0],tile_pts[:,1])):
			for i,(y,x) in enumerate(zip(locy,locx)):
				for a in np.arange(sz):
					for b in np.arange(sz):
						pts[b+a*sz+k*(tile_size-1)+i*sz*sz*(tile_size-1),0]=y+b+c*sz
						pts[b+a*sz+k*(tile_size-1)+i*sz*sz*(tile_size-1),1]=x+a+d*sz

	elif shape=="square":
		tile_pts=np.array([[0,0]])
		tile_size=np.shape(tile_pts)[0]
		pts=np.empty([sz*sz*tile_size*n,2])

		for i,(y,x) in enumerate(zip(locy,locx)):
			for k,(c,d) in enumerate(zip(tile_pts[:,0],tile_pts[:,1])):
				for a in np.arange(sz):
					for b in np.arange(sz):
						pts[b+a*sz+k*(tile_size-1)+i*sz*sz*(tile_size-1),0]=y+b+c*sz
						pts[b+a*sz+k*(tile_size-1)+i*sz*sz*(tile_size-1),1]=x+a+d*sz

	elif shape=="arrow":
		tile_pts=np.array([[0,0],[1,-1],[2,-2],[1,1],[2,2]])
		tile_size=np.shape(tile_pts)[0]
		pts=np.empty([sz*sz*tile_size*n,2])

		for i,(y,x) in enumerate(zip(locy,locx)):
			for k,(c,d) in enumerate(zip(tile_pts[:,0],tile_pts[:,1])):
				for a in np.arange(sz):
					for b in np.arange(sz):
						pts[b+a*sz+k*tile_size+i*sz*sz*tile_size,0]=y+b+c*sz
						pts[b+a*sz+k*tile_size+i*sz*sz*tile_size,1]=x+a+d*sz

	elif shape=="x":
		tile_pts=np.array([[0,0],[1,1],[1,-1],[-1,-1],[-1,1]])
		tile_size=np.shape(tile_pts)[0]
		pts=np.empty([sz*sz*tile_size*n,2])

		for i,(y,x) in enumerate(zip(locy,locx)):
			for k,(c,d) in enumerate(zip(tile_pts[:,0],tile_pts[:,1])):
				for a in np.arange(sz):
					for b in np.arange(sz):
						pts[b+a*sz+k*(tile_size-1)+i*sz*sz*(tile_size-1),0]=y+b+c*sz
						pts[b+a*sz+k*(tile_size-1)+i*sz*sz*(tile_size-1),1]=x+a+d*sz

	for a,b in zip(pts[:,0], pts[:,1]):
		if (a>=0) and (a<h) and (b>=0) and (b<w):
			img[a,b]=color

	return img

def task():
	backgrounds={'black_0':0,'random':None,'white_255':255}
	noise_methods=['gauss','s_p']
	UAV_shapes=['arrow','cross','square2','square3','x']
	params=dict(img_each=100, UAV_num=2,h=50, w=50, gauss_sigma=50, gauss_mu=128, s_p_mu=1)
	fd_out='/home/triet/Desktop/simul_images1/'
	for background, color in backgrounds.iteritems():
		for noise in noise_methods:
			for UAV_shape in UAV_shapes:
				for i in xrange(0,params['img_each']):
					img=createbackground(params['h'],params['w'],color)
					if noise=='gauss':
						img=noising(params['gauss_mu'],noise,img,params['gauss_sigma'])
					elif noise=="s_p":
						img=noising(params['gauss_mu'],noise,img)

					if color==0:
						img=add_UAVs(params['UAV_num'],255,UAV_shape,img)
					elif color==255:
						img=add_UAVs(params['UAV_num'],0,UAV_shape,img)
					elif color==None:
						img=add_UAVs(params['UAV_num'],np.random.randint(256),UAV_shape,img)

					file_name=fd_out+background+'/'+UAV_shape+'/'+'img_{}.txt'.format(i)
					np.savetxt(file_name,img, delimiter=' ')
	
				
