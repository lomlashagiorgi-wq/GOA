password = input("შეიყვანე ახალი პაროლი: ")
confirm_password = input("გაიმეორე პაროლი: ")
print("პაროლის სიგრძე:", len(password))
if password != confirm_password:
    print("პაროლები არ ემთხვევა")
elif len(password) <= 8:
    print("პაროლი ძალიან მოკლეა")
else:
    print("პაროლი წარმატებით შეიცვალა")