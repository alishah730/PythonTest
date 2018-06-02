def outer(func):
    def inner():
        print("Accessing :", func.__name__ +" hello")
        return func()
    return inner

@outer
def greet():
    return "Hello"


#wish = outer(greet)

# wish()

greet=outer(greet) #decorating greet


greet() # calling new greet
