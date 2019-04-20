"""
this is comment paragraph
"""
from geometri.segitiga import luas
from geometri.persegi_panjang import luas_pp
from geometri_class.segitiga import Segitiga

print(1 + 1)
print('test hello')

alas = 10
tinggi = 5
luas_segitiga = 1/2*alas*tinggi

if luas_segitiga < 25:
    print ('kecil')
elif luas_segitiga == 25:
    print ('pas')
else:
    print ('gede ya')

for i in range (0,10):
    print (i, i*luas_segitiga)



print(luas('luas segitiga :', 3,6))

'''Pembuatan module: PACKAGE'''

print (luas_pp('luas persegi panjang:', 5, 6))

'''Pembuatan module: class'''

luas1 = Segitiga('Luasnya: ', 5, 6)
print (luas1.title, luas1.luas_segitiga())


