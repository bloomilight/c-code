def main():
    for t in range(10):
        print(f"the falling distance in {t}s is {falling_distance(t)}m")

def falling_distance(t):
    d=round(0.5*9.81*t,2)
    return d

main()
