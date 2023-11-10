thang = int(input("Nhập tháng: "))
ngay = int(input("Nhập ngày: "))
ngay_le = {
  (1, 1): "Ngày đầu năm",
  (7, 1): "Ngày Canada",
  (12, 25): "Ngày Giáng sinh"
}
if (thang, ngay) in ngay_le.keys():
  print(ngay_le[(thang, ngay)])
else:
  print("Thang va ngay nhap vao khong tuong ung voi mot ngay le co đinh")
