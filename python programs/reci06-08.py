sentence=input("input your sentence")
print(str.upper(sentence[0]),end='')
for i in range(1,len(sentence)):
    if sentence[i-2:i] == '. ':
        print(str.upper(sentence[i]),end='')
    else:
        print(sentence[i],end='')
