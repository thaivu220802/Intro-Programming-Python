import sys
import stdio

m = int(sys.argv[1])
d = int(sys.argv[2])

dateBetween = (m == 3) and (d >= 20)
dateBetween = dateBetween or ((3 < m) and (m < 6))
dateBetween = dateBetween or (m == 6) and (d <= 20)

stdio.writeln(dateBetween)