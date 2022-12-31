import random
d={1:'rock', 2:'paper', 3:'scissor'}

for i in range(3):
    computer=d[random.randint(1,3)]
    while True:
        user=(input('input your choice')).lower()
        if user=='scissor' or user=='rock' or user== 'paper':
            break
    print(computer)
    if user=='scissor' and computer=='paper' or user=='rock' and computer=='scissor' or user=='paper' and computer=='rock':
        print('you win')
        break
    elif computer=='scissor' and user=='paper' or computer=='rock' and user=='scissor' or computer=='paper' and user=='rock':
        print('you lose')
        break
    else:
        continue
    print('draw')

    

