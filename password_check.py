
PASSWORD_LENGTH = 6


def main():
    password = input("Enter Valid Password:\n>> ")
    valid_password = get_valid_password(password)
    display_password_length(valid_password)


def get_valid_password(password):
    while len(password) < PASSWORD_LENGTH:
        password = input("Password must be {} letters or over\n>> ".format(PASSWORD_LENGTH))
    return password


def display_password_length(valid_password):
    for i in valid_password:
        print("*", end="")


main()
