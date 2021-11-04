print('Option 1')
import eks_1_lib #import module

fib_1 = eks_1_lib.fib(100)
col_1 = eks_1_lib.collatz(17)
print(fib_1)
print(col_1)

#################################

print('Option 2')
import eks_1_lib as el

print(el.collatz(5))
c = el.C_LIGHT
print(c,'m/s')

#############################

print('Option 3')
from eks_1_lib import fib

fib_2 = fib(75)
print(fib_2)

##############################

print('Option 4')
from eks_1_lib import H_PLANCK as h, C_LIGHT as c, fib
print(c)
print(h)
print(fib(30))
