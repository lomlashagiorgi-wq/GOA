steps = int(input("შეიყვანე გადადგმული ნაბიჯების რაოდენობა: "))
goal = int(input("შეიყვანე დასახული მიზანი: "))
if steps < goal:
    missing = goal - steps
    print("კიდევ", missing, "ნაბიჯი გჭირდება მიზნამდე!")
else:
    print("გილოცავ! მიზანი შეასრულე ან გადააჭარბე!")