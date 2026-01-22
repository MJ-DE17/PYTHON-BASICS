#Escape sequence :
a = "Pretty \flittle\b \ooo lady \noh oh \nyou can \rask \tme \"flowers \""

# output
# Pretty little \ooo lady 
# oh oh 
# you can 
# ask 	me "flowers "

print(a)

# Python - Format - Strings

age = 36
txt = f"My name is John, I am {age}"
print(txt)

# Display the price with 2 decimals:
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

# Perform a math operation in the placeholder:
txt = f"The price is {20 * 59} dollars"
print(txt)

# String Concatenation
a ="Joe"
b = "Keery"

print(a + " " + b)


# modification in strings :
a = "Data ,Engineering   "
print(a.upper())
print(a.lower())

# removw white space :

print(a.strip())
# replace 
print(a.replace("D" ,"B"))
# Split Stringinto list 
#  output :['Data ', 'Engineering   ']
print(a.split(","))


print("hey")

a ="""hey there
how you doing ?"""
print (a)

 # in arrays :
print(a[1])

for x in "apple":
    print(x)
    
print(len(a))

txt = " Are you doing good ? "
print("bad" in txt )


if "good" in txt:
    print("yes")
else :
    print("No")