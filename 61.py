number = float(input("Enter a number: "))
if number == 0:
        print("Error!") 
        exit()
sum=0
count=0
while number != 0:
    sum+=number
    count+=1
    number = float(input("Enter another number (or 0 to stop) : "))   
    if number == 0:
      break
    else:
     sum+= number
     count += 1
     average = sum / count
print("The average is:", average)