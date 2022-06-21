a=int(input("Number 1: "))
b=int(input("Number 2: "))
c=int(input("Number 3: "))

s=(a+b+c)/2

area=(s*(s-a)*(s-b)*(s-c))**0.5
print("The area of the triangle is %0.2f" %area)