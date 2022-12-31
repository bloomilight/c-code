def main():
    s1=[]
    s2=[]
    s3=[]
    S=[s1,s2,s3]
    display_square(S)
    print(s1)
    print(s2)
    print(s3)
    if judge(S)== 'no' :
       print('no')
    else:
        print('yes')
            
        
        
def display_square(S):
    for k in range(3):
        for i in range(3):
            s=int(input('number'))
            S[i].append(s)

def judge(S):

    for i in range(3):
        s=0
        for k in range(3):
            s+= S[i][k]
        if s!=15:
            return 'no'

main()
