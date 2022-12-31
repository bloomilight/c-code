f=open('USPopulation.txt','r')
before=int(f.readline())
big=0
small=99999999
total=0
b=0
c=0
for i in range(1950,1990):
    now=int(f.readline())
    if now-before>=big:
        big=now-before
        b=i
    if now-before<=small:
        small=now-before
        c=i
    total=now-before
    before=now
f.close()
print('average:',total//40)
print('greatest increase:',b)
print('smallest increase:',c)

        
