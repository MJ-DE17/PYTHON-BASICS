from List.lvl5_loop import max_val

dict = {}
s = "programming"

for ch in s :
    dict[ch] = dict.get(ch,0) + 1
print(dict)

s = "hey im doing okay.Hey"

s = s.lower().replace("." , " ")
words = s.split()
w_d = {}

for w in words:
    w_d[w] = w_d.get(w,0)+1
print(w_d)

# FIND KEY WITH MAXIMUM VALUE
d = {"e":10,"b":40,"c":20}
print(max(d,key=d.get))

# max(iterable, key=function)
# iterable → what to loop on
# key=function → how to compare items
# d.get(key) - returns the value of that key.

# using loop:
max_key = None
max_val = -1

for k in d:
    if d[k] > max_val:
        max_val = d[k]
        max_key = k
print("using loop " , max_key)

# k is key ; d[k] is val of key

# FIND KEY WITH MINIMUM VALUE using keys() loop
d = {"a":10,"b":40,"c":20}

min_key = None
min_value = float("inf")
print(min(d,key=d.get))
for k in d.keys():
    if d[k] < min_value:
        min_value = d[k]
        min_key = k


# Q5 MERGE TWO DICTIONARIES

d1 = {"a":1,"b":2}
d2 = {"c":3,"d":4}
d1.update(d2)
print(d1)

# Q6 REMOVE DUPLICATES FROM LIST USING DICTIONARY
lst = [12,3,4,5,12]

dit = list(dict.fromkeys(lst))
print("Q6 : " ,dit)


# Q7 SORT DICTIONARY BY VALUES
d = {"a":3,"b":1,"c":2}


sorted_dd = dict(sorted(d.items(), key=lambda x:x[1]))

# or
sorted_d = {}
while d:
    min_key = None
    min_val = float("inf")

    for k in d:
        if d[k] < min_val:
            min_val = d[k]
            min_key = k

    sorted_d[min_key] = d[min_key]
    d.pop(min_key)

print(sorted_d)

# Q8 CHECK IF TWO STRINGS ARE ANAGRAM
s1 = "listen"
s2 = "silents"

d1 = {}
d2 = {}

for c in s1 :
    d1[c] = d1.get(c ,0)+ 1
for c in s2 :
    d2[c] = d2.get(c ,0)+ 1
print(d1 == d2)

# Q9 GROUP ELEMENTS WITH SAME LENGTH

words = ["hi","hello","to","python","go"]
d = {}

for w in words:
    d[w] = d.get(w ,0)+ 1

# for i in item
