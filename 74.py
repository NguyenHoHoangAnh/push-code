MIN = 1
MAX = 10
print("  ", end="")
for i in range(MIN, MAX + 1):
    print("%4d" % i, end="")
print()
for i in range(MIN, MAX + 1):
    print("%4d" % i, end="")
    for j in range(MIN, MAX + 1):
        print("%4d" % (i* j), end="")
    print()     
