d={}
f=open('codes.txt','r')
for line in f:
    s=line.split(' ')
    d[s[0]]=s[1].strip('\n')
f.close()
g=open('testcode.txt','r')
m=g.read()
s=''
for character in range(len(m)):
    s+=d.get(m[character],m[character])
print(s)
