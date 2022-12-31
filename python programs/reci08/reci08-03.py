def main():
    import random
    series=[]
    total=0
    small=101
    big=0
    for i in range(20):
        s=random.randint(0,100)
        series.append(s)
        total+=s
        smaller(s)
        bigger(s)
    print("big=",big)
    print('small=',small)
    print('total=', total)
    print('average=',total/100)

def smaller(s):
    global small
    if s<small:
        small=s

def bigger(s):
    global big
    if s>big:
        big=s

main()   
