def planet_mass(gravity, radius):
    mass = (gravity * radius ** 2) / (6.67 * 10 ** -11)
    return mass

def planet_vol(radius):
    vol = (4/3) * 3.14 * radius ** 3
    return vol
