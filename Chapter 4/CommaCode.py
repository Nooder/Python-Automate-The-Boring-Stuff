test = ["super", "happy", "fun", "monkeys", "omg"]

def commaCode(list):
    str = ""
    for i in range(len(list)):
        if i == 0:
            str += list[i]
        elif i < len(list) - 1:
            str += ", " + list[i]
        else:
            str += " and " + list[i]
    return str

print(commaCode(test))