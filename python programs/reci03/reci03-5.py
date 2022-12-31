people=int(input("the number of people attending the event"))
number=int(input("the number of hotdogs each people will be given"))
print("The minimum number of packages of hot dogs required:",(people+9)//10*number)
print("The minimum number of packages of hot dogs buns required:",(people+7)//8*number)

print("The number of hot dogs that will be left over:",people%10*number)
print("The number of hot dog buns that will be left over:",people%8*number)
