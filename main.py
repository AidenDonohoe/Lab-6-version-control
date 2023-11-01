# Aiden's Code
def password_encoder(password):
    result = ""
    for i in range(0, len(password)):
        result += str((int(password[i])+3)%10)
    return result


if __name__ == '__main__':
    while(True):
        print('-------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit')
        print()
        user_choice = input('Please enter an option: ')
        if user_choice == 1:
            user_password = input('Please enter your password to encode: ')
            encoded_password = password_encoder(user_password)
            print('Your password has been encoded and stored!')
        elif user_choice == 2:
            print('The encoded password is' + password_encoder(user_password) + ', and the original password is', user_password)
        else:
            break



