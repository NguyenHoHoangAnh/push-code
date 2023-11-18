import math
x_first=int(input("Enter the x part of the coordinate: "))
y_first=int(input("Enter the y part of the coordinate: "))
prev_x=x_first
prev_y=y_first
list_distance=[]
while True:
    x_str=input("Enter the x part of the coordinate: (blank to quit): ")
    if x_str=="":
        break
    x=int(x_str)
    y=int(input("Enter the y part of the coordinate: "))
    distance=math.sqrt((x-prev_x)**2+(y-prev_y)**2)
    list_distance.append(distance)
    prev_x=x
    prev_y=y    
last_distance=math.sqrt((prev_x-x_first)**2+(prev_y-y_first)**2)
list_distance.append(last_distance)
perimeter=sum(list_distance)
print("The perimeter of that polygon is", perimeter)