x=float(input("Enter a number: "))
y=x/2
while y**2-x>0.001 or x-y**2>0.001:
    y=(y+x/y)/2
print("Square root:",format(y,'.3f'))
