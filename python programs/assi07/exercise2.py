def main():
    l=semi()
    print('Minimum:',min(l[0]))
    print('Maximum:',max(l[0]))
    print('Average:',f'{l[1]/l[2]:.2f}')

def semi():
    while True:
        while True:
            name=input('> Filename: ')
            try:
                f=open(f'{name}','r')
            except:
                print('File not found')
                break
            if len(f.readline())==0:
                print('The file is empty')
                break
            f.close()
            f=open(f'{name}','r')
            try:
                lista=[]
                total=0
                number=0
                for line in f:
                    lista.append(int(line))
                    total+=int(line)
                    number+=1
                g=[lista,total,number]
                return g
            except ValueError:
                print('The file contains invalid data')
                break
            

    

main()
