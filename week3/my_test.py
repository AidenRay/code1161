
def some_function():
    
    while True:
        x = input("Give me something: ")
        print(x)
        if x == "Exit!":
            return x
some_function()