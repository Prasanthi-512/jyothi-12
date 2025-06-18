def slug_generator(string):
    result = ""
    string = string.lower()
    for char in string:
        if char.isalnum():
            result += char
        elif char == " ":
            result += "-"
        else:
            continue
    return result
title=input()
result = slug_generator(title)
print(result)


#input format : Hello World! Welcome to Django
#output format : hello-world-welcome-to-django
#Specialcahracters must be skiped  space must be converted into "-" uppercase converted into lowercase
