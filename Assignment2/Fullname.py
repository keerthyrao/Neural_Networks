fname = input("Enter your first name: ")
lname = input("Enter your last name: ")
def fullname(fname, lname):
    global full_name
    full_name = fname + " " + lname
    print("your full_name is : ", full_name)
fullname(fname, lname)
def string_alternative(full_name):
    print("your alternative string is: ", full_name[::2])
string_alternative(full_name)
