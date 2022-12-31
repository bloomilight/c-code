name=input('input the name')
g=open('GirlNames.txt','r')
b=open('BoyNames.txt','r')
a=False
c=False
for line in g:
    if name==line.strip('\n'):
        a=True
if a:
    print('it is popular among girls')
else:
    print('it is not popular among girls')

for line in b:
    if name==line.strip('\n'):
        c=True
if c:
    print('it is popular among boys')
else:
    print('it is not popular among boys')
