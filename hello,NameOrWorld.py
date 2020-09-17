def hello(name=''):
        # Sets default argument to '' if none is given
    if name == '':
        print("Hello, World!");
    else:
        print("Hello,", name.capitalize() + "!")

hello()
