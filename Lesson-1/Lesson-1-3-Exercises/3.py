import stdio
import sys

a = float(sys.argv[1])
b = float(sys.argv[2])

if (0.0 < a) and (a < 1.0) and (0.0 < b) and (b < 1.0):
    stdio.writeln(True)
else:
    stdio.writeln(False)