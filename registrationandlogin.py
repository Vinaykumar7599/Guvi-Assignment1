def register():
    db = open("registered_ID.txt", "r")
    a = input("username: ")
    d = []
    for line in db:
        x = line.split(",")
        d.append(x[0])

    if a in d:
        print("Try Again with different username")
        register()

    elif (a[0] == '@' or a[0] == '$' or a[0] == '_' or a[0] == '%' or a[0] == '!' or a[0] == '#' or a[0] == '*' or a[
        0] == '&'):
        print("Start with only characters")
        register()

    else:
        print("Username created")

    b = input("Create your password with atleast one capital letter one integer and one special character: ")
    s = False

    if len(b) < 6 and len(b) > 18:
        print("Your Password must be minimum of six characters and maximum of 18, Try Again")
        register()

    if len(b) > 6 and len(b) < 18:
        l, u, p, d = 0, 0, 0, 0
        for i in b:
            if i.isdigit():
                d += 1
            if i.islower():
                l += 1
            if i.isupper():
                u += 1
            if (i == '@' or i == '$' or i == '_' or i == '%' or i == '!' or i == '#' or i == '*' or i == '&'):
                p += 1
            if (l >= 1 and u >= 1 and p >= 1 and d >= 1 and l + p + u + d == len(b)):
                s = True

    if s:
        c = input("Confirm Password: ")
        while (c != b):
            print("Password Miss Match")
            c = input("Try Again: ")

    else:
        print("Try again")
        register()

    file = open("registered_ID.txt", "a")
    file.write(a + "," + b + "\n")
    file.close()
    login()

def login():
    X=input("Enter your username to login: ")
    X = X.strip()
    db = open("registered_ID.txt", "r")
    d = []
    for line in db:
        x = line.split(",")
        d.append(x[0])

    if X in d:
        Y=input("Please Enter your password: ")
        Y=Y.strip()
        file1=open("registered_ID.txt","r").readlines()
        for x in file1:
            x=x.strip()
            info=x.split(",")
            if X==info[0] and Y==info[1]:
                print("Successfully")
            else:
                F = input("Forgot Password [y/n] : ")

                if F == "n":
                    print("try")
                    login()

                if F == "y":
                    b = input("Create Password using Special characters and Numbers: ")
                    s = False

                    if len(b) < 6 and len(b) > 18:
                        print("Password must contain minimum 6 character and maximum of 18")
                        register()

                    if len(b) > 6 and len(b) < 18:
                        l, u, p, d = 0, 0, 0, 0
                        for i in b:
                            if i.isdigit():
                                d += 1
                            if i.islower():
                                l += 1
                            if i.isupper():
                                u += 1
                            if (
                                    i == '@' or i == '$' or i == '_' or i == '%' or i == '!' or i == '#' or i == '*' or i == '&'):
                                p += 1
                            if (l >= 1 and u >= 1 and p >= 1 and d >= 1 and l + p + u + d == len(b)):
                                s = True

                    if s:
                        c = input("Confirm Password: ")
                        while (c != b):
                            print("Password doesn't match, Try Again")
                            c = input("Try Again: ")

                    else:
                        print("Sorry,Try again")
                        login()

                    file = open("registered_ID.txt", "w")
                    file.write(X + "," + b + "\n")
                    file.close()

    else:
        print("This ID is not registered")
        register()

def welcome():
    print("Use your Email ID as Username")
    W=input("Login|Register[l/r]: ")
    if W=="l":
        login()
    elif W=="r":
        register()
    else:
        print("Check The Credentials")
        welcome()
welcome()
