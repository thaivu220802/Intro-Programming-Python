import stdio
import sys

n = int(sys.argv[1])

if n > 0:
    power = 1
    while power <= n:
        stdio.writeln(power)
        power*=2

stdio.writeln()