import sys
import stdio

n = int(sys.argv[1])
power = 1
while power * 2 <= n:
    power *= 2

stdio.writeln(power);