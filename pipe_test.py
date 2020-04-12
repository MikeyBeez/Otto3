#!/usr/bin/env python3
import sys
k = 0
try:
   for line in iter(sys.stdin.readline, b''):
      k = k + 1
      if "julius" in line:
        print (line)
except KeyboardInterrupt:
   sys.stdout.flush()
   pass
   #     print (k)
