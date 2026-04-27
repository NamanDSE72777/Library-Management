from books import books, issued_Books
from datetime import datetime

# Show available books
def show_books():
    print("\nAvailable Books:")
    found = False
    for book, data in books.items():
        if data["available"] > 0:
            print(f"{book} → Available: {data['available']}/{data['total']}")
            found = True
    if not found:
        print("No books available.")


# Issue book
def issue_book():
    show_books()
    name = input("\nEnter book name: ")

    if name in books and books[name]["available"] > 0:
        student = input("Enter student name: ")
        issue_date = datetime.now()
        duration = books[name]["duration"]

        books[name]["available"] -= 1

        issued_Books.append({
            "book": name,
            "student": student,
            "date": issue_date,
            "duration": duration
        })

        print(f"\n'{name}' issued to {student}")
        print(f"Return within {duration} days")

    else:
        print("Book not available.")


# Return book and Fine imposition
def return_book():
    name = input("\nEnter book name: ")
    student = input("Enter student name: ")

    for record in issued_Books:
        if record["book"] == name and record["student"] == student:
            return_date = datetime.now()
            issue_date = record["date"]
            duration = record["duration"]

            days_used = (return_date - issue_date).days

            fine = 0
            if days_used > duration:
                late_days = days_used - duration
                weeks = (late_days // 7) + 1
                fine = weeks * 10   # Fine of ₹10 per week

            print("\nReturn Details:")
            print("Book:", name)
            print("Student:", student)
            print("Days Used:", days_used)

            if fine > 0:
                print(f"Late return! Fine = ₹{fine}")
            else:
                print("Returned on time")

            books[name]["available"] += 1
            issued_Books.remove(record)
            return

    print("Record not found.")


# It Show's issued books
def show_issued():
    print("\nIssued Books:")
    if len(issued_Books) == 0:
        print("No books issued.")
    else:
        for record in issued_Books:
            print(f"{record['book']} → {record['student']}")