from space.planet import Planet
from space.calc import planet_mass, planet_vol

planet1 = Planet('Saturn', 100, 3.3, 'Sun-System')
print(planet1)
print(planet_mass(planet1.gravity, planet1.radius))
print(planet_vol(planet1.radius))