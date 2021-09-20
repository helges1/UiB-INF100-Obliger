def hyd_press(p, g, z):
    p = p * z**-3
    g = g * 10**-2
    z = z
    pa = p * g * z
    dbar = pa*10**4
    return dbar