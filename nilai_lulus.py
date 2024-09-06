while True:
 ipas = int(input('\nMasukan nilai ipas : '))
 bahasa_indonesia = int(input('Masukan nilai bahasa indonesia : '))
 bahasa_inggris = int(input('Masukan nilai bahasa inggiris : '))
 matematika = int(input('Masukan nilai matematika : '))
 total = ipas + bahasa_indonesia + bahasa_inggris + matematika

 if total >= 200:
     print('Lulus\n')
 else:
     print('tidak lulus\n')