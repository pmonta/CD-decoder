import numpy as np
import scipy.interpolate
import scipy.signal
import sys

# correct for timing drift

def tcorr(n):
  tcorr_p = [(0,4158.5),(6,4155.1),(15,4157.7),(22,4161.4),(32,4167.3),(42,4175.9)]
  t = [4751*c[0] for c in tcorr_p]
  c = [c[1] for c in tcorr_p]
  f = scipy.interpolate.interp1d(t,c,kind="quadratic",fill_value="extrapolate")
  return f(np.arange(n))-4158.5

x = np.loadtxt(sys.stdin)
n = len(x)
t = np.arange(n) - tcorr(n)
f = scipy.interpolate.interp1d(t,x,fill_value="extrapolate")

s = 4751/588   # samples per bit

tap=0.2
z = scipy.signal.lfilter([-tap,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0-tap],1,x)   # equalizer (approximate)
f = scipy.interpolate.interp1d(t,z,fill_value="extrapolate")

ti = 12.09+s*np.arange(0,25500)   # symbol timing
wk = f(ti)

thresh = 82.8   # slicing threshold

s = ['1' if b else '0' for b in wk>thresh]
print(''.join(s),end='')
