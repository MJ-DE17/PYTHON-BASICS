tup =( 9 ,1,2,3,4 ,4)
for i in tup:
    print(i)
    print ("5" in tup)
    print(len(tup))
    print(tup.count(4))
    print(tup.index(4))
    # unpacking
    t = (1,2,3)
    a  ,b, c = t
    print(a ,b ,c)
    # /list -> tuple
    lst = [2,34,5,7]
    lt =tuple(lst)
    t = (4, 9, 1, 7)
    print(max(t))
    print(min(t))
    t = ((1, 2), (3, 4))
    print(t[1][0])