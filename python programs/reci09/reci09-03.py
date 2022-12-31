import random
number=int(input('input the number that a file will hold'))
f=open('random number.txt','w')
for i in range(number):
    f.write(str(random.randint(1,500))+'\n')
f.close()
