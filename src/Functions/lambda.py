# my 1st labmda function
product = lambda x : x *2
print(product(4))

add = lambda x ,y : x +y
print(add(9 , 9))

word = lambda i : i in "Python"
print(word('y'))

# lambda in map

prices = ["$12.0", "$34.00" , "$60.0"]
print(list(map(lambda p : float(p.replace("$","")),prices)))

# break down it into steps LAMBDA MAP: DATA TRANSFORMATION
# 1.condition :  float(p.replace("$","") test for one string p ="$ 20.00"
# 2.if works : make it to lambdafucntion
# 3.map function to iterator
# 4. save the valiues as the list
# 5. print it =>


# remove all th eprices below than 100
# 1. labmda logic
# 2. filter logic
# 3. filter to applyfunction to filter alll the data
prices = [100 , 50 , 200 , 400 ,590]
print(list(filter(lambda p : p >= 100,prices)))

studs = [ ["Mx" , 90],
          ["El" , 90],
          ["MSH" , 59]]

print(list(filter(lambda  row : row[1] >=70 , studs)))
# starts with the 'M'
print(list(filter(lambda row : row[0].lower().startswith('m'), studs)))

name = " mansa"



