# SHA3-224: Output d = 224, Rate r = 1152, Capacity c = 448
# SHA3-256: Output d = 256, Rate r = 1088, Capacity c = 512
# SHA3-384: Output d = 384, Rate r = 832, Capacity c = 768
# SHA3-512: Output d = 512, Rate r = 576, Capacity c = 1024

def stringToBinary(n):
    p = [bin(ord(i))[2:].zfill(8) for i in n]
    return p

def binaryXORFunction(x, y):
    tmp = []
    for i in range(len(x)):
        if(x[i] == y[i]):
            tmp.append(str(0))
        else:
            tmp.append(str(1))
    result = ''.join(tmp)
    return result

n = "The quick brown fox jumps over the lazy dog"
p = stringToBinary(n)

r = int(1152 / 8)
block = 1
diff = 0

if (r > len(p)):
    diff = int(r - len(p))
else:
    block = int(len(p) // r)
    diff = int(r - (len(p) % r))

if (diff != 0):
    if (diff == 1):
        p.append('10000001')
    else:
        p.append('10000000')
        for i in range(int(r - len(p) - 1)):
            p.append('00000000')
        p.append('00000001')

pBreak = []
for i in range(block):
    tmp = []
    for j in range(r):
        tmp.append(p[i * r + j])
    pBreak.append(tmp)

s = []
for i in range(5):
    tmp = []
    for j in range(5):
        for k in range(8):
            tmp.append('11111111')
    s.append(tmp)

for i in range(len(pBreak)):
    for j in range(int(448 / 8)):
        pBreak[i].append('00000000')
    tmp = []
    for j in range(len(pBreak[i])):
        tmp.append(binaryXORFunction(pBreak[i][j], s[j // 40][j % 40]))
    