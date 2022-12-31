f=open('wordlist.txt','r')
d={}
s=(f.read().split())
n=0
for word in s:
    try:
        d[word]=int(d[word])+1
    except:
        d[word]=1
print(d)
    
