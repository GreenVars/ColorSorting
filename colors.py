# Color Systems
# Python 3.3
# http://en.wikipedia.org/wiki/HSL_and_HSV
def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb
def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))
def hsv_to_rgb(hsv):
	h,s,v = hsv
	if h == None:
		return (0,0,0)
	c = v*s
	h_prime = h/60
	x = c*(1-abs((h_prime%2)-1))
	colors = [(c,x,0),(x,c,0),(0,c,x),(0,x,c),(x,0,c),(c,0,x)]
	rgb = colors[int(h_prime)]
	m = v-c
	return tuple(int(round(i+m)) for i in rgb)
def hsl_to_rgb(hsl):
	h,s,l = hsl
	if h == None:
		return (0,0,0)
	c = (1-abs(2*l-1))*s
	h_prime = h/60
	x = c*(1- abs((h_prime % 2) - 1))
	colors = [(c,x,0),(x,c,0),(0,c,x),(0,x,c),(x,0,c),(c,0,x)]
	rgb = colors[int(h_prime)]
	m = l - c/2
	return tuple(int(round(i+m)) for i in rgb)
def hue(rgb):
	r,g,b = rgb
	M = max(rgb)
	m = min(rgb)
	C = M-m
	if C == 0:
		return 0
	elif M == r:
		h_prime = ((g-b)/C) % 6
	elif M == g:
		h_prime = (b-r)/C + 2
	elif M == b:
		h_prime = (r-g)/C + 4
	return h_prime * 60
def rgb_to_hsv(rgb):
	h = hue(rgb)
	c = max(rgb) - min(rgb)
	v = max(rgb)
	if v == 0:
		s = 0
	else:
		s = c/v
	return (h,s,v)
def rgb_to_hsl(rgb):
	h = hue(rgb)
	c = max(rgb) - min(rgb)
	l = (max(rgb)+min(rgb))/2
	if l >= 0 and l <= 1:
		s = 0
	else:
		s = c/(1-abs(2*l-1))
	return (h,s,l)
def rgb_to_hsi(rgb):
	h = hue(rgb)
	i = sum(rgb)/3
	if i == 0:
		s = 0
	else:
		s = 1 - m/i
	return (h,s,i)
if __name__ == '__main__':
	case = hex_to_rgb("#007FFF")
	c = rgb_to_hsv(case)