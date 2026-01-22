gender = [ "F" , "M" , "T"]
for x in gender:
    print(x)

# looping htrough string

for x in "Hello":
    print(x)
    if x =="l":
        break
    # print(x)
#  conitnues ignore annd skips the continon
for x in "Hello":
    # print(x)
    if x =="l":
        continue
    print(x)
# range

for x in range(6):
    print(x)

for x in range(2, 30, 3):
  print(x)

for x in range(6):
  print(x)
else:
  print("Finally finished!")

days = ["Mon" , "Tues" , "Wed" , "Thurs" , "Fri"]
week_count =  [1 ,2,3,4 ,5]
for day , date in zip (days , week_count):
    print(day,date)


# alternative naswer
for i in range(len(days)):
    print(days[i], week_count[i])
