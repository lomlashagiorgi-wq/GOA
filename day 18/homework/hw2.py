guess_password =input("enter your pasword:")
password = "asdfghjk" 
count = 0
while guess_password != password:
    count += 1
    print("try again its wrong password")
    guess_password = input("enter your password:")

print("your guessed pasword its:",guess_password,"tries:",count,)