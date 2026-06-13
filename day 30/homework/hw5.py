email1 = input("შეიყვანე ელ-ფოსტა: ")
email2 = input("გაიმეორე ელ-ფოსტა: ")

if email1 != email2:
    print("იმეილები არ ემთხვევა")
elif len(email1) <= 10:
    print("ტექსტი ძალიან მოკლეა")
elif "@" not in email1:
    print("აკლია @ სიმბოლო")
else:
    print("იმეილი წარმატებით დარეგისტრირდა")