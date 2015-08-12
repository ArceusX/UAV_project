import cv2
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
	
def task():
	backgrounds={'black_0':0,'random':None,'white_255':255}
	noise_methods=['gauss','s_p']
	UAV_shapes=['arrow','cross','square2','square3','x']
	params=dict(img_each=2, UAV_num=2, UAV_color=128, h=50, w=50, gauss_sigma=50, gauss_mu=128, s_p_mu=1)
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
					img=add_UAVs(params['UAV_num'],params['UAV_color'],UAV_shape,img)
					file_name=fd_out+background+'/'+UAV_shape+'/'+'img_{}.txt'.format(i)
					np.savetxt(file_name,img, delimiter=' ')
	
				
