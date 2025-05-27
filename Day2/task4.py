def is_valid_pin(pin):
    return pin.isdigit() and len(pin) in (4, 6)


user_input = input("Enter a PIN: ")
if is_valid_pin(user_input):
    print("Valid PIN")
else:
    print("Invalid PIN")