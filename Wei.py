# KONSTRUKSI SEQUENTIAL = eksekusi berurutan
"""
ini adalah note
"""
print('Nurul Hidayati')
print('kayak gitu')

# Percabangan
print('\nPERCABANGAN')
nurul_ingin_cepat = False
if nurul_ingin_cepat:
    print('ya jalan lurus ajah dong')
else:
    print('kalau gamau cepat, belok kanan kiri saja')

# PERULANGAN / looping
print('-'*50)
print('PERULANGAN')
jumlah_anak_nurul = 4
# print('hai anak ke #1')
# print('hai anak ke #2')
# print('hai anak ke #3')
# print('hai anak ke #4')

for a in range (1, jumlah_anak_nurul+1): # 4 - 1 = 3
    print(f'halo anak #{a}')
# pemanggilan dengan inisialisasi sementara agar di panggil berurutan

# list / array / daftar
print("\nlist") # \n itu newline / enter, hanya bisa digunakan di dalam kalimat dengan petik 1 ' / petik 2 "
# anak1 = 'topek'
# anak2 = 'nurul'
# anak3 = 'lukman'

# print(anak1)
# print(anak2)
# print(anak3)

anak = ['topek', 'nurul', 'lukman']  # tipe data list diawali dengan kurung siku
print(f'hai anak ku {anak[2]}') # pemanggilan data tertentu dari list, menggunakan index sesuai urutan
# di mulai dari 0

nilai_nurul = 99.9

# kurung kurawal = {} tipe data dictioanry
print(type(anak)) # kurung siku = [] itu tipe data list
print(type(jumlah_anak_nurul)) # int / integer tipe data yg mengandung nilai bil bulat
print(type(nilai_nurul)) # float / tipe data decimal
print(type(nurul_ingin_cepat)) # tipe data bool / bernilai 2 = True or False