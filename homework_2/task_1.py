import math as m

a = float(input("Enter first side of the triangle: "))
b = float(input("Enter second side of the triangle: "))
c = float(input("Enter third side of the triangle: "))

x = (a+b+c)/2
s = m.sqrt(x*(x-a)*(x-b)*(x-c))
p = 2*x
print("Area of the triangle is: ", s)
print("Perimeter of the triangle is: ", p)