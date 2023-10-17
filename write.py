with open('files/write.txt', 'w') as write_file:
    write_file.write('Hey there, this is a test\n')
    write_file.write('This is another line, I am writing to a file\n')

with open('files/write.txt', 'a') as write_file:
    write_file.write('This is a new line, I am writing to a file\n')

quotes = [
    '\nI can resist everything except temptation.',
    '\nWe are all in the gutter, but some of us are looking at the stars.',
    '\nAlways forgive your enemies; nothing annoys them so much.'
]

with open('files/write.txt', 'a') as write_file:
    write_file.writelines(quotes)