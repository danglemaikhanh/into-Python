def greet(name="dude", time="morning"):
    print(f'Good {time}, {name}!')

 #name = input('Enter your name: ')
 #time = input('Enter the time of day: ')
greet()

def area(r):
    return 3.142 * r*r

def vol(area, length):
    print(area * length)

radius = int(input('Enter a radius: '))
length = int(input('Enter the length: '))

vol(area(radius), length)