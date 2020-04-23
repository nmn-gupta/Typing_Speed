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


if choice == 1:
    while True:
        if check_Email():
            break
        else:
            pass

    password = input("Enter the password:")
    print("Sucessfully Logged in!!")
