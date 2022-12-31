x=int(input("input your number"))
n=x
result=x
process=str(x)
while n>=2:
     n-=1
     result*=n
     process+="*"
     process+=str(n)
print(str(x)+"!="+str(process)+"="+str(result))
    
