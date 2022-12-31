def clean_users(L):
    S=L[:]
    for i in range(len(L)):
        for k in range(len(L[i])):
            if L[i][k] == 'c' or L[i][k] == 'C' or L[i][k] == 'g' or L[i][k] == 'G' or L[i][k] == 'z' or L[i][k] == 'Z':
                S.remove(L[i])
                break
    return S

