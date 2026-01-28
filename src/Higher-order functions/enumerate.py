# returns both the valus and index
# why this is used?
# instead of for loop , we use it for finding the exact bad data

letters = ['a','f','s']
print(enumerate(letters))
#<enumerate object at 0x0000023B74AC6C50>

# so now we can print element :
print(list(enumerate(letters)))
# [(0, 'a'), (1, 'f'), (2, 's')]

print(list(enumerate(letters , start=1)))
# [(1, 'a'), (2, 'f'), (3, 's')] index strats from 1

letters = ['a','f','s']
for index , value in enumerate(letters):
    print(index , value)
# 0 a
# 1 f
# 2 s