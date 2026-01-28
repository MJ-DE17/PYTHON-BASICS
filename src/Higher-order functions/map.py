# # to do data transformation : how we gonna do it :
# map is the fast , clean way to do data transformation
    # 1. for loop
    # 2. map - function wjant to repeat and iterable

letters = ["s","f","g"]
print(list(map(str.upper, letters)))
# ['S', 'F', 'G']

# convert list items into integers
nums = [ '1','2' , '3']
print(list( map(int ,nums)))

for i in ( map(int ,nums)):
    print(i)

#
name = ["steve " , "El" ,"Max "]
print(list(map(str.strip , name)))

# looping:
for n in (map(str.strip , name)):
    print(n)