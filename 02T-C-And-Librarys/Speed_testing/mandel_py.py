import numpy as np

def mandel_py(h, w, maxit=20):
	"""
	Returns the Mandelbrot set.
	"""
	x, y = np.ogrid[-2:0.8:w*1j, -1.4:1.4:h*1j]
	c = x+y*1j
	output = np.zeros((w, h), dtype=int) + maxit
	for i in range(h):
		for j in range(w):
			z = c[i,j]
			c0 = c[i,j]
			for k in range(maxit):
				z = z**2 + c0
				if z*z.conjugate() > 4.0:
					output[i, j] = k
					break
	return output.T

if __name__ == '__main__':
	mandel_py(1024, 1024)
