stones = float(input("Vekt i stones: "))
pounds = float(input("Vekt i pounds: "))

kgst = float(stones / 0.15747)
kglb = float(pounds / 2.20462)

print("Vekt i kilogram:", kgst + kglb)
