# username = user
# password = password
# loop menu
def menu():
    print("Menu\n-------------")
    print("1. Encode\n2. Decode\n3. Quit")
    print()


def password_encode(password):
    encoded = password
    for digit in password:
        encoded = int(password(digit)) + 3 % 10
    return encoded


while True:
    menu()
    yolo = int(input("Please enter an option: "))
    if yolo == 1:
        password = int(input("Please enter your password to encode: "))
        print("Your password has been encoded and stored!\n")
    if yolo == 2:
        password = password_encode(password)
        print(f'The encoded password is {password_encode(encoded)}, and the original password is {password}\n')


