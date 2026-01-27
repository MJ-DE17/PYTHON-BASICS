user = {'id' : 1 , 'age' : 21 , 'city':'Vizag'}
# using keys
print(user['age'])

# to handle error
print(user.get('name', 'unknown'))

# checks
print("gender" in user)
print("age" not in user)

# view Obj
print(user.keys())
print(user.values())
print(user.items()) #gives in the tuples dict_items([('id', 1), ('age', 21), ('city', 'Vizag')])
print(user)  #{'id': 1, 'age': 21, 'city': 'Vizag'}


# Looping
for u in user:
    print(u,user[u])

for key, value in user.items():
    print(key , value)

# ADD , UPDATE , REMOVE
user["name"] = 'Manasa'

user['age'] = 22
user.update({'city' : 'Chennai', 'name' : 'sudh'})
print(user)

user.pop('age')
user.popitem()
print(user)

# fromkeys : build anew dict where all the keys get the same default value

users = dict.fromkeys(["id" , "name" , "age", "city"],None)
print(users)
users["age"] = 55
print(users)



