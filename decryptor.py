### Original code by Quang Viet NGUYEN

def main():
    # our alphabet with a dictionary to quickly search for its index
    alphabet = "abcdefghijklmnopqrstuvwxyz ,.!()"
    abc_index = {}

    for i, c in enumerate(alphabet):
        abc_index[c] = i

    N = len(alphabet) # abc_index length
    P = 6 # key length

    with open("file.txt", "r") as f:
        ciphertext = f.read()
    
    with open("result.txt", "w") as f:
        f.write(" ")
    
    # keyword is CRYPTO (2, 17, 24, 15, 19, 14)
    keys = [30, 15, 8, 17, 13, 18] 
    
    result = []
    for i, c in enumerate(ciphertext):
        b = keys[i % P]
        index = abc_index[c] + b
        index %= N

        result.append(alphabet[index])

    result = ''.join(result)
    
    print(result)

    return

if __name__ == "__main__":
    main()