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

# Mencari d yang bulat berdasarkan k
def cariD(totient, e):
    k = 1
    found = False
    while not(found):
        d = (1 + (k * totient)) / e
        if (d % 1 == 0):
            print(d % 1)
            print(d)
            d = int(d)
            return d
        else:
            k += 1

# Proses enkripsi
def enkripsi(m, e, n):

    # Plaintext diubah menjadi array of integer yang merupakan urutan
    # ASCII masing-masing karakter
    mList = [ord(i) for i in m]
    print(mList)

    # # Dilakukan penambahan spasi jika jumlah karakter tidak bulat
    # if (len(mList) % 2 != 0):
    #     mList.append(32)
    # print(mList)

    # Melakukan pengelompokkan menjadi blok-blok dengan ukuran yang sama
    mBlock = []
    for i in range (int(len(mList) / 2)):
        mBlock.append((mList[2 * i] * 1000) + (mList[2 * i + 1]))
    print(mBlock)

    # Blok-blok dienkripsi menjadi blok-blok ciphertext
    c = []
    for i in range (len(mBlock)):
        c.append(pow(mBlock[i], e, n))
    print(c)
    return c

# Proses dekripsi
def dekripsi(c, d, n):
    
    # Blok-blok ciphertext didekripsi menjadi blok-blok integer
    print(c)
    mBlock = []
    for i in range (len(c)):
        mBlock.append(pow(c[i], d, n))
    print(mBlock)

    # Blok-blok integer dipecah ke bentuk semula
    mList = []
    for i in range(len(mBlock)):
        tmp = mBlock[i] // 1000
        mList.append(tmp)
        mList.append(mBlock[i] - (tmp * 1000))
    print(mList)
    
    # Melakukan pengecekan elemen terakhir,
    # Bila elemen terakhir berupa spasi, elemen tersebut dibuang
    print(mList[len(mList) - 1])
    if (mList[len(mList) - 1] == 32):
        mList.pop()
    print(mList)

    # Melakukan pengubahan urutan angka menjadi karakter semula
    tmp = []
    for i in range (len(mList)):
        tmp.append(chr(mList[i]))
    print(tmp)

    # Array of char digabungkan menjadi pesan yang telah didekripsi
    m = ''.join(tmp)
    print(m)
    return m
