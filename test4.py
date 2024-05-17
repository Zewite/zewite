#create
'''a = [1,2.1,3]
tuple(a)
b = tuple('abc') '''
a = (1, 1.1, 'a',[4,5,6],{'a':1,'b':2},None,True)
a =()
b = tuple()
b=(1,)
a = [1,2.1,3]
tuple(a)
b = tuple('abc')
a = (1,2.1,'d')
a[0]
a[2]
# их можно складывать
a = (1,2,3)
a = (4,5,6)
c = a + b
print(c) # now c= (1,2,3,4,5,6)
a += b # now a= (1,2,3,4,5,6)