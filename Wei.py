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


"""
Dictionary / kamus
KVP
key value pair
"""

kamus_ind_eng = {'anak': 'child', 'child': 'anak', 'ayah': 'father'}

print(kamus_ind_eng['ayah'])
print(kamus_ind_eng['child'])

data_dari_server_gojek = { #data_dari_server_gojek itu variable, kurung kurawal awalan dictionary
    'tanggal' : '31 juli 2021', # tanggal dan driver list itu key
    'driver_list' : [
        {'nama' : 'nurul', 'jarak' : 10},
        {'nama' : 'nad', 'jarak' : 5},
        {'nama' : 'lola', 'jarak' : 15},] # nurul nad lola itu value
}

print(data_dari_server_gojek['tanggal']) # pemanggilan variable tanpa tanda petik di dalam print
print(data_dari_server_gojek['driver_list']) # pemanggilan data di dalam dictionary menggunakan tanda petik
# print(data_dari_server_gojek['driver_list'][0]['nurul']) # kurung siku digunakan untuk memanggil value tertentu, dimulai dari 0
# print(data_dari_server_gojek['driver_list'][2]['lola'])
print(data_dari_server_gojek['driver_list'][2]['jarak'])

print(f"ini data driver tanggal {data_dari_server_gojek['tanggal']} dan  ")
print(f"nama best driver adalah {data_dari_server_gojek['driver_list'][2]['nama']}")