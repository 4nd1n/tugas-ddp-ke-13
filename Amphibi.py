from Animal import Animal

# setiap class hild itu memiliki 2 properti dan method
class Amphibi(Animal):
    def __init__(self , name, makanan, hidup, berkembang_biak, jenis_air, bernapas ):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.jenis_air = jenis_air
        self.bernapas = bernapas

    def info_amphibi(self):
        super().info_animal(),
        print("jenis Air \t\t\t : ", self.jenis_air,
              "\nBernapas \t\t\t :,", self.bernapas) 

Amphibi = Amphibi("katak", "Serangga", "Dua alam", "Bertelur", "Air tawar", "Kulit dan paru-paru")
Amphibi.info_amphibi()      


