# Aiden's Code
def password_encoder(password):
    result = ""
    for i in range(0, len(password)):
        result += str((int(password[i])+3)%10)
    return result


def password_decoder(encoded_password):
    decoded_password = ""

    for char in encoded_password:
        decoded_digit = str((int(char) - 3) % 10)  # Shift the digit down by 3 and wrap around
        decoded_password += decoded_digit

    return decoded_password




if __name__ == '__main__':
    while(True):
        print('-------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit')
        print()
        user_choice = input('Please enter an option: ')
        if user_choice == "1":
            user_password = input('Please enter your password to encode: ')
            encoded_password = password_encoder(user_password)
            print('Your password has been encoded and stored!')
        elif user_choice == "2":
            decoded_password = password_decoder(encoded_password)
            print('The decoded password is ' + encoded_password + ', and the original password is', decoded_password)
        else:
            break



