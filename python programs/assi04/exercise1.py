number=int(input("Enter a positive number: "))
for i in range(1,2*number):
    for m in range(number-1-(abs(i-number))):
        print('-',end='')
    for s in range(2*abs(i-number)+1):
        print('#',end='')
    for d in range(number-1-(abs(i-number))):
        print('-',end='')
    print()
