nilai = int(input('Masukkan Angka : '))
 
hasil = None
if nilai <= 100 and nilai >= 80:
    hasil = 'A'
elif nilai <= 79 and nilai >= 70:
    hasil = 'B'
elif nilai <= 69 and nilai >= 60:
    hasil = 'C'
elif nilai <= 59 and nilai >= 50:
    hasil = 'D'
elif nilai <=49 and nilai >= 0:
    hasil = 'E'
else:
    print('inputan salah')
 
print('Nilai {} =  {}'.format(nilai, hasil))
