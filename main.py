def main():
    print("welcome to expenses tracker!\n")
    print("1. Add a new expense")
    print("2. View all expenses")
    print("3. View summary(by category,by date,total)")
    print("4. Delete an expense")
    print("5. Export to file (csv/json)")
    print("6. Quit")
    print("")

    choice  = input("What do you want to do ? ")
    print(f"You entered {choice}")


main()
