# Buat class animal sebagai parent class, class animal mempunyai properti 4 properti (name, makanan, hidup, berkembang biak)

class Animal:
    def __init__(self,nama,makanan,hidup,berkembang_biak):
        self.nama = nama
        self.makanan = makanan
        self.hidup = hidup
        self.berkembang_biak = berkembang_biak
    def info_animal(self):
        print("nama hewan \t\t\t : ", self.nama,
              "\nMakanan \t\t\t : ", self. makanan,
              "\nHidup \t\t\t\t : ", self.hidup,
             "\nBerkembang Biak \t\t : " , self.berkembang_biak)

# hewan = Animal("kucing" , "ikan" , "udara" , "")melahirkan
# hewan.info_animal()
# buat minimal 3 class child (Amphibi,  Mamalia, Carnivora, dll) setiap class child itu memiliki 2 properti dan method  
# buat 3 objek dari masing masing class child. 


