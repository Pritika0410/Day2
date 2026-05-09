print("Nova AI")
print("Instructions: Type exit to shutdown")
print("-" * 40)

while 1 == 1:
    user = input("user: ")

    if user == "exit":
        print("shutting down, goodbye!")
        break

    if user == "hello":
        print("Hello, I am Nova AI!")

    elif user == "status":
        print("All operations running!")

    else:
        print(f"I dont understand {user}")