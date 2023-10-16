from classes import Planet

planet1 = Planet('Saturn', 100, 3.3, 'Sun-System')
print(planet1)
print(planet1.shape)
# instance method
print(Planet.commons())
print(Planet.spin('a very high speed'))