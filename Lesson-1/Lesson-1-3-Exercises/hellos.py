import stdio
import sys

n = int(sys.argv[1])

for i in range(1, n + 1):
    if (i % 100 > 10) and (i % 100 < 20):
        stdio.writeln(str(i) + 'th Hello')
    elif (i % 10 == 1):
        stdio.writeln(str(i) + 'st Hello')
    elif (i % 10 == 2):
        stdio.writeln(str(i) + 'nd Hello')
    elif (i % 10 == 3):
        stdio.writeln(str(i) + 'rd Hello')
    else:
        stdio.writeln(str(i) + 'th Hello')