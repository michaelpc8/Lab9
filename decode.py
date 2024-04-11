def decode(password):
    passwordList = []
    decodedPassword = ""

    passwordList.extend(password)
    for number in passwordList:
        number = int(number)
        number -= 3
        number = str(number)
        decodedPassword += number
    return decodedPassword