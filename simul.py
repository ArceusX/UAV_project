import cv2
import numpy as np
import os.path
from scipy.spatial import ConvexHull

def create_background(h,w,px_val=None):
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

def add_UAVs(n,clr,sz,shape,img):

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

	return (img.astype('uint8'),pts.astype('int'),tile_size)

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

def add_UAVs_write_to_file(n,clr,sz,shape,img,file_name):
	im,coords,tile=add_UAVs(n,clr,sz,shape,img)
	coords=np.reshape(coords,(sz*sz*tile,2,n))
	cv2.imwrite(file_name,im)
	bounding_box=np.empty(shape=(2,2,n))
	(bounding_box[0,:,:],bounding_box[1,:,:])=np.amin(coords,axis=0),np.amax(coords,axis=0)
	return bounding_box,im
	dir_name,f_name=os.path.split(file_name)
	f_name,f_ext=f_name.split(".")
	np.savetxt(dir_name+"/"+f_name+"_data.txt",coords,delimiter=" ",newline="\n")




def task():
	backgrounds={'black_0':0,'random':None,'white_255':255}
	noise_methods=['gauss','s_p','None']
	UAV_shapes=['arrow','cross','square','x']
	params=dict(img_each=100, UAV_num=2,h=256, w=256, gauss_sigma=100, gauss_mu=256, s_p_mu=1)
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
						img=add_UAVs(np.random.randint(1,5),255,2,UAV_shape,img)
					elif color==255:
						img=add_UAVs(np.random.randint(1,5),0,2,UAV_shape,img)
					elif color==None:
						img=add_UAVs(np.random.randint(1,5),np.random.randint(256),2,UAV_shape,img)

					file_name=fd_out+background+'/'+UAV_shape+'/'+noise+'/'+'img_{}.png'.format(i)
					im=cv2.imwrite(file_name,img)
					print i
					

def task1():
	for i in xrange(0,10):
		fd_out='/home/triet/Desktop/simul_images1/black_0/arrow/gauss/'
		img=createbackground(256,256,0)
		img=noising(256,'gauss',img,100)
		img=add_UAVs(np.random.randint(1,5),2,255,'arrow',img)
		file_name=fd_out+'img_{}.png'.format(i)
		cv2.imwrite(file_name,img)

	
				
