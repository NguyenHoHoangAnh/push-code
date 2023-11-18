# Khởi tạo biến tổng chi phí
total_cost = 0

# Vòng lặp cho đến khi người dùng nhập vào một dòng trống
while True:
    # Nhập tuổi của khách
    age = input("Nhập tuổi của khách (để trống để thoát): ")

    # Nếu tuổi là một dòng trống, hãy thoát khỏi vòng lặp
    if age == "":
        break

    # Tính giá nhập học cho khách
    if int(age) <= 2:
        cost = 0
    elif int(age) >= 3 and int(age) <= 12:
        cost = 14.00
    elif int(age) >= 65:
        cost = 18.00
    else:
        cost = 23.00

    # Thêm chi phí vào tổng chi phí
    total_cost += cost

# Hiển thị tổng chi phí
print("Chi phí nhập học là $" + str(round(total_cost, 2)))