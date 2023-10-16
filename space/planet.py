class Planet:
    name: str
    radius: int
    gravity: float
    system: str
    # Class Attribute
    shape = 'round'
    def __init__(self, name, radius, gravity, system):
        # instance attributes
        self.name = name
        self.radius = radius
        self.gravity = gravity
        self.system = system

    def __str__(self):
        return f'The Planet is: {self.name}, the radius = {self.radius}, gravity = {self.gravity} and the System is {self.system}'
    # Class Method
    @classmethod
    def commons(cls):
        return f'All planets are {cls.shape} because of gravity'
    # Static Method
    @staticmethod
    def spin(speed = '2000 miles per hours'):
        return f'The planet spins and spins a {speed}'