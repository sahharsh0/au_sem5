'''
  Library Management System: Manage book inventory, users, and transactions
'''
def user_login(users, username, password):
    if username in users and users[username] == password:
        print(f"Welcome, {username}!")
        return True
    else:
        print("Invalid username or password.")
        return False

def add_book(inventory, book_title):
    if book_title in inventory:
        print(f"'{book_title}' already exists in the inventory.")
    else:
        inventory.append(book_title)
        print(f"Added '{book_title}' to the inventory.")
def remove_book(inventory, book_title):
    if book_title in inventory:
        inventory.remove(book_title)
        print(f"Removed '{book_title}' from the inventory.")
    else:
        print(f"'{book_title}' not found in the inventory.")
def check_book(inventory, book_title):
    if book_title in inventory:
        print(f"'{book_title}' is available in the inventory.")
    else:
        print(f"'{book_title}' is not available in the inventory.")
def transaction(inventory, book_title, action):
    if action == "borrow":
        if book_title in inventory:
            inventory.remove(book_title)
            print(f"You have borrowed '{book_title}'.")
        else:
            print(f"'{book_title}' is not available for borrowing.")
    elif action == "return":
        if book_title not in inventory:
            inventory.append(book_title)
            print(f"You have returned '{book_title}'.")
        else:
            print(f"'{book_title}' was not borrowed or does not exist in the inventory.")
def main():
    users = {"admin": "password123", "user1": "pass1"}
    inventory = ['The Great Gatsby', 'The Metamorphosis', '1984', 'Pride and Prejudice']
    
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    if not user_login(users, username, password):
        return
    
    while True:
        print("\n1. Add Book")
        print("2. Remove Book")
        print("3. Check Book Availability")
        print("4. View Inventory")
        print("5. Borrow Book")
        print("6. Return Book")
        print("7. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            book_title = input("Enter book title to add: ")
            add_book(inventory, book_title)
        elif choice == "2":
            book_title = input("Enter book title to remove: ")
            remove_book(inventory, book_title)
        elif choice == "3":
            book_title = input("Enter book title to check availability: ")
            check_book(inventory, book_title)
        elif choice == "4":
            print("Books in the inventory:")
            if not inventory:
                print("No books available in the inventory.")
            for book in inventory:
                print(f"- {book}")
        elif choice == "5":
            book_title = input("Enter book title to borrow: ")
            transaction(inventory, book_title, "borrow")
        elif choice == "6":
            book_title = input("Enter book title to return: ")
            transaction(inventory, book_title, "return")
        elif choice == "7":
            print("Thank you for using the Library Management System.")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()