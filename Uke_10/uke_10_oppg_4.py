def first_letter_last_word(filename):
    with open(filename, encoding="utf8") as f:
        x = f.readlines()
        x = x[0]
        return(x[::-1])

     
print(first_letter_last_word("askeladden.txt",))