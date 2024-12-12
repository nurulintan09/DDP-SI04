from animals import *

class ular(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, warna_ular, jenis_ular):
          super().__init__(nama, makanan, hidup, berkembang_biak)
          self.warna = warna_ular
          self.jenis = jenis_ular
        
    def cetak_ular(self):
         super().cetak()
         print(f'warna ular ini adalah {self.warna}, dan hewan ini jenisnya ular {self.jenis}')
         

print('----- cetak ular ------')
print('----- objek pertama ------')
boa = ular('ular boa', 'reptil', 'daerah berbatu', 'melahirkan', 'coklat', 'ular yang lambat')
boa.cetak_ular()

# objek kedua 
print('\n----- objek kedua -----')
kobra = ular('ular kobra', 'daging', 'padang rumput', 'bertelur', 'hitam', 'berbisa')
kobra.cetak_ular()

# objek ketiga 
print('\n----- objek ketiga -----')
sanca = ular('ular sanca', 'reptil', 'hutan', 'bertelur', 'cokelat dan hitam', 'tidak berbisa')
sanca.cetak_ular()

