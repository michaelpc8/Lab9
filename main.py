# Michael Pierre-Canel

main = True
password = ()
encodedPass = ()

def encoder(password):

    passwordList = []
    encodedPass = ""

    passwordList.extend(password)
    for num in passwordList:
        num = int(num)
        num += 3
        num = str(num)
        encodedPass += num
    return encodedPass

def main():
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        choice = input("Please enter an option: ")

        if choice == "1":
            password = input("Please enter your password to encode: ")
            encoded_password = encoder(password)
            print("Your password has been encoded and stored!")

        elif choice == "2":
            decoded_password = decode(encoded_password)
            print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}")

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please choose 1, 2, or 3.")


if __name__ == "__main__":
    main()
