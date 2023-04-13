import random

# Menginisialisasi sebuah array berisi bilangan-bilangan prima pertama untuk kebutuhan Rabin Miller Primality Test
primaDibawah1000 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 
                    43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 
                    101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 
                    151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 
                    199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 
                    263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 
                    317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 
                    383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 
                    443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 
                    503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 
                    577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 
                    641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 
                    701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 
                    769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 
                    839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 
                    911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 
                    983, 991, 997]

# Men-generate sebuah bilangan berukuran 512 bit
def randomPrimeCandidate():
    while True:
        # -1 digunakan untuk mencegah bilangan yang di-generate merupakan bilangan berukuran 513 bit
        tmp = random.randrange(pow(2, 511), pow(2, 512) - 1)
        if (tmp % 2 != 0):
            return tmp

# Melakukan Low Level Primality Test (pengecekan dengan bilangan-bilangan prima pertama)
def lowLevelPrime():
    while True:
        x = randomPrimeCandidate()
        factor = False
        for i in primaDibawah1000:
            if (x % i == 0):
                factor = True
            elif (x <= i):
                factor = True
        if not(factor):
            return x 

# Melakukan High Level Primality Test (pengecekan dengan Rabin Miller Primality Test sebanyak 20 kali iterasi)
def isMillerRabinPassed(miller_rabin_candidate):
   
    maxDivisionsByTwo = 0
    evenComponent = miller_rabin_candidate-1
   
    while evenComponent % 2 == 0:
        evenComponent >>= 1
        maxDivisionsByTwo += 1
    assert(2**maxDivisionsByTwo * evenComponent == miller_rabin_candidate-1)
   
    def trialComposite(round_tester):
        if pow(round_tester, evenComponent, miller_rabin_candidate) == 1:
            return False
        for i in range(maxDivisionsByTwo):
            if pow(round_tester, 2**i * evenComponent, miller_rabin_candidate) == miller_rabin_candidate-1:
                return False
        return True
   
    for i in range(20): 
        round_tester = random.randrange(2, miller_rabin_candidate)
        if trialComposite(round_tester):
            return False
    return True

# Menghasilkan sebuah bilangan prima berukuran 512 bit
def generatePrima():
    while True:
        x = lowLevelPrime()
        if isMillerRabinPassed(x):
            return x

# Mencari d berdasarkan nilai e dan totient
def cariD(totient, e):
    return pow(e, -1, totient)

# Proses enkripsi
def enkripsi(m, e, n):

    # Mengubah m yang merupakan hasil hashing SHA3-256 berupa hexadecimal menjadi decimal
    m = int(m, 16)

    # Mengenkripsi message dalam bentuk decimal menjadi ciphertext
    c = pow(m, e, n)

    # Menghasilkan ciphertext dalam bentuk hexadecimal seperti pada contoh
    c = hex(c)

    return c

# Proses dekripsi
def dekripsi(c, d, n):
    
    # Mengubah ciphertext dari bentuk hexadecimal menjadi decimal
    c = int(c, 16)
    
    # Mendekripsi ciphertext menjadi decimal
    m = pow(c, d, n)

    # Mengubah decimal menjadi bentuk hexadecimal
    m = hex(m)

    return m
