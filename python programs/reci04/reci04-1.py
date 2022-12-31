import random
s=random.randint(1,10)
guess=int(input('input your guess'))
if s==guess:
    print('you are right,it is',s)
else:
    print('you are wrong,it should be',s)
