from Animal import Animal

class Mamalia(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak,ukuran_tubuh, jenis_kulit):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.ukuran_tubuh = ukuran_tubuh
        self.jenis_kulit = jenis_kulit

    def info_mamalia(self):
        super().info_animal(),
        print("Ukuran Tubuh \t\t\t : ", self.ukuran_tubuh,
             "\njenis kulit \t\t\t : ", self.jenis_kulit)
        

gajah = Mamalia("Gajah", "Tumbuh-tumbuhan", "Darat", "Melahirkan", "kecil", "Berbulu")
gajah.info_mamalia()
print("=====================")
Kucing = Mamalia("kucing", "Ikan", "Darat", "Melahirkan", "Kecil", "Sedikit berbulu")
Kucing.info_mamalia()
print("=====================")
kuda = Mamalia("kuda", "rumput", "Darat", "Melahirkan", "Berambut")
kuda.info_animal()