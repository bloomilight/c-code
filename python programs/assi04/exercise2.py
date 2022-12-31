number=int(input('How many words (3-6): '))
shortest=''
longest=''
average=0
for i in range(1,number+1):
    word=input(f'Word #{i} please > ')
    length=len(word)
    if length >= len(longest):
        longest=word
    elif longest == '':
        longest=word
    if length <= len(shortest):
        shortest=word
    elif shortest == '':
        shortest=word
    average+=length
print('Shortest:',shortest)
print('Longest:',longest)
print('Average Length:', f"{average/number:.2f}")
    
