import stdio
import sys
import random

n = int(sys.argv[1])

sum = 0
num1 = random.random()
stdio.writeln(num1)
max = num1
min = num1

for i in range(2, n+1):
    num = random.random()
    stdio.writeln(num)
    sum += num
    if max < num:
        max = num
    elif min > num:
        min = num

stdio.writeln('Average value: ' + str(sum / n))
stdio.writeln('Maximum: ' + str(max))
stdio.writeln('Minimum: ' + str(min))
