def main():
    square=int(input('input the square'))
    cost=int(input('input the cost of the paint per gallon'))
    total_cost(square,cost)

def total_cost(square,cost):
    total_cost=calculate_paint_cost(square,cost)+calculate_labor_cost(square)
    print(f"the total cost is ${total_cost}")

def calculate_paint_volume(square):
    paint_volume=square/112
    return paint_volume

def calculate_labor_hours(square):
    labor_hours=square/112*8
    return labor_hours

def calculate_paint_cost(square,cost):
    paint_cost=calculate_paint_volume(square)*cost
    return paint_cost

def calculate_labor_cost(square):
    labor_cost=calculate_labor_hours(square)*35
    return labor_cost

main()
