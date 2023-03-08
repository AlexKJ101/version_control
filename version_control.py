#Alexander Jamison

def encode(password):
    new_pass = ""
    for i in password:
        if int(i) < 7:
            new_pass = new_pass + str(int(i) + 3)
        elif i == "7":
            new_pass = new_pass + "0"
        elif i == "8":
            new_pass = new_pass + "1"
        else:
            new_pass = new_pass + "2"
    return new_pass


if __name__ == "__main__":
    i = 0
    while i == 0:
        print("Menu \n------------- \n1. Encode \n2. Decode \n3. Quit ")
        option = input("Please enter an option: ")
        if option == "1":
            input_password = input("Please enter your password to encode: ")
            encoded = encode(input_password)
            print("Your password has been encoded and stored!")
        else:
            i = 1





