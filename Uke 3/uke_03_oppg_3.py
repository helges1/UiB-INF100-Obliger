enhet = input("Angi enhet: ")

enhet_nm = "nm"
enhet_thz = "THz"

verdi = float(input("Verdi: "))

if enhet == enhet_nm and (verdi > 10**9):
    print("Dette er radiobølger")
elif enhet == enhet_nm and (verdi > 10**6 < 10**9):
    print("Dette er mikrobølger")
elif enhet == enhet_nm and (verdi > 740 < 10**6):
    print("Dette er infrarød stråling")
elif enhet == enhet_nm and (verdi > 380 < 740):
    print("Dette er synlig lys")
elif enhet == enhet_nm and (verdi > 10 < 380):
    print("Dette er ultrafiolett stråling")
elif enhet == enhet_nm and (verdi > 0.01 < 10):
    print("Dette er røntgenstråling")      
elif enhet == enhet_nm and (verdi < 0.01):
    print("Dette er gammastråling")  
 
elif enhet == enhet_thz and (verdi < 3*10**-4):
    print("Dette er radiobølger")
elif enhet == enhet_thz and (verdi > 3*10**-4 < 0.3):
    print("Dette er mikrobølger")
elif enhet == enhet_thz and (verdi > 0.3 < 405):
    print("Dette er infrarød stråling")
elif enhet == enhet_thz and (verdi > 405 < 790):
    print("Dette er synlig lys")
elif enhet == enhet_thz and (verdi > 790 < 3*10**4):
    print("Dette er ultrafiolett stråling")
elif enhet == enhet_thz and (verdi > 3*10**4 < 3*10**7):
    print("Dette er røntgenstråling") 
elif enhet == enhet_thz and (verdi > 3*10**7):
    print("Dette er røntgenstråling") 

else:
    print("Du har tastet feil enhet. Dette må enten være [nm] eller [THz]")