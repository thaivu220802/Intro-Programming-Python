import stdio
import sys
import math

y = int(sys.argv[1])
m = int(sys.argv[2])
d = int(sys.argv[3])

y_0 = y - (14 - m) // 12
x = y_0 + y_0 // 4 - y_0 // 100 + y_0 // 400
m_0 = m + 12 * ((14 - m) // 12) - 2
d_0 = (d + x + (31 * m_0) // 12) % 7

stdio.writeln(d_0)