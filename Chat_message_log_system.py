messages = []

def add_message():
    sender = input("Enter sender name: ")
    text = input("Enter message: ")
    messages.append({"sender": sender, "text": text})
    print("Message saved")

def view_messages():
    if not messages:
        print("No messages available")
    else:
        for msg in messages:
            print(msg["sender"], "says:", msg["text"])

def main():
    while True:
        print("1. Add Message")
        print("2. View Messages")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_message()
        elif choice == "2":
            view_messages()
        elif choice == "3":
            break
        else:
            print("Invalid option")

main()
