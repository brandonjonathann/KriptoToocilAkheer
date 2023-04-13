from RSA import *

p = generatePrima()
q = generatePrima()
n = p * q
totient = (p - 1) * (q - 1)
while True:
    e = generatePrima()
    if (totient % e != 0):
        break
d = cariD(totient, e)
m = "92dad9443e4dd6d70a7f11872101ebff87e21798e4fbb26fa4bf590eb440e71b"

print('')
print("p: " + str(p))
print('')
print("q: " + str(q))
print('')
print("n: " + str(n))
print('')
print("totient: " + str(totient))
print('')
print("e: " + str(e))
print('')
print("d: " + str(d))

print('')
print("ENKRIPSI")
print('')
c = enkripsi(m, e, n)
print("Hasil enkripsi: ")
print(c)

print('')
print("DEKRIPSI")
print('')
m = dekripsi (c, d, n)
print("Hasil dekripsi: ")
print(m)

kunciPublik = [e, n]
kunciPrivat = [d, n]

print(kunciPublik)
print(kunciPrivat)