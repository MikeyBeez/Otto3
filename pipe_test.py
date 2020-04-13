#!/usr/bin/env python3
import sys
try:
   for line in iter(sys.stdin.readline, b''):
      if "julius" in line or "julia" in line:
        print (line)
except KeyboardInterrupt:
   sys.stdout.flush()
   pass
