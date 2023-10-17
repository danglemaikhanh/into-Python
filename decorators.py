def cough_dec(func):
    def func_wrapper():
        # code before function
        print('*cough*')
        func()
        # code after function
        print('*cough*')
    return func_wrapper

@cough_dec
def question():
    print("can you hear me?")

@cough_dec
def answer():
    print("yes! I can hear you!")
    
question()
answer()