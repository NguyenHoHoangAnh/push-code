import random
max=random.randint(1,100)
count=0
print(max)
for _ in range (99):
    n=random.randint(1,100)
    if n>max:
        max=n
        print(n,"<== Update")
        count=count+1
    else:
        print (n)
print("The maximum value found was",max)
print("The maximum value was updated",count,"times")
