import numpy
import scipy
from scipy import ndimage


im = scipy.misc.imread('Kalpana.jpeg')
im = im.astype('int32')
#dx = ndimage.sobel(im, 0)   horizontal derivative
#dy = ndimage.sobel(im, 1)  # vertical derivative
LoG = ndimage.gaussian_laplace(im, 2)
thres = numpy.absolute(LoG).mean() * 0.25
output = scipy.zeros(LoG.shape)
w = output.shape[1]
h = output.shape[0]

for y in range(1, h - 1):
    for x in range(1, w - 1):
        patch = LoG[y-1:y+2, x-1:x+2]
        p = LoG[y, x]
        maxP = patch.max()
        minP = patch.min()
        if (p.any() > 0):
            zeroCross = True if minP < 0 else False
        else:
            zeroCross = True if maxP > 0 else False
        if ((maxP - minP) > thres) and zeroCross:
            output[y, x] = 1

scipy.misc.imsave('gaussian3.jpg', output)