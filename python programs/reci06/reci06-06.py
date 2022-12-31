name=input("name=")
length=len(name)
for i in range(length):
    if str.isupper(name[i]):
        print(name[i],".",end='')
    
