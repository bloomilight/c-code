number=int(input("please input a number that is between 0-36"))
if number>=0 and number<=36:
   if number%2==0:
       if number==0:
           print("green")
       elif number<=10:
           print("black")
       elif number<=18:
           print("red")
       elif number<=28:
           print("black")
       else:
           print("red")
   else:
       if number<=10:
           print("red")
       elif number<=18:
           print("black")
       elif number<=28:
           print("red")
       else:
           print("balck")
else:
    print("wrong")
    
    

