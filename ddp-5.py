# jawaban no 1
kendaraan = ["scoopy", "Sepeda motor", 120, "Hitam", 2]
print("kendaraan saya adalah")
print(kendaraan)
print("==================")
# tambahkan dari list tersebut dibelakang dengan value : [harga kendaraan, tipe kendaraan]
kendaraan.append (110000000)
kendaraan.append ("metic")
print(kendaraan)
# tambahkan setelah jenis kendaraan dengan value [merk kendaraan]
kendaraan.insert (2, "scoopy")
print(kendaraan)
print("=======================")

# jawaban no 2
pilih = int(input("""selamat datang diaplikasi menghitung
1. untuk menghitung luas persegi
2. untuk menghitung luas lingkaran
3. untuk menghitung luas segitiga

masukan pilihan anda: \n"""))

match pilih:
    case 1 :
        print("kamu memilih 1 untuk menghitung luas persegi")
        sisi = int(input("masukan sisi persegi: "))
        luaspersegi = sisi*sisi
        print("luas persegi yang sisinya",sisi, "adalah", luaspersegi)
    case 2 :
        print("kamu memilih 2 untuk menghitung lingkaran")
        jari2 = int(input("masukan jari-jari: "))
        luaslingkaran = 3.14 * jari2 * jari2
        print("luas lingkaran yang jari-jarinya",jari2, "adalah", luaslingkaran)
    case 3 :
        print("kamu memilih 3 untuk menghitung segitiga")
        alas = int(input("masukan alas segitiga: "))
        tinggi = int(input("masukan tinggi segitiga"))
        luassegitiga = 0.5 * alas * tinggi
        print("luas segitiga dengan alas",alas, "dan tinggi", tinggi, "adalah", luassegitiga)
    case _:
        print("Anda salah pilih")
