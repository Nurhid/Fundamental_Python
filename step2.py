"""
menghitung luas segitiga
"""
print('menghitung luas segitiga #1')
alas = 10
tinggi = 6
luas = alas * tinggi
print(f'segitiga dengan alas = {alas} dan tinggi = {tinggi} memiliki luas = {luas}')

print('\nmenghitung luas segitiga #2')
def hitung_luas(alas,tinggi): # def = deklarasi fungsi, dalam kurung itu atribut
    hitung_luas_segitiga = alas * tinggi / 2
    return hitung_luas_segitiga

print(hitung_luas(10,6))
print(type(hitung_luas))