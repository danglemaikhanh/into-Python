class Planet:
    name: str
    radius: int
    gravity: float
    system: str
    def __init__(self, name, radius, gravity, system):
        self.name = name
        self.radius = radius
        self.gravity = gravity
        self.system = system

    def __str__(self):
        return f'The Planet is: {self.name}, the radius = {self.radius}, gravity = {self.gravity} and the System is {self.system}'

planet1 = Planet('Saturn', 100, 3.3, 'Sun-System')
print(planet1)