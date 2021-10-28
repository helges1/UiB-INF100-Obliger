xs = ["a", "b", "c"]

# print(xs[5]) # fails with IndexError

# Option 1 - catch everything

try:
    x1 = xs[2]
    x2 = xs[5]
    print(x2 - x1)
except Exception:
    print("Something went wrong")
    print("Decide what to do next here")
    # ...


# Option 2 - catch specific

try:
    x1 = xs[2]
    x2 = xs[5]  # broken
    print(x2 - x1)
except IndexError as err:
    print("We caught an IndexError:", err)

# Option 3 - TypeError still goes out

try:
    x1 = xs[2]
    x2 = xs[0]
    print(x2 - x1)  # broken
except IndexError as err:
    print("We caught an IndexError:", err)

# get TypeError in Terminal


# Option 4 - both caught

try:
    x1 = xs[2]
    x2 = xs[0]
    print(x2 - x1)  # broken

except IndexError as err:
    print("We caught an IndexError:", err)

except TypeError as err:
    print("We caught a TypeError:", err)
