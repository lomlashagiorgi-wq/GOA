text = "hello"
new_text = ""
for i in range(len(text)):
    if i == 2:
        new_text += "a"
    else:
        new_text += text[i]
print(new_text)