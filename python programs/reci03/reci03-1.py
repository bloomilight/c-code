a=int(input("input the length of the first rectangle"))
b=int(input("input the width of the first rectangle"))
c=int(input("input the length of the second rectangle"))
d=int(input("input the width of the second rectangle"))
if(a*b)>(c*d):
    print("the first rectangle is bigger than the second rectangle")
elif(a*b)==(c*d):
    print("the first rectangle is the same as the second rectangle")
else:
    print("the first rectangle is smaller than the second rectangle")

