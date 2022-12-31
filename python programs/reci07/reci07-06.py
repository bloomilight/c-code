def main():
    total=0
    for t in range(5):
        grade=int(input('input your grade'))
        total+=grade
        print(determine_grade(grade))
    print(f"the average score is {calc_average(total)}")
def determine_grade(grade):
    if grade>=90:
        return 'A'
    elif grade>=80:
        return "B"
    elif grade>=70:
        return "C"
    elif grade>=60:
        return"D"
    else:
        return"F"

def calc_average(total):
    s=total/5
    return s

main()
