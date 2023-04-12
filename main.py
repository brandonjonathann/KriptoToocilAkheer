from RSA import *

print("")
print("---")
print("") 

p = generatePrima()
q = generatePrima()

print("p yang didapatkan: " + str(p))
    
print("")
print("---")
print("") 

print("q yang didapatkan: " + str(q))
    
print("")
print("---")
print("") 

n = p * q
print("n yang didapatkan: " + str(n))
print(len([i for i in str(n)]))

print("")
print("---")
print("") 

totient = (p - 1) * (q - 1)
print("totient yang didapatkan: " + str(totient))

while True:

    print("")
    print("---")
    print("") 

    e = generatePrima()

    if (totient % e != 0):
        break

print("e yang didapatkan: " + str(e))

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

for i in cList:
    if (n > i):
        print("Safe")

print("DEKRIPSI")
m = dekripsi (cList, d, n)
print("Hasil dekripsi: " + str(m))

print("")
print("---")
print("")

print(pow(253, 1019, 3337))
print(pow(1619, 1019, 3337))
print(pow(3096, 1019, 3337))
print(pow(165, 1019, 3337))
print(pow(26, 1019, 3337))
print(pow(442, 1019, 3337))
print('')
print(pow(792, 1019, 3337))
print(pow(772, 1019, 3337))
print(pow(705, 1019, 3337))
print(pow(299, 1019, 3337))
print(pow(46, 1019, 3337))
print(pow(1600, 1019, 3337))