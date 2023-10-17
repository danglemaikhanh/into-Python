from random import randint

ninja_words = [
    'Aiki', 'Buyu', 'Chimonjutsu', 'Cho sen', 'Dojo', 'Gakusei', 'Haiboku',
    'Jin', 'Kenshi', 'Obake ken', 'Rakusha', 'Sanmaru', 'Tekkon', 'Yoko'
]

paras =  int(input('How many paragraphs of lorem ipsum do you want? '))

def ninjas(word):
    random_pos = randint(0, len(ninja_words) -1)
    return f'{word} {ninja_words[random_pos]}'


with open('projects/ipsum_text.txt') as ipsum_original:
    items = ipsum_original.read().split()

    for n in range(paras):
        ninja_text = list(map(ninjas, items))
        with open('projects/ninja_ipsum.txt', 'a') as ipsum_ninja:
            ipsum_ninja.write(' '.join(ninja_text) + '\n\n')