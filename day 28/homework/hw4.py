students = ["Alex", "Ben", "Chris", "David", "Elena", "Frank", "George"]
top_three = students[:3]
print("პირველი სამი სტუდენტი:", top_three)
print("ყოველი მეორე სტუდენტი:", students[::2])
students.append("Hannah")
students.remove("David")
print("საბოლოო სია:", students)
print("ბოლო ორი სტუდენტი:", students[-2:])