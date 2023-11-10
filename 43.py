menhgia = int(input("Nhập mệnh giá của tờ tiền: "))
if menhgia not in [1, 2, 5, 10, 20, 50, 100]:
    print("Lỗi: Mệnh giá không hợp lệ")
    exit()
if menhgia == 1:
    print("George Washington")
elif menhgia == 2:
    print("Thomas Jefferson")
elif menhgia == 5:
    print("Abraham Lincoln")
elif menhgia == 10:
    print("Alexander Hamilton")
elif menhgia == 20:
    print("Andrew Jackson")
elif menhgia == 50:
    print("Ulysses S. Grant")
else:
    print("Benjamin Franklin")