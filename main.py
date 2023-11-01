# Aiden's Code
def password_encoder(password):
    result = ""
    for i in range(0, len(password)):
        result += str(int(password[i])+3)
    return result


if __name__ == '__main__':
    user_password = input("Please enter password: ")
    encoded_password = password_encoder(user_password)
    print("Encoded password is:", encoded_password)

