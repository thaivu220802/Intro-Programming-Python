import sys
import stdio

for i in range (1000, 2000):
    if(i % 5 == 4):
        stdio.writeln(str(i))
    else:
        stdio.write(str(i) + '\t')

stdio.writeln()