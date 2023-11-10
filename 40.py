a=float(input('side 1: '))
b=float(input('side 2: '))
c=float(input('side 3: '))
if a==b and b==c:
    print("The triangle is equilateral")
elif (a==b) or (b==c) or (a==c) :
    print('"The triangle is isosceles"')
else:
        print("The triangle is scalene")