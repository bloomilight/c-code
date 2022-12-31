name=input("input the name of the file")
f=open(name,'w')
i=1
for line in f:
    f.write(f'{i}: {line}')
    i+=1
f.close()

