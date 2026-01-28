# syntax - filter(function , Iterable)
# used for filtering out eg instead of removing using remove() ,  we do the filter function
# its perfect for the cleaning up the data
# define filter rule  + data = output

letters = ["s","f" , "", None , False,"g"]
print(list(filter(None , letters) ))# None removes the empty string , False an even the None
# ['s', 'f', 'g']

for i in filter(bool , letters):
    print(i)
    # s
    # f
    # g

items = ["s","f" ,'1','2',"g"]

# keeps only the letters:
print(list(filter(str.isalpha , items)))
# ['s', 'f', 'g'] here (str.isalpha) str in the class name
