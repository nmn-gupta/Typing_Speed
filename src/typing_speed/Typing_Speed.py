print("Press 1. for login/sign in")
print("Press 2. for registration/sign up")
choice = int(input())


def check_Email():
    input_Email = input("Enter the Email: ")
    e = input_Email
    r = "abcdefghijklmnopqrstuvwxyz._0123456789/\*-"
    if "@" in e:
        t = e.partition("@")
        if all(i in r for i in t[0]):
            if all(j in r for j in t[2]) and (t[2].endswith(".com") or t[2].endswith(".in")):

                return True


            else:
                print("Invalid Email!!")
                return False

    else:
        print("Invalid Email!!")

        return False


def check_password():
    input_password = input("Enter the password: ")
    s = input_password
    special = ",.#@$%&^*_-"
    flag = 1
    l = len(s)
    if any(i.isspace() for i in s):
        print("Inavalid Password!!")
        print("There shouldn't be any space!!")
        return False


    elif not (l >= 5):
        print("Inavalid Password!!")
        print("Password must contain atleast five characters!!")
        return False


    elif not (l <= 10):
        print("Inavalid Password!!")
        print("Password contains atmost ten characters!!")
        return False


    elif not (any(i.isdigit() for i in s)):
        print("Inavalid Password!!")
        print("Password must contains atleast one digit!!")
        return False

    elif not (any(i in special for i in s)):
        print("Inavalid Password!!")
        print("Password must contain atleast one special character!!")
        return False

    elif not (any(i.isupper() for i in s)):
        print("Inavalid Password!!")
        print("Password must contain atleast one upper case alphabet!!")
        return False


    elif not (any(i.islower() for i in s)):
        print("Inavalid Password!!")
        print("Password must contain atleast one lower case alphabet!!")
        return False


    else:
        return "True"


if choice == 1:
    while True:
        if check_Email():
            break
        else:
            pass

    password = input("Enter the password:")
    print("Sucessfully Logged in!!")
