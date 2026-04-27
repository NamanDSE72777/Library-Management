from functions import show_books, issue_book, return_book, show_issued

def library():
    while True:
        print("\n====== LIBRARY MENU ======")
        print("1. Show Available Books")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. Show Issued Books")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            show_books()
        elif choice == "2":
            issue_book()
        elif choice == "3":
            return_book()
        elif choice == "4":
            show_issued()
        elif choice == "5":
            print("Thank you!")
            break
        else:
            print("Invalid choice")

library()