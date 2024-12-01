class PhuongTien:
    def __init__(self, banhxe, nhienlieu, mausac, giatien):
        self.banhxe = banhxe
        self.nhienlieu = nhienlieu
        self.mausac = mausac
        self.giatien = giatien
    
    def thong_tin(self):
        return f"Phương tiện có {self.banhxe} bánh, chạy bằng {self.nhienlieu}, màu {self.mausac}, giá {self.giatien}."

# Lớp con: Xe máy
class XeMay(PhuongTien):
    def __init__(self, banhxe, nhienlieu, mausac, giatien, loai_xe):
        super().__init__(banhxe, nhienlieu, mausac, giatien)
        self.loai_xe = loai_xe
    
    def thong_tin(self):
        base_info = super().thong_tin()
        return f"{base_info} Loại xe: {self.loai_xe}."

# Lớp con: Xe ô tô
class XeOTo(PhuongTien):
    def __init__(self, banhxe, nhienlieu, mausac, giatien, so_cho_ngoi):
        super().__init__(banhxe, nhienlieu, mausac, giatien)
        self.so_cho_ngoi = so_cho_ngoi
    
    def thong_tin(self):
        base_info = super().thong_tin()
        return f"{base_info} Số chỗ ngồi: {self.so_cho_ngoi}."
    
# Tạo đối tượng cho Xe máy
xe_may = XeMay(2, "xăng", "đỏ", 20000000, "tay ga")
print(xe_may.thong_tin())

# Tạo đối tượng cho Xe ô tô
xe_oto = XeOTo(4, "dầu", "trắng", 700000000, 7)
print(xe_oto.thong_tin())
        
    