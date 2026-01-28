# combines 2 or more sequences into pairs(tuples)

numbs =[ 1,2,3,4]
letters = ["s","f","g"]
print(list(zip(letters,numbs)))
# [('s', 1), ('f', 2), ('g', 3)]

for l , n in zip(letters , numbs):
    print(l , n)
    # s 1
    # f 2
    # g 3