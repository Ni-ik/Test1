def fun1(a):
    return a[1]**2


a=[
    [1,0.3],
    [2,0.2]
]

a.sort(key=fun1)

print(a)
print(sum(a[:][0]))
print ("vvv")
a={1:3, 2:4}
c=[i for i in a if i>1]
print(c)

a=['1','2','3','4']
print( 3 in a)
print(', '.join(a).join(a))
c=a
