import hashlib

def hash(m):
    tmp = hashlib.new("sha3_256", m.encode())
    return tmp.hexdigest()