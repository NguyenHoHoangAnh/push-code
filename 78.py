#BÀI 78
result=""
q=int(input("Enter a decimal: "))
decimal=q
while q>0:
    r=q%2
    result=str(r)+result
    q=q//2
print(decimal,"-->",result)