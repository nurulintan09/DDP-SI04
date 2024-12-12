from animals import *

class burung(Animal):
     def __init__(self, nama, makanan, hidup, berkembang_biak, warna_bulu, bunyi):
          super().__init__(nama, makanan, hidup, berkembang_biak)
          self.warna_bulu = warna_bulu
          self.bunyi = bunyi

     def cetak_burung(self):
        super().cetak()
        print(f'hewan ini berbulu {self.warna_bulu}, dan hewan ini berbunyi {self.bunyi}')
print('----- cetak burung ------')
print('----- objek pertama ------')
beo = burung('burung beo', 'biji-bijian', 'udara', 'bertelur', 'blue and orange', 'kamu cantik')
beo.cetak_burung()

# objek kedua 
print('\n----- objek kedua -----')
merpati = burung('burung merpati', 'biji-bijian', 'udara', 'bertelur', 'putih', 'assalamualaikum')
merpati.cetak_burung()

# objek ketiga
print('\n----- objek ketiga -----')
kenari = burung('burung kenari', 'biji-bijian', 'udara', 'bertelur', 'biru', 'Kicauan melodius yang lembut dan variatif.')
kenari.cetak_burung()