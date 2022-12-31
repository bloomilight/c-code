try:
    f=open('random number.txt','r')
except IOError:
    print('IOError')
number=0
sum1=0
try:
    for line in f:
        number+=1
        sum1+=(int(line))
    f.close()
except ValueError:
    print('Value Error')
print('number:',number)
print('sum:', sum1)
print('average:',sum1//number)
    
