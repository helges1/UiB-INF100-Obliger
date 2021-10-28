def open_file(filename):

    with open(filename, encoding="utf8") as f:

        return "\n".join([f">>>{line.strip()}<<<" for line in f.readlines()])  

# print(open_file("askeladden.txt")) 