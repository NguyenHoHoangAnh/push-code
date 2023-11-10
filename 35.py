n=int(input("Human years: "))
if n>0:
    if n<=2:
        print("Dog years:",n*10.5)
    elif n>2:
        print("Dog years:",21+(n-2)*4)
else:
    print("Inappropriate value!")