while True:
 barang = int(input('\nMasukan jumlah barang : '))
 
 if int(barang) <= 10:
     print('Barang perlu direstok\n')
 else:
     print('Barang terjual\n')