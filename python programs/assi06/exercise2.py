def valid_username(name, userList):
    if len(name)<4:
        print('Invalid User Name')
        return False

    if not(name.isalnum()):
        print('Invalid User Name')
        return False

    if name[0].isdigit():
        print('Invalid User Name')
        return False

    for i in range(len(userList)):
        if name.lower() == userList[i][0].lower():
            print('User Name Exists')
            return False

    print('Valid User Name')
    return True
    
def valid_password(password):
    upper=False
    lower=False
    digit=False

    if len(password)<10:
        print('Invalid Password')
        return False

    if not(password.isalnum()):
        print('Invalid Password')
        return False

    for i in range(len(password)):
        if password[i].isupper():
            upper=True
        if password[i].islower():
            lower=True
        if password[i].isdigit():
            digit=True

    if not(upper) or not(lower) or not(digit):
        print('Invalid Password')
        return False

    print('Valid Password')
    return True

def add_user(userList):
    
    while True:
        username=input('> Enter User Name: ')
        if valid_username(username,userList):
            break

    while True:
        password=input(f'> Enter Password for {username}: ')
        if valid_password(password):
            passwordC=input(f'> Confirm Password for {username}: ')
            if passwordC==password:
                print(f'User {username} created')
                userList.append([username,password])
                break
            else:
                print('Passwords do not match')


    
    
