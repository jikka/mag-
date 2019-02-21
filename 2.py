a=input("\nEnter the N number")
b=input("\nEnter the K number")
c=list(str(a))
d=b
while d>0:
    d=d-1
    del(c[d])
print(''.join(c))
