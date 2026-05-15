print("Nova AI")
print("Instructions: Type exit to shutdown")
print("-" * 40)

history = [" "]

while True:
    user = input("user: ")

    history.append("user")

    clean = user.lower().strip()

    if clean == "exit":
        print("shutting down, goodbye!")
        break

    if clean == "hello":
        print("Hello, I am Nova AI!")

    elif clean == "status":
        print("All operations running!")

    else:
        print(f"I dont understand {user}")

print("history")