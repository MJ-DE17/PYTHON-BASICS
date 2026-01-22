def greet():
    print("Hello World")
greet()
greet()

def greet(name):
    print("Hello " + name)
greet("Manasa")

def sum (n ):
    print( n + n)
sum(58)

def sum (n , a):
    print( n * a)
sum(58 , 10)


# return sends the value back to the caller
def add(n, a):
    return n + a
value = add(58, 10)
print(value)

#  If no return, Python returns None
def add(n, a):
    print (n+a)
value = add(58, 10)
print(value)

# Passing Values to Functions
def multiply(a, b):
    return a * b
multiply(4, 5) # it doesn't print anything because it only returns

# to run we need to use print
print(multiply(4, 5))
