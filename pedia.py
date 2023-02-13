from string import *

def pedia(sentence=4):
    import wikipedia
    query = input("Enter your query: ")
    sentence = input("how many sentences do you want?\n you will get 4 sentences by default._:")
    answer = wikipedia.summary(query,sentences=sentence)
    link = wikipedia.page().url
    print(answer,"\n for more info follow the link below: \n",link)

def personalInfo():
        password = input("Enter password: ")
        confirm_password = input("confirm your password: ")
        while True:
            if password == confirm_password:
                print(f"You've been registerd, Mr.{name.capitalize()} so go ahead and read what you want.")
                pedia()
            else:
                print("Your password doesn't matched so,please try again here:  \n")
                personalInfo()
            

def nEmail():
    name = input("Enter name: ")
    email = input("Enter email: ")
    cond = "@gmail.com" and "@email.com"
    while True:
        if cond in email:
            personalInfo()
        if digits in name:
            print("invaid entry please fill again.")
            nEmail()
        else:
            print("Invalid Email please start here again:")
            nEmail()


print("***********WelCome To YourPedia************")
print("you have to go through some basic registeration to reach YourPedia")
name = input("press any key to start: ")
if name in ascii_letters:
    True
    nEmail()
else:
    print("Enter the single key please")