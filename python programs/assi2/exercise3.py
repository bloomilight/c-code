year=int(input('Year: '))
if year%4==0:
    if year%400==0:
       print('Leap year')
    elif not year%100==0:
       print('Leap year')
    else:
       print('Not leap year')
else:
    print('Not leap year')
if (year+2)%4==0 and year>=1950:
    print('World Cup year')
if year%4==0 and year>=1960 and not year==2020:
    print('Euro Cup year')
elif year==2021:
    print('Euro Cup year')
    
    
