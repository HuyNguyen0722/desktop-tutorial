class BankAccount():
    def __init__(self, ten_nganhang, ten_chutaikhoan, so_taikhoan, so_tien):
        self.ten_nganhang = ten_nganhang
        self.ten_chutaikhoan = ten_chutaikhoan
        self.so_taikhoan = so_taikhoan
        self.so_tien = so_tien
        
    def rut_tien(self, so_tienrut):
        self.so_tienrut = so_tienrut
        if (self.so_tienrut > self.so_tien):
            print("EM quá nghèo để rút tiền")
        else:
            self.so_tien -= so_tienrut
            print("Em giàu vãi ò")
            
    def nap_tien(self, so_tiennap):
        self.so_tien += so_tiennap
        print("Em đã thành tỉ phú")
        
    def in_thong_tin(self):
        print(f"Tài khoản ngân hàng: {self.ten_nganhang}")
        print(f"Chủ tài khoản: {self.ten_chutaikhoan}")
        print(f"Số tài khoản: {self.so_taikhoan}")
        print(f"Số dư hiện tại: {self.so_tien} VNĐ.")
        
tai_khoan = BankAccount("Mbbank", "NGUYEN VAN A", "460017187465", 500000000)
tai_khoan.in_thong_tin()

tai_khoan.rut_tien(20000)
tai_khoan.in_thong_tin()