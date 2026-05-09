security_pin = 1234

correct_pin = int(input("Please enter your pin: "))

if correct_pin == security_pin:
    print("Welcome!")

else:
    print("Access denied.")

