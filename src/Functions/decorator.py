# Decorator = function that modifies another function
# Uses @decorator_name
# Inner function = wrapper()
# func() executes original function

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


def myfunction8():
  return "Have a great day!"
print(myfunction8.__name__)


# decorator that counts how many times a function is called.
def count_calls(func):
    c =0
    def wrapperc():
        nonlocal c  # access to edit outer var
        c +=1
        print("Function called " ,c ," times")
        return func()
    return wrapperc

@count_calls
def greet():
    print("Hello")

greet()
greet()
greet()
greet()
greet()
greet()


# Allow function execution only if user is logged in.
logged_in = True
def login_req(func):
    def wrap():
        if logged_in:
            return func()
        else:
            print("Login please")
    return wrap

@login_req
def dashboard():
    print("Welcome to dashboard!")

dashboard()