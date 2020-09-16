import math
import stdio

for i in range (1, 12):
    n = 2 ** i
    stdio.write(str(math.log2(n)) + '\t')
    stdio.write(str(n) + '\t')
    stdio.write(str(n * math.log(n)) + '\t')
    stdio.write(str(n ** 2 ) + '\t')
    stdio.write(str(n ** 3) + '\t')
    stdio.writeln(str(2 ** n) + '\t')
stdio.writeln()