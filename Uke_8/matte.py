x = float(input("X0 value: "))
v = (float(input("Iterations: ")))
val=1
print(f"X{val} = {x}")

while v > 1:
    y = x - ((((1)/(x**2  + 1))-x)/(((-2*x)/(x**2+1)**2)-1))
    x=y
    val+=1
    v-=1
    print(f"X{val} = {y}")