import matplotlib.pyplot as plt
from math import sin

# liste med x-verdier
xs = [n / 10 for n in range(101)]
# 2 ulike lister med y-verdier
ys_1 = [sin(x) for x in xs]
ys_2 = [3 * sin(x) for x in xs]

plt.plot(xs, ys_1, "-.r")
plt.plot(xs, ys_2, "--b")

# Legge undermerker til x og y-aksen.
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.minorticks_on.html
plt.minorticks_on()


# savefig lagrer filene
plt.savefig("uke_12_oppg_2.png")


# interaktivt vindu
plt.show()
