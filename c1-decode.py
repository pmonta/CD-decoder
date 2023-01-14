import sys
from reedsolo import RSCodec

def parse(t):
  t = t.split()
  f = bytearray(32)
  fe = bytearray(32)
  for i in range(32):
    if t[i+1]=='--':
      f[i] = 0
      fe[i] = 1
    else:
      f[i] = int(t[i+1],16)
      fe[i] = 0
    if i in [12,13,14,15,28,29,30,31]:
      f[i] = 255 - f[i]
  return f,fe
  
class delay1():
  def __init__(self):
    self.f0 = bytearray(32)
    self.f0e = bytearray(32)
  def delay(self, f, fe):
    r = bytearray(32)
    re = bytearray(32)
    r[0::2] = f[0::2]
    r[1::2] = self.f0[1::2]
    re[0::2] = fe[0::2]
    re[1::2] = self.f0e[1::2]
    for i in range(32):
      self.f0[i] = f[i]
      self.f0e[i] = fe[i]
    return r,re

rsc = RSCodec(4)
d = delay1()
frame = 0

for t in sys.stdin.readlines():
  f,e = parse(t)
  f,e = d.delay(f,e)
  try:
    dec0,dec1,epos = rsc.decode(f,erase_pos=[i for i in range(28) if e[i]])
    for i in range(32):
      b = dec1[i]
      print("%02x "%b,end='')
      if i==11 or i==15 or i==27:
        print("    ",end='')
    print()
  except:
    for i in range(32):
      print("-- ",end='')
      if i==11 or i==15 or i==27:
        print("    ",end='')
    print()
  frame += 1
