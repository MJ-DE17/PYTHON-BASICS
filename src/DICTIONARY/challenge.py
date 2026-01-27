user = {'id' : 1 , 'age' : 21 , 'city':'Vizag' , 'name' : 'Manasa'}

# user.update({'name'.upper() , 'city'.upper()})


user_str = {
    k.capitalize(): v.upper()
    for k , v in user.items() #loop
    if isinstance(v , str)
}
print(user_str)
