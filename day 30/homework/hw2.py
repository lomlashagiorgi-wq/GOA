temperatures = [12, -2, 5, -5, 0, 18, -1]

for temp in temperatures:
    if temp < 0:
        print("ყინვაა:", temp, "გრადუსი")
    elif temp <= 15:
        print("გრილა:", temp, "გრადუსი")
    else:
        print("თბილა:", temp, "გრადუსი!")