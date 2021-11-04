# Vi kan definere funksjoner...

def fib(n):
    """Return the fibonacci sequence up to n as a list"""
    a, b = 0, 1
    seq = []
    while a < n:
        seq.append(a)
        a, b = b, a+b
    return seq

        
def collatz(n):
    """Return the collatz sequence from n as a list"""
    def collatz_step(n):
        if n % 2 == 0:
            return n//2
        else:
            return 3*n + 1
    seq = [n]
    while n > 1:
        n = collatz_step(n)
        seq.append(n)
    return seq

# ...eller verdier i en bibliotek

# speed of light [m/s]
C_LIGHT = 299792458

# Planck constant [Js]
H_PLANCK = 6.62607015e-34
