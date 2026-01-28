# returns an iterator tha flips the data order

letters = ['a','f','s']
print(reversed(letters))
# <list_reverseiterator object at 0x000002385FFE3FD0>

print(list(reversed(letters)))
# ['s', 'f', 'a']

for  value in reversed(letters):
    print(value)
# s
# f
# a