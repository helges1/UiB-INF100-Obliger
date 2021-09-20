def hyd_pres(p, g, z):
    p = p * 100 **-3
    g = g * 10**-2
    z = z

    pa = p * g * z
    dbar = round(pa*10**4, 2)

    return dbar