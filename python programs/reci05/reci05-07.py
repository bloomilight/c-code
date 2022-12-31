start=int(input("Starting number of organisms: "))
increase=(int(input("Average daliy increase: ")[0:-1]))/100
days=int(input("Number of days to multiply: "))
n=1
print("Day"," "*20,"Approximate Population")
while n<=days:
    print(n," "*20,start)
    start*=(1+increase)
    n+=1
