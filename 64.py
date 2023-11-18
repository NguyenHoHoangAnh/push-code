# Số lượng xu trong một đô la
PENNY_PER_DOLLAR = 100
NICKEL_PER_DOLLAR = 20
# Khởi tạo biến tổng
total = 0
# Vòng lặp cho đến khi người dùng nhập vào một dòng trống
while True:
    # Nhận giá từ người dùng
    price = input("Nhập giá của sản phẩm: ")

    # Kiểm tra xem giá có phải là một số không
    if not price.isdigit():
        break

    # Thêm giá vào tổng
    total += float(price)

# Tính số xu cần thiết để thanh toán tổng số tiền
coins_needed = int(total * PENNY_PER_DOLLAR)

# Tính số dư khi chia số xu này cho 5
remainder = coins_needed % NICKEL_PER_DOLLAR

# Điều chỉnh tổng số tiền nếu cần thiết
if remainder < 2.5:
    total -= remainder
else:
    total += 5 - remainder

# Hiển thị tổng chi phí và số tiền đến hạn
print("Tổng chi phí:", total)
print("Số tiền đến hạn:", round(total, 2))