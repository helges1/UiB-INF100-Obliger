y_dict = {
  0 : 0,
  1 : "vafler",
  "two" : 2,
  5 : 4
}

my_list = [0, 1, "boller", 4]


print("Dictionary Keys:")
for key, value in y_dict.items() :
    print (key)
print()

print("Dictionary Values:")
for key, value in y_dict.items() :
    print (value)
print()

print("Dictionary keys/value:")
for key, value in y_dict.items() :
    print (key, value)
print()

print("List values:")
print(*my_list, sep = "\n")
print()

print ("List indices/value: ")
for i in range(len(my_list)):
    print (i, end = " ")
    print (my_list[i])