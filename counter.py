### Original code by Quang Viet NGUYEN

def main():
    from collections import defaultdict
    # our alphabet with a dictionary to quickly search for its index
    alphabet = "abcdefghijklmnopqrstuvwxyz ,.!()"
    abc_index = {}

    for i, c in enumerate(alphabet):
        abc_index[c] = i

    print(abc_index)

    N = len(alphabet) # abc_index length
    P = 6 # key length

    with open("file.txt", "r") as f:
        ciphertext = f.read()

    # initialize frequency counter and group of texts
    counters = [defaultdict(int) for i in range(P)] # frequency counter
    texts = ['' for i in range(P)] #group of ciphertexts

    # analyze the original ciphertext
    for i, char in enumerate(ciphertext):        
        texts[i % P] = texts[i % P] + (char if char != ' ' else '_')
        counters[i % P][char] += 1
    
    for text in texts:
        print(text)

    for counter in counters:
        print(sorted(counter.items(), key=lambda item: item[1]))
    return




if __name__ == "__main__":
    main()