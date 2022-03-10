### Original code by Quang Viet NGUYEN

def main():
    # our alphabet with a dictionary to quickly search for its index
    alphabet = "abcdefghijklmnopqrstuvwxyz ,.!()"
    abc_index = {}

    for i, c in enumerate(alphabet):
        abc_index[c] = i

    N = len(alphabet) # abc_index length

    with open("file.txt", "r") as f:
        ciphertext = f.read()
    print("Acceptable characters (case insensitive): " + alphabet)
    invalid = True
    while invalid:
        invalid = False
        print("Please enter the keyword: ")
        keys = input().lower()
        keys = list(keys)

        for i, key in enumerate(keys):
            if key not in alphabet:
                print("Invalid character found")
                invalid = True
                break
            keys[i] = abc_index[key]

    P = len(keys) # key length

    result = []
    for i, c in enumerate(ciphertext):
        b = keys[i % P]
        index = abc_index[c] - b
        index %= N

        result.append(alphabet[index])

    result = ''.join(result)
    
    print(result)

    return

if __name__ == "__main__":
    main()