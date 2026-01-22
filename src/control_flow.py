

#short hand if :
if 10 < 34 : print("Intresting!")


a = 2
b = 330
print("A") if a > b else print("B")


bigger = a if a > b else b
print(bigger)
# if-else example
number = int(input("Enter a number: "))

if number > 0:
    print("Positive number")
elif number == 0:
    print("Zero")
else:
    print("Negative number")

# loop example
for i in range(1, 4):
    print("Count:", i)


if "s" in "friend":
    print("Happy")
else :
    print("Sad")