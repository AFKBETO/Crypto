p = 7207 ######################
g = 4177 ######################

def main():
    dA, dB = 14, 0 ######################

    eA = (g ** dA) % p
    eB = (g ** dB) % p
    eB = 3090 ######################

    print(f"eA, eB = {eA}, {eB}")
    print(f"dA, dB = {dA}, {dB}")

    sA = 4139 ######################
    k = 4414 ######################
    
    rA, yAB = encrypt(eB, sA, k)

    print(f"Ciphered text (rA, yAB) = ({rA}, {yAB})")

    r, y = 2523, 4346 ######################
    res = decrypt(r, y, dA)
    print(f"Deciphered text r = {res}")
    
def encrypt(eB, sA, k):
    rA = (g ** k) % p
    yAB = (sA * eB ** k) % p
    return (rA, yAB)

def decrypt(rA, yAB, dB):
    r = (rA ** dB) % p
    s = (yAB * inverse(r, p)) % p
    return s

def euclid(a, b):
    u1, v1 = 1, 0
    u2, v2 = 0, 1
    if (a < b): a, b = b, a

    while (a % b):
        q = a // b
        u1, u2 = u2, u1 - u2 * q
        v1, v2 = v2, v1 - v2 * q
        a, b = b, a % b
    
    return u2, v2

def inverse(k, n):
    _, res = euclid(k, n)
    return res


if __name__ == "__main__":
    main()