f=open('specialfile.txt','r')
k=set()
a=[]
for line in f:
    if line.strip('\n') in k:
        try:
            a.remove(line.strip('\n'))
        except:
            continue
    else:
        k.add(line.strip('\n'))
        a.append(line.strip('\n'))
print(a)
