print("Welcome the System")

sys_pas="123"
sys_usern="henry"

usern = input("Username: ")
pas = input("password: ")

if sys_usern == usern and sys_pas != pas:
    print("password wrong")
elif sys_usern != usern and sys_pas == pas:
    print("Username wrong")
else:
    print("Welcome")


