n=input("Enter a binary: ")
dem=len(n)
i=1
decimal=0
while i<=dem:
    digit_str=n[i-1]
    digit=int(digit_str)
    decimal=(decimal*2)+digit
    i=i+1
print(n,"-->",decimal)