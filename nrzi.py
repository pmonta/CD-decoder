import sys

s = sys.stdin.read()
s = s[504:]  # frame sync

c0 = '1' if s[0]=='0' else '0'

for c in s:
    print('1' if c0!=c else '0',end='')
    c0 = c
