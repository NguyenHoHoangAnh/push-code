#BÀI 76
n=int(input("Enter an integer (2 or greater): "))
factor=2
if n>=2:
    print("The prime factors of",n,"are:")
    while factor<=n:
        if n%factor==0:
            print(factor)
            n=n//factor
        else:
            factor=factor+1
else:
    print("Inappropriate value!")