def first_letter_last_word(filename):
    with open(filename, encoding="utf8") as f:
        fil = f.readlines()
        count = 0
        bokstaver = []

        while count < len(fil):
            words = fil[count].split()
            last = words[-1]
            bokstaver.append(last[0])
            count += 1
        
        return ''.join(bokstaver)

# print(first_letter_last_word("askeladden.txt",))