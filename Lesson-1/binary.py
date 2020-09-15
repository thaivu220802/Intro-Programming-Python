import stdio
import sys
import math

n = int(sys.argv[1])
v = 1

while v * 2 <= n:
    v *= 2

while v > 0:
    if n >= v:
        stdio.write('1')
        n -= v
    else:
        stdio.write('0')
    v //= 2

stdio.writeln()