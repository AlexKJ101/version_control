#Alexander Jamison

def encode(password):
    new_pass = ""
    #Cycles through each digit of the original password and encodes it before storing it in a new variable
    for i in password:
        if int(i) < 7:
            new_pass = new_pass + str(int(i) + 3)

        #The following are if statements so that the digits wrap back around instead of going into double digits
        elif i == "7":
            new_pass = new_pass + "0"
        elif i == "8":
            new_pass = new_pass + "1"
        else:
            new_pass = new_pass + "2"

    #returns the newly encoded password
    return new_pass

#Function to decode the encoded password
def decode(encoded_pass):



if __name__ == "__main__":

    #Loops the menu so that the user can use the encoder/decoder more than once without restarting the program
    i = 0
    while i == 0:

        #Prints out a visual display of the menu
        print("Menu \n------------- \n1. Encode \n2. Decode \n3. Quit ")

        #Asks the user to select which option they want to use for the program
        option = input("Please enter an option: ")

        if option == "1":

            #Prompts user to input a password
            input_password = input("Please enter your password to encode: ")

            #Runs the encode function to encode the password
            encoded = encode(input_password)
            print("Your password has been encoded and stored!")

        elif option == "2":

            #Decodes the previously encoded password and returns the original password
            original = decode(encoded)
            print(f"The encoded password is {encoded}, and the original password is {original}.")

        else:

            #Ends the while loop and the program by setting i equal to a number other than 0
            i = 1





