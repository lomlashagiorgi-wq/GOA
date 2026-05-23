students = ["Alex", "Ben", "Chris", "David", "Elena", "Frank", "George"]
top_three = students[:3]
print(students[ : :2])
students = students + ["Hannah"]
new_stduents = []

for i in students:
    if i != "David":
        new_stduents += [i]
        
students = new_stduents

print(students)
print(students[4:6])