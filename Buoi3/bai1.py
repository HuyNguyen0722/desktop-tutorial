class PhuongTien:
    def __init__(self, bien_so, hang_so, nhien_lieu):
        self.bien_so = bien_so
        self.hang_so = hang_so
        self.nhien_lieu = nhien_lieu
        
a = PhuongTien("15B3-47671", "Honda", "110cc")
print(a.bien_so, a.hang_so, a.nhien_lieu)