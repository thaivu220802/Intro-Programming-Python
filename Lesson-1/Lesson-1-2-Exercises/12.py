import stdio
import sys

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

notTriangle = a >= (b + c)
notTriangle = notTriangle or (b >= (c + a))
notTriangle = notTriangle or (c >= (b + a))

stdio.writeln(not notTriangle)