def add_together_safely(a, b, c, d):

        try:
            return a + b + c + d
        except TypeError as e:
            print(f"Failed with error: {e}")

print(add_together_safely(1, 2, "b", "c"))