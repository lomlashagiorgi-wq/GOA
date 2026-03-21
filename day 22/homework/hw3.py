score = int(input("შეიყვანეთ მიღებული ქულა: "))

if score == 100:
    print("A Group")
elif 80 <= score:
    print("B Group")
elif score >=99:
    print("B Group")
elif 40 <= score:
    print("C Group")
elif score >= 70:
    print("C Group")
else:
    print("D Group")
