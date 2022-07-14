#(-b+-(b**2-4ac)) / 2a

import cmath

a=int(input("Number 1: "))
b=int(input("Number 2: "))
c=int(input("Number 3: "))

d=((b**2)-(4*a*c))*0.5

sol1=(-b-cmath.sqrt(d))/2*a
sol2=(-b+cmath.sqrt(d))/2*a

print("The solutions are {0} and {1}".format(sol1,sol2))