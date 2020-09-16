import math
import stdio
import sys

t = float(sys.argv[1])
v = float(sys.argv[2])

if ((t > 50) or (t < -50)) or ((v > 120) or (v < 3)):
    stdio.writeln('Invalid input')
else:
    w = 35.74 + 0.6215*t + (0.4275*t - 35.75) * (v ** 0.16)
    stdio.writeln(w)