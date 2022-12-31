
def main():
    d=build_attraction_dict('top_tourist_attractions.txt')
    add_attraction(d)
    h=build_province_attraction_dict(d)
    w=most_attractions(h)
    print()
    print('Provinces with at least 3 attractions:')
    for i in w:
        print(i)
    

def build_attraction_dict(n):
    f=open(f'{n}','r')
    d={}
    for line in f:
        s=line.split(',')
        d[(s[1]).strip('\n')]=s[0]
    return d

def add_attraction(d):
    a=input('Input a new attraction: ')
    b=input('Input a new province: ')
    d[a]=b

def build_province_attraction_dict(d):
    s={}
    for k,v in d.items():
        if s.get(v)==None:
            s[v]=[k]
        else:
            s[v].append(k)
    return s

def most_attractions(d):
    s=set()
    for k in d.keys():
        if len(d.get(k)) > 2:
            s.add(k)
    return s


if __name__=='__main__':
    main()

