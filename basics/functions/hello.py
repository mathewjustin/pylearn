# This is an example for defining a function
def hello():
    name=str(input("Enter your name."))
    if name:
        print("Hello "+ str(name))
    else:
        print("Hello world")
    return

hello()

