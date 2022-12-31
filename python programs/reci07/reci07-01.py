def main():
    actual_value=float(input('please input your property'))
    computePropertyTax(actual_value)
   

def computePropertyTax(actual_value):
    assesment=actual_value*0.6
    tax=assesment*0.72*0.01
    print(f'the assesment value is ${assesment}')
    print(f'The tax is $ {tax}')
    

main()
