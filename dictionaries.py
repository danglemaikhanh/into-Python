# def ninja_intro(dict):
#     for key, val in dict.items():
#         print(f'I am {key} and I am a {val} belt')

def belt_count(dict):
    belts = list(dict.values())
    for belt in set(belts):
        num = belts.count(belt)
        print(f'There are {num} {belt} belts')

ninja_belts = {}

while True:
    ninja_name = input('Enter yout ninja name: ')
    ninja_belt = input('Enter your belt: ')
    ninja_belts[ninja_name] = ninja_belt

    another = input('add other? (y/n)')
    if another == 'y':
        continue
    else: 
        break

belt_count(ninja_belts)