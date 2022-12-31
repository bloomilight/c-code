def main():
    N=int(input('input your number'))
    diamond(N)

def diamond(N):
    for s in range(1,N+1):
        print(f'{s:02d}',end='')
    print('')
    for k in range(1,N-1):
        for q in range(1,abs((N-1)//2-k)+2):
            print(f'{q:02d}',end='')
        for n in range(4*((N+1)//2-1-abs((N+1)//2-1-k))-2):
            print(' ',end='')
        for m in range(N-abs((N-1)//2-k),N+1):
            print(f'{m:02d}',end='')
        print('')
    for w in range(1,N+1):
        print(f'{w:02d}',end='')
    print('')

if __name__=='__main__':
                       main()
    

