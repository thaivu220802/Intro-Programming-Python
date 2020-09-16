import math
import sys
import stdio

a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])

if a == 0:
    stdio.writeln(-c / b)
else:
    discriminant = b*b - 4*a*c
    if discriminant < 0:
        stdio.writeln('Equation has no real roots.')
    elif discriminant == 0:
        stdio.writeln(- b / (2 * a))
    else:
        discriminant = math.sqrt(discriminant)
        stdio.writeln((-b - discriminant)/(2*a))
        stdio.writeln((-b + discriminant)/(2*a))

stdio.writeln()