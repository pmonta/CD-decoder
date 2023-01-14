import numpy as np
import sys
import efm

def decode_cd(s):
  if s in efm.efm_decode_table:
    return "%02x"%efm.efm_decode_table[s]
  elif s=='00100000000001':
    return "s0"
  elif s=='00000000010010':
    return "s1"
  else:
    return "--"

def decode(s):
  if s in efm.efm_decode_table:
    return efm.efm_decode_table[s]
  else:
    return 0

while True:
  s = sys.stdin.read(588)
  if len(s)!=588:
    break
  if s[0:24]!='100000000001000000000010':
    print("bad sync")
    sys.exit()
  for i in range(33):
    b14 = s[24+3+17*i:24+3+17*i+14]
    b = decode_cd(b14)
    print("%s "%b,end='')
    if i==0 or i==12 or i==16 or i==28:
      print("    ",end='')
  print()
