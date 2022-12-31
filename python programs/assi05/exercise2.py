def valid_password(pwd):
    if check1(pwd):
        if check2(pwd):
            if check3(pwd):
                return True
            else:
                    return False
        else:
            return False
    else:
        return False

def check1(pwd):
    if len(pwd) < 10:
        print('Password is too short')
        return False
    else:
        return True
        
def check2(pwd):
    if not(str.isalnum(pwd)):
        print('Wrong characters')
        return False
    else:
        return True

def check3(pwd):
   if checkup(pwd) or checklow(pwd) or checkdigit(pwd):
       print('Need at least 1 uppercase letter, 1 lowercase letter and 1 digit')
       return False
   else:
       print('Valid password')
       return True

def checkup(pwd):
    for i in range(len(pwd)):
        if str.isupper(pwd[i]):
            return False
    return True

def checklow(pwd):
    for i in range(len(pwd)):
        if str.islower(pwd[i]):
            return False
    return True
def checkdigit(pwd):
    for i in range(len(pwd)):
        if str.isdigit(pwd[i]):
            return False
    return True

if __name__ == '__main__':
    valid_password(pwd)
    
