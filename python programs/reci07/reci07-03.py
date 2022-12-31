def main():
    first=int(input('first number'))
    second=int(input('second number'))
    print(f"the bigger number is {maximum(first, second)}")


def maximum(first,second):
    if first>=second:
        return first
    else:
        return second

main()

