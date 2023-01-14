import numpy as np
import cv2
import scipy.interpolate

img = cv2.imread("cd-stitched.png",cv2.IMREAD_GRAYSCALE)
Y,X = img.shape
f = scipy.interpolate.RectBivariateSpline(range(Y), range(X), img, kx=2, ky=2)

cx,cy = 63256.883, -146662.097   # center
a = -112.90                      # initial angle, degrees
r = 159965.770                   # radius

def sample(f,a,r):
  n = 209700
  da = 1.2295376502e-6  # ~1.23 urad, about 55 nm
  da *= 180/np.pi
  t = a + da*np.linspace(0,n,n+1)
  x = cx + r*np.cos(t*np.pi/180)
  y = cy - r*np.sin(t*np.pi/180)
  w = f(y, x, grid=False)
  return w

s = sample(f,a,r)
np.savetxt("waveform.dat",s)
