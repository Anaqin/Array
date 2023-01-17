# menghitung angka
angka = int(input("masukan angka: "))

# jika habis dibagi nol, maka genap
if(angka % 2) == 0:
    print("{0} adakah bilangan genap".format(angka))

# jika tidak habis di bagi nol,maka ganjil
else:
    print("{0} adalah bilangan ganji".format(angka))