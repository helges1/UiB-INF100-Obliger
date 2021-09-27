høyde = float(input("Stenen droppes fra høyde: "))
tid = 0
nåværende_høyde = høyde

while nåværende_høyde >= 0:
    nåværende_høyde = høyde - 0.5 * 9.8 * tid**2
    
    if nåværende_høyde > 0:
        print(round(nåværende_høyde, 1),"m")
        tid += 1
    else: 
        break
    
print(0, "m")   
print("Stenen lander mellom", tid - 1, "og", tid, "sekunder etter at den droppes.")