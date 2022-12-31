d1={'CS101':3004,'CS102':4501,'CS103':6755,'NT110':1244,'CM241':1411}
d2={'CS101':'Haynes','CS102':'Alvarado','CS103':'Rich','NT110':'Burke','CM241':'Lee'}
d3={'CS101':'8:00am','CS102':'9:00am','CS103':'10:00am','NT110':'11:00am','CM241':'1:00pm'}
number=input('input your course number')
print(f'room number: {d1.get(number)}\ninstructor: {d2.get(number)}\nmeeting time: {d3.get(number)}')
