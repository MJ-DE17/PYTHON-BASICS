from enum import unique

list = [ 1,2,3,4,5,6 , 0 , -1 , -5]

new_list = [ n for n in list]

# even:
new_list = [ n for n in list if n % 2 ==0 ]

print(new_list)

# Square of Numbers
sq = [n*n  for n in list ]
print(sq)

# Strings to Uppercase
names = ["manasa", "pavi", "mevin"]
up = [d.upper() for d in names ]
print(up)

# Filter Strings by Starting Letter 'm'
start_ltr = [name.upper() for name in names if name[0] == 'm']

# positive number

pos_num = [l for l in list if l > 0]
print(pos_num)

# Replace Values Using Condition

result = [x if x % 2 == 0 else 0 for x in list]
print(result)

# Flatten a Nested List
matrix = [[1, 2], [3, 4]]
flat = [x for row in matrix for x in row]
print(flat)

# remove duplicate
dpl = [1, 2, 2, 3]
unique = []
r_dpl = [unique.append(x)
         for x in dpl
         if x not in unique]
print(unique)

# Replace negative numbers with 0
rep_negative = [ x if x > 0 else 0 for x in list ]
print(rep_negative)

fl = [ n[0]  for n in names ]
print(fl)

vowels = [v for v in names if v in 'aieou']

# Extract unique elements
# unique_lst = list(set(dpl))
# print(unique_lst)


# Remove empty strings
Strings = ["" , "mansa" , "vaish" , "makha"]
empty = [s for s in Strings if s]
print(empty)