#global variable
my_name = 'ryu'

def print_name():
    global my_name
    #local variable
    my_name = 'yoshi'
    print('the name inside the function is', my_name)

print_name()
print('the name outside the function is', my_name)