#Tugas 1
durasi_per_episode = 35 
jumlah_episode = 10

total_menit = durasi_per_episode * jumlah_episode
jam = total_menit // 60
menit = total_menit % 60

print("Total durasi nonton:", jam , menit ,"menit")
print("="*50)

#Tugas 2
ikan_cupang = 10000
ikan_koi = 20000
uang = 200000

beli = (ikan_cupang * 5) + (ikan_koi * 2)
sisa_uang = uang - beli
print("sisa uany nya adalah", sisa_uang)
print("="*50)

#Tugas 3
# Input data dari pengguna
jarak_perjalanan = float(input("Masukkan total jarak perjalanan (KM): "))
konsumsi_bbm = float(input("Masukkan konsumsi BBM sepeda motor (KM per Liter): "))
kapasitas_tangki = float(input("Masukkan kapasitas tangki sepeda motor (Liter): "))
harga_bensin = float(input("Masukkan harga bensin per liter (Rp): "))
diskon_minimal = float(input("Masukkan minimal bensin untuk diskon (Liter): "))
besar_diskon = float(input("Masukkan besar diskon per liter (Rp): "))

# Hitung total bensin yang dibutuhkan
total_bensin_dibutuhkan = jarak_perjalanan / konsumsi_bbm

# Hitung harga setelah diskon
harga_setelah_diskon = harga_bensin
if total_bensin_dibutuhkan > diskon_minimal:
    harga_setelah_diskon = harga_bensin - besar_diskon
    status_diskon = "Ya (Rp {:,}/L)".format(besar_diskon)
else:
    status_diskon = "Tidak"

# Hitung total biaya bensin
total_biaya_bensin = total_bensin_dibutuhkan * harga_setelah_diskon

# Hitung berapa kali harus mengisi bensin
jumlah_isi_bensin = total_bensin_dibutuhkan / kapasitas_tangki

# Output hasil
print("\n" + "="*50)
print("HASIL PERHITUNGAN BENSIN UNTUK PERJALANAN")
print("="*50)
print("Total jarak perjalanan:",jarak_perjalanan,"KM")
print("Konsumsi BBM:",konsumsi_bbm,"KM/L")
print("Kapasitas tangki:", kapasitas_tangki,"Liter")
print("Harga bensin normal: Rp", harga_bensin,"/L")
print("Minimal diskon:", diskon_minimal,"Liter")
print("Besar diskon: Rp", besar_diskon,"/L")
print("Mendapat diskon:",status_diskon)
print("-"*50)
print("Total bensin yang dibutuhkan:", total_bensin_dibutuhkan, "Liter")
print("Harga bensin setelah diskon: Rp", harga_setelah_diskon,"/L")
print("Total biaya bensin: Rp", total_biaya_bensin)
print("Perkiraan jumlah isi bensin:", jumlah_isi_bensin, "kali")
print("="*50)
