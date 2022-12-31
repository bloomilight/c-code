def main():
    lottery_number=[]
    for i in range(7):
        lottery_number.append(number())
    print (lottery_number)

def number():
    import random
    s=random.randint(0,9)
    return s

main()
