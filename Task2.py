security_pin = 1234

correct_pin = int(input("Please enter the security pin."))

# correct_pin = int(correct_pin)

if security_pin == correct_pin:
    print("Welcome!")
else: print("Acess denied.")

