from RSA import *

valid = False
while not(valid):

    print("")
    print("---")
    print("") 

    p = int(input("Masukkan nilai p (bilangan prima): "))
    q = int(input("Masukkan nilai q (bilangan prima): "))
    
    if (isPrima(p) and isPrima(q)):
        valid = True
    else:
        print("p dan q harus merupakan bilangan prima")
    
print("")
print("---")
print("") 

n = p * q
print("n yang didapatkan: " + str(n))

totient = (p - 1) * (q - 1)
print("totient yang didapatkan: " + str(totient))

valid = False
while not(valid):

    print("")
    print("---")
    print("") 

    e = int(input("Masukkan nilai e (bilangan relatif prima dari totient): "))

    if (not(isFaktor(totient, e))):
        valid = True
    else:
        print("e harus relatif prima terhadap totient")

print("")
print("---")
print("")

m = input("Masukkan pesan yang ingin dienkripsi: ")

print("")
print("---")
print("")

d = cariD(totient, e)
print("d yang didapatkan: " + str(d))

print("")
print("---")
print("")

print("ENKRIPSI")
cList = enkripsi(m, e, n)
print("Ciphertext: " + str(cList))

print("")
print("---")
print("")

print("DEKRIPSI")
m = dekripsi (cList, d, n)
print("Hasil dekripsi: " + str(m))

print("")
print("---")
print("")