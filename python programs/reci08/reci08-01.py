def main():
    sale=[]
    total=0
    for i in range(7):
        d=day()
        sale.append(d)
        total+=d
    print (sale)
    print (total//7)

def day():
    s=int(input('sale'))
    return s

main()
