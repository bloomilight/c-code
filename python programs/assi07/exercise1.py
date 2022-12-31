def main():
    f=open('file1.txt','r')
    g=open('file2.txt','r')
    s=[]
    for line1 in g:
        s.append(line1)
    for line2 in f:
        s.append(line2)
    
    p=open('file1.txt','w')
    for line3 in s:
        p.write(line3)
    p.close()
    q.close()
main()
