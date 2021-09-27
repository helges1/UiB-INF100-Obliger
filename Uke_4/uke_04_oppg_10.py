sekund = 0
grader = 25.0

while grader < 100:
    print (f"{sekund}s = {grader:.1f}°C")
    grader += 0.625
    if grader >= 100:
        print(f"{grader:.1f}°C i {sekund} sekunder")
    sekund += 1

