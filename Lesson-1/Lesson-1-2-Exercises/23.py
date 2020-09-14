import math
import stdio
import sys

x = float(sys.argv[1])
y = float(sys.argv[2])

r = math.sqrt(x ** 2 + y ** 2)
theta = math.atan2(y, x)

stdio.writeln(r)
stdio.writeln(theta)