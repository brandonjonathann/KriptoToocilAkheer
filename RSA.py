# Cek bilangan prima atau tidak
def isPrima(x):
    prima = True
    if ((x <= 1) ):
        prima = False
    elif (x != 2):
        for i in range (x - 2):
            if (x % (i + 2) == 0):
                prima = False
                break
    return prima

# Cek bilangan faktor atau bukan
def isFaktor(totient, e):
    if (totient % e == 0):
        return True
    else:
        return False

# Cari d yang bulat berdasarkan k
def cariD(totient, e):
    k = 1
    found = False
    while not(found):
        d = (1 + (k * totient)) / e
        if (d % 1 == 0):
            d = int(d)
            return d
        else:
            k += 1

# Dibikin tidak sama dengan Slides Pak Rin karena spasi dihilangkan
# Spasi dianggap sebagai "00" dan A sebagai "01", begitu pula seterusnya
# Dengan begitu, pesan dengan jumlah karakter yang ganjil
# Dapat disisipkan spasi untuk menggenapkan pesan agar pembagian blok
# menjadi lebih masuk akal

# Proses enkripsi
def enkripsi(m, e, n):

    # Plaintext diubah menjadi array of integer yang merupakan urutan
    # ASCII masing-masing karakter
    mList = [(ord(i) - 64) for i in m]

    # Spasi diubah menjadi "00" untuk memperlancar proses enkripsi
    for i in range (len(mList)):
        if (mList[i] == -32):
            mList[i] = 0

    # Dilakukan penambahan spasi jika jumlah karakter tidak bulat
    if (len(mList) % 2 != 0):
        mList.append(0)

    # Melakukan pengelompokkan menjadi blok-blok dengan ukuran yang sama
    mBlock = []
    for i in range (int(len(mList) / 2)):
        mBlock.append((mList[2 * i] * 100) + (mList[2 * i + 1]))

    # Blok-blok dienkripsi menjadi blok-blok ciphertext
    cList = []
    for i in range (len(mBlock)):
        tmp = (mBlock[i] ** e) % n
        cList.append(tmp)
    return cList

# Proses dekripsi
def dekripsi(cList, d, n):
    
    # Blok-blok ciphertext didekripsi menjadi blok-blok integer
    mBlock = []
    for i in range (len(cList)):
        # Digunakan metode seperti ini, bukan m = c ** d % n
        # Karena ukuran bilangan terlalu besar pada python
        # Sehingga harus disederhanakan
        tmp = cList[i]
        for j in range (int(d) - 1):
            tmp = tmp * cList[i]
        tmp = tmp % n
        mBlock.append(tmp)

    # Blok-blok integer dipecah ke bentuk semula
    mList = []
    for i in range(len(mBlock)):
        tmp = mBlock[i] // 100
        mList.append(tmp)
        mList.append(mBlock[i] - (tmp * 100))

    # Urutan karakter dikembalikan ke urutan ASCII awalnya
    # Begitu pula dengan spasi yang dijadikan sebagai "00",
    # Dikembalikan ke nilai semulanya
    for i in range (len(mList)):
        if (mList[i] == 0):
            mList[i] = -32
        mList[i] += 64
    
    # Melakukan pengecekan elemen terakhir,
    # Bila elemen terakhir berupa spasi, elemen tersebut dibuang
    if (mList[len(mList) - 1] == 32):
        mList.pop

    # Melakukan pengubahan urutan angka menjadi karakter semula
    tmp = []
    for i in range (len(mList)):
        tmp.append(chr(mList[i]))

    # Array of char digabungkan menjadi pesan yang telah didekripsi
    m = ''.join(tmp)
    return m
