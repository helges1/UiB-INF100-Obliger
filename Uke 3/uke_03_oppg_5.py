m_aar = float(input("Angi menneskeår: "))

if m_aar <= 2:
    print("Dette tilsvarer", (10.5 * m_aar), "hundeår.")
elif m_aar > 2:
    print("Dette tilsvarer", (21 + 4 * (m_aar - 2)), "hundeår.")
