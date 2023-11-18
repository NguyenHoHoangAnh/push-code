m=int(input("m= "))
n=int(input("n= "))
d=min(m,n)
while m%d!=0 or n%d!=0:
    d=d-1
print (d,"is the greatest common divisor of",n,"and",m)