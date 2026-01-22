def add(a, b):   # a, b → parameters
    return a + b

add(2, 3)        # 2, 3 → arguments

def student(name, age, city):
    print(name, age, city)

data = student("Asha", city="Chennai", age=20)

print(data)

def add(*args):
    return sum(args)
ans = add(1,2,3,4)
print(ans)

# Argument Unpacking
# Unpacking list/tuple/dict into arguments
nums = [2, 3]
print(add(*nums))
def subtract(**ksrgs):
    return ksrgs

datas = {"a": 35, "b": 5}
print(subtract(**datas))

def profile(**kargs):
    return kargs
print(profile(name="Manasa" , age =21))

# There is NO difference between kargs, ksrgs, kwargs, or any other name.
# They are just variable names.
# What matters is:
# * → positional arguments
# ** → keyword arguments

# mutable passin args - (list, dict, set)
def modify(lstt):
    lstt.append(10)
x = [1 ,3]
modify(x)
print(x)

# immutable passin objects - (int, float, str, tuple)
def change(n):
    n = 10
x = 5
change(x)
print(x)