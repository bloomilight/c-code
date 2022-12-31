import random
d1={}
d2={}
s=1
right=0
wrong=0
f=open('chinese-provincial-capitals.txt','r')
f.readline()
for line in f:
    a=line.split(',')
    d1[s]=a[0]
    d2[s]=a[1].strip('\n')
    s+=1
f.close()
print(d1)
print(d2)
while True:
    r=random.randint(1,s)
    province=d1[r]
    print(province)
    capital=input('input the capital')
    if capital ==d2[r]:
        print('it is correct')
        right+=1
    else:
        print('it is not correct')
        wrong+=1
    print('right answers:',right,'\n'+'wrong answers:',wrong)
