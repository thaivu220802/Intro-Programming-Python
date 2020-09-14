import sys
import stdio
import math

a = int(sys.argv[1])
b = int(sys.argv[2])

evenDivide = (a % b) == 0
evenDivide = evenDivide or ((b % a) == 0)

stdio.writeln(evenDivide)