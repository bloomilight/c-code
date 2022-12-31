t=1
tui=8000
print("year"," "*12,"tuition")
while t<=5:
    print(t," "*20,round(tui*1.05**(t-1),2))
    t+=1
