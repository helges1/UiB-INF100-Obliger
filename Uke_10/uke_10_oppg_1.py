def open_file(filename):
    
    with open(filename, encoding="utf8") as f:

        return f.read()

# print(open_file("askeladden.txt"))