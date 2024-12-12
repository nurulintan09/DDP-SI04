from animals import *

class ikan(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, warna_ikan, jenis_ikan):
          super().__init__(nama, makanan, hidup, berkembang_biak)
          self.warna = warna_ikan
          self.jenis = jenis_ikan
    def cetak_ikan(self):
         super().cetak()
         print(f'warna ikan ini adalah {self.warna}, dan hewan ini jenisnya ikan {self.jenis}')
print('----- cetak ikan ------')
print('----- objek pertama ------')
nemo = ikan('ikan nemo', 'plankton', 'air', 'bertelur', 'orange', 'air laut')
nemo.cetak_ikan()

# objek kedua 
print('\n----- objek kedua -----')
guppy = ikan('ikan guppy', 'cacing/serangga kecil', 'air', 'bertelur', 'biru', 'air tawar')
guppy.cetak_ikan()

# objek ketiga
print('\n----- objek ketiga -----')
hiu = ikan('ikan hiu', 'ikan kecil, udang', 'air', 'bertelur', 'abu', 'air laut')
hiu.cetak_ikan()
