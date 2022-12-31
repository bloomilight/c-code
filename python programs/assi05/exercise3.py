
def greatest_common_divisor(n1,n2):
        for i in range(min(n1,n2),0,-1):
            if n1%i ==0 and n2%i==0:
                n1=n1%i
                n2=n2%i
                return i
def reduce_fraction(num,den):
        k=greatest_common_divisor(num,den)
        num=num//k
        den=den//k
        return num,den

if __name__ == '__main__':
       greatest_common_divisor(n1,n2)
       reduce_fraction(num,den)
    
    
