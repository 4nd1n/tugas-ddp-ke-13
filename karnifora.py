from Animal import Animal

class Karnifora(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak,ukuran_tubuh, jenis_kulit):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.ukuran_tubuh = ukuran_tubuh
        self.jenis_kulit = jenis_kulit

    def info_Karnifora(self):
        super().info_animal(),
        print("Ukuran Tubuh \t\t\t : ", self.ukuran_tubuh,
             "\njenis kulit \t\t\t : ", self.jenis_kulit)
        

Beruang = Karnifora("Beruang", "Bambu", "Hutan", "Melahirkan", "Berbadan besar", "Berbulu")
Beruang.info_Karnifora()
print("=====================")
Harimau = Karnifora("Harimau", "Daging", "Darat", "Melahirkan", "Besar/kecil", "berbulu")
Harimau.info_Karnifora()