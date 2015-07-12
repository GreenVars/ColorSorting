# GLITCH ART
# Python 3.3
from PIL import Image
from os import listdir
from itertools import product
import colors
import time
def combine(top, bottom, index, convert_to=colors.rgb_to_hsv, convert_back=colors.hsv_to_rgb):
	''' Sort the pixels of two images then rearrange the colors of both images
		based on the others sort '''
	top_pix = top.load()
	bottom_pix = bottom.load()
	w,h = top.size
	a = time.time()
	print ('start' , a)
	top_pixels = (top_pix[x,y] for x in range(w) for y in range(h))
	bottom_pixels = (bottom_pix[x,y] for x in range(w) for y in range(h))
	b = time.time()
	print ('map pixels' , b - a)
	top_pixels = [(c,i) for c,i in zip(map(convert_to,top_pixels),
				 ((x,y) for x in range(w) for y in range(h)))]
	bottom_pixels = [(c,i) for c,i in zip(map(convert_to,bottom_pixels),
					((x,y) for x in range(w) for y in range(h)))]
	d = time.time()
	print ('to hsv' , d - b)
	top_pixels.sort(key=lambda c:c[0][index])
	bottom_pixels.sort(key=lambda c:c[0][index])
	e = time.time()
	print ('sort' , e - d)
	top_pixels = ((convert_back(c), i) for c, i in top_pixels)
	bottom_pixels = ((convert_back(c), i) for c, i in bottom_pixels)
	f = time.time()
	print ('to rgb' , f - e)
	t_dict = {}
	b_dict = {}
	for pixels, cords in zip(zip(bottom_pixels, top_pixels)
						   , product(range(w), range(h))):
		x , y = cords
		t_p, b_p = pixels
		t_dict[(x,y)] = t_p
		b_dict[(x,y)] = b_p
	g = time.time()
	print ('sorted dicts' , g - f)
	for x , y in product(range(w), range(h)):
		t_cord = t_dict[(x,y)][1]
		top_pix[t_cord] = b_dict[(x,y)][0]
		b_cord = b_dict[(x,y)][1]
		bottom_pix[b_cord] = t_dict[(x,y)][0]	
	h = time.time()
	print ('swap pixels' , h - g)
	print ('finish' , h - a)
def pixel_sort(img,index=0, convert_to=colors.rgb_to_hsv, convert_back=colors.hsv_to_rgb):
	''' Sort an images pixels by an index of their color value '''
	pix = img.load()
	w,h = img.size
	pixels = (pix[x,y] for x in range(w) for y in range(h))
	pixels = list(map(convert_to, pixels))
	pixels.sort(key=lambda c:c[index])
	pixels = map(convert_back, pixels)
	for pixel, cord in zip(pixels, product(range(w), range(h))):
		x,y = cord
		pix[x,y] = pixel
def all_rgb(template, index=0, convert_to=colors.rgb_to_hsv):
	''' Requires 64 bit and loads of time '''
	img_names = ["16bithue", "16bitsat", "16bitval"]
	color_img = Image.open("tools/%s.png" % img_names[index])
	w,h = template.size
	temp_pix = template.load()
	color_pix = color_img.load()
	temp_map = (temp_pix[x,y] for x in range(w) for y in range(h))
	temp_map = ((c,i) for c,i in zip(map(convert_to,temp_map),
				((x,y) for x in range(w) for y in range(h))))
	temp_map = sorted(temp_map, key=lambda c:c[0][index])
	temp_map = (i for c, i in temp_map) # ignore color only need cords
	print("SORTED")
	i = 0
	for pixel, cords in zip(temp_map, product(range(w), range(h))):
		temp_pix[pixel] = color_pix[cords]
		if i % ((w*h)//50) == 0:
			print(i)
		i += 1
	print("DONE")
if __name__ == '__main__':
	art = listdir('tests')
	art.remove('Thumbs.db')
	t = time.time()
	#img = Image.open("4096x4096/amazon.png")
	#img = Image.open("1280x720/paint.png")
	#img2 = Image.open('1280x720/magnolia.png')
	#pixel_sort(img, index=0)
	combine(img, img2,index=0, convert_to=colors.rgb_to_hsv, convert_back=colors.hsv_to_rgb)
	#all_rgb(img, index=2)
	print(time.time() - t)
	#img.save('tests/16bitval.png')
	img.save('trials/%s.png' % time.time())
	img2.save('trials/%s.png' % time.time())