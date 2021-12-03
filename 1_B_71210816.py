angka = int(input("masukkan angka : "))
hasil = 0
for k in range (1,angka+1):
    print (k, end=" ")
    if (k == angka):
        print ("=", end=" ")
    else :
        print ("+", end = " ")
    hasil = hasil + k
print(hasil)