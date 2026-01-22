
def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result

print(multiply(2,3,4))

def extract_numbers(**kwargs):
    numbers = []
    for value in kwargs.values(): #all values from dictionary
        if isinstance(value, int):  #is th built in key to check the type of specific value
            numbers.append(value)
    return numbers
print(extract_numbers(name="Manasa", age=21, score=90, city="Chennai"))

def total(*args , **kwargs):
    total = 0
    for num in  args:
        total += num
    for num in kwargs.values():
        if isinstance(num ,int):
            total += num
    return total
print(total(10, 20, bonus=5, age=21))

# Default Argument
def add_item(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst
