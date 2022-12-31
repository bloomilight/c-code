number=int(input('Number of packages: '))
if number<10:
    print(round(number*49.99,2))
elif number<20:
    print(round(number*49.99*0.9,2))
elif number<50:
    print(round(number*49.99*0.8,2))
elif number<100:
    print(round(number*49.99*0.7,2))
else:
    print(round(number*49.99*0.6,2))
 
