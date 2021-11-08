import matplotlib.pyplot as plt
from math import sin

# liste med x-verdier
xs = [n / 10 for n in range(101)]
# 2 ulike lister med y-verdier
ys_1 = [sin(x) for x in xs]
ys_2 = [3 * sin(x) for x in xs]

plt.plot(xs, ys_1, "-.r")
plt.plot(xs, ys_2, "--b")

# Første interseksjonen
plt.annotate("", xy=(3.20, 0), xytext=(xs[3], ys_1[3]), arrowprops=dict(arrowstyle="->"))
plt.text(xs[0], ys_1[-1], "Første interseksjonen")



# savefig lagrer filene
plt.savefig("uke_12_oppg_3.png")


# interaktivt vindu
plt.show()
