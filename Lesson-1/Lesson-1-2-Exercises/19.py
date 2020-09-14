import sys
import stdio
import math

G = 9.80665
x_0 = float(sys.argv[1])
v_0 = float(sys.argv[2])
t   = float(sys.argv[3])

stdio.writeln(x_0 + v_0 * t + G * t ** 2 / 2)