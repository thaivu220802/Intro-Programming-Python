import sys
import stdio

x = float(sys.argv[1])
y = float(sys.argv[2])
z = float(sys.argv[3])

orderCheck = (x < y) and (y < z)
orderCheck = orderCheck or ((x > y) and (y > z))

stdio.writeln(orderCheck)