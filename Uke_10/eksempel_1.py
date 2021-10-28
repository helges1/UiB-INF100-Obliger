# 3 ways of getting information from a file

with open("timemachine.txt", encoding="utf8") as f:
    for line in f:
        line = line.strip()  # removes spaces before and after string
        l = len(line)
        print("The line is", l, "long, and ends with")
        print(">>>", line[-20:], "<<<")

# ========

with open("timemachine.txt", encoding="utf8") as f:
    all_lines = f.readlines()

print(len(all_lines), "lines in the text")

# ==========

with open("timemachine.txt", encoding="utf8") as f:
    all_lines = f.read()

print("vvvvvvv")
print(all_lines)
print("^^^^^^^")

# ========

with open("numbers.txt", "w", encoding="utf8") as f:
    for i in range(100):
        f.write(f"{i} is a nice number")


# now open the file numbers.txt in your editor and see what's inside

# we can also use .writelines() to write to the file
with open("numbers2.txt", "w", encoding="utf8") as f:
    lines = [f"{i} is a nice number\n" for i in range(100)]
    f.writelines(lines)


# open the file numbers2.txt in your editor and see what's inside

# write other files!
