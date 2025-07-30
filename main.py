from datetime import datetime

def main():
    print("welcome to expenses tracker!\n")
    print("1. Add a new expense")
    print("2. View all expenses")
    print("3. View summary(by category,by date,total)")
    print("4. Delete an expense")
    print("5. Export to file (csv/json)")
    print("6. Quit \n")

    choice  = input("What do you want to do ? ").strip()
    if choice  == "1":
        add_new_entry()
    


def add_new_entry():
    category = input("Category(Food,Rent,Tution,Misc):").strip()
    expense = input("Expense(Amount):").strip()
    date = input("Date(Leave it empty to set the date to now):").strip()

    if not date:
        date = datetime.now().strftime("%Y-%m-%d")

    



main()
