admin = {'admin': '1234'}
students = {'1001': '111', '1002': '222', '1003': '333'}

# Courses
courses = ['MAT101', 'ENG101', 'ACC101']
MAT101 = ['1001', '1003']
ENG101 = ['1001', '1002']
ACC101 = ['1003']


def login():
    # Asks user for username and password
    username = input("Enter Username: ").lower()
    password = input("Enter Password: ")
    admin_mode = False

    # Checks if user is logging in as admin first to then bypass the student login
    if username in admin.keys():
        if password in admin.values():
            print("Logged in as Admin.")
            return username
        else:
            print("Username or Password incorrect.")
            return

    # Checks if username is valid
    if username in students.keys() or admin_mode:
        pass
    else:
        print("Username or Password incorrect.")
        return

    # Checks is password is valid
    if password in students.values() or admin_mode:
        pass
    else:
        print("Username or Password incorrect.")
        return

    # Tries logging in with given username and password
    if students[username] == password:
        print("Logged in as Student.")
        return username

    else:
        print("Username or Password incorrect.")
        return

def list_courses(username):
    counter = 0

    print("Enrolled in: ")
    if username in MAT101:
        print("MAT101")
        counter += 1

    if username in ENG101:
        print("ENG101")
        counter += 1

    if username in ACC101:
        print("ACC101")
        counter += 1

    if counter == 0:
        print("None")
    else:
        print(f"Total: {counter}")


def add_course(username):
    while True:
        course = input("Enter Course: ").upper()

        if course not in courses:
            print("Invalid Course.")

        if course == 'ACC101':
            if username in ACC101:
                print("You are already enrolled in ACC101.")
                ans = input("Enter 0 to return to menu, Enter 1 to add a course: ")
                if ans == '0':
                    break
                elif ans == '1':
                    pass
            else:
                print("Course added.")
                ACC101.append(username)
                break

        if course == 'MAT101':
            if username in MAT101:
                print(f"You are already enrolled in {course}.")
                ans = input("Enter 0 to return to menu, Enter 1 to add a course: ")
                if ans == '0':
                    break
                elif ans == '1':
                    pass
            else:
                print("Course added.")
                MAT101.append(username)
                break

        if course == 'ENG101':
            if username in ENG101:
                print("You are already enrolled in ENG101.")
                ans = input("Enter 0 to return to menu, Enter 1 to add a course: ")
                if ans == '0':
                    break
                elif ans == '1':
                    pass
            else:
                print("Course added.")
                ENG101.append(username)
                break


def drop_course(username):
    while True:
        course = input("Enter Course: ").upper()

        if course not in courses:
            print("Invalid Course.")

        if course == 'ACC101':
            if username not in ACC101:
                print(f"You are not enrolled in {course}.")
                ans = input("Enter 0 to return to menu, Enter 1 to drop a course: ")
                if ans == '0':
                    break
                elif ans == '1':
                    pass
            else:
                print("Course dropped.")
                ACC101.remove(username)
                break

        if course == 'MAT101':
            if username not in MAT101:
                print(f"You are not enrolled in {course}.")
                ans = input("Enter 0 to return to menu, Enter 1 to drop a course: ")
                if ans == '0':
                    break
                elif ans == '1':
                    pass
            else:
                print("Course dropped.")
                MAT101.remove(username)
                break

        if course == 'ENG101':
            if username not in ENG101:
                print(f"You are not enrolled in {course}.")
                ans = input("Enter 0 to return to menu, Enter 1 to drop a course: ")
                if ans == '0':
                    break
                elif ans == '1':
                    pass
            else:
                print("Course dropped.")
                ENG101.remove(username)
                break


def bill(username):
    enrolled_in = []
    in_state = False
    state_rate = 1500
    out_state_rate = 3500

    if username in MAT101:
        enrolled_in.append('MAT101')
    if username in ENG101:
        enrolled_in.append('ENG101')
    if username in ACC101:
        enrolled_in.append("ACC101")

    while True:
        answer = input("Are you a current North Carolina resident? [y/n]: ").lower()
        if answer == 'y':
            in_state = True
            break
        elif answer == 'n':
            in_state = False
            break
        else:
            print("Invalid entry, try again.")

    print("- - - - - BILL - - - - -")
    print(f"Number of Classes Enrolled: {len(enrolled_in)}")
    if in_state:
        print(f"Total: {len(enrolled_in) * state_rate}")
    else:
        print(f"Total: {len(enrolled_in) * out_state_rate}")
    print("- - - - - - - - - - - - -")


def menu():
    while True:
        select = input("Enter 0 to quit, Enter 1 to Login: ")

        try:
            select = int(select)
        except:
            print("Error, invalid entry.")

        if select > 1 or select < 0:
            print("Error, invalid entry.")

        if select == 0:
            print("Goodbye!")
            quit()

        if select == 1:
            global username
            username = login()
            if username != None:
                break
            else:
                menu()

    while True:
        answer = input("Enter 0 to logout, Enter 1 to add a course, Enter 2 to drop a course,"
                       " Enter 3 to list your courses, Enter 4 to show current bill: ")

        if answer == '0':
            print(f"Logged out of {username}")
            menu()

        elif answer == '1':
            add_course(username)

        elif answer == '2':
            drop_course(username)

        elif answer == '3':
            list_courses(username)

        elif answer == '4':
            bill(username)

menu()