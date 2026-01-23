def divide(a ,b ):
    print(a /b)


def wrapper_divide(funct):
    def wrapper(a ,b):
        if a < b:
            a ,b = b ,a
        return funct(a,b)
    return wrapper

divide = wrapper_divide(divide)
divide(3 ,9)


# Method 2 :
# @chnageCase is  ==  greet = changeCase(greet)


def changeCase(func):
    def inner(*args , **kwargs):
        return func(*args , **kwargs).upper()
    return inner
@changeCase  #this or
def greet(name):
    return "Hello " + name
# greet = changeCase(greet)  this

print(greet("Manasa"))
