while True:
 nilai = input('\nMasukan Nilai Siswa : \n')

 if int(nilai) >= 80:
    print('Nilai A\n')
 elif int(nilai) >= 70:
    print('Nilai B\n')
 elif int(nilai) >= 60:
    print('Nilai C\n')
 elif int(nilai) >= 50:
    print('Nilai D\n')
 else:
    print('Nilai E\n')