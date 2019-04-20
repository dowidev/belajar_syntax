"""
this is comment paragraph
"""
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

def luas (detail, alas, tinggi):
    print (detail)
    return alas*tinggi/2

print(luas('luas adalah', 3,6))