from datetime import datetime
from tabulate import tabulate
import csv
import os 

def main():
    ensure_csv_file()  #Ensures that the header and csv file exists

    print("Welcome to expenses tracker!\n")
    print("1. Add a new expense")
    print("2. View all expenses")
    print("3. View summary(by category,by date,total)")
    print("4. Delete an expense")
    print("5. Export to file (csv/json)")
    print("6. Quit \n")

    choice  = input("What do you want to do ? ").strip()
    if choice  == "1":
        add_new_entry()
    elif choice == "2":
        view_all_expenses()
    


def add_new_entry():
    category = input("Category(Food,Rent,Tution,Misc):").strip()
    expense = input("Expense(Amount):").strip()
    date = input("Date(Leave it empty to set the date to now):").strip()
    print("")
    if not date:
        date = datetime.now().strftime("%Y-%m-%d")

    with open("expenses.csv",mode="a",newline="") as file:
        writer  = csv.writer(file)
        writer.writerow([category,expense,date])

    print(f"Added: {category} | {expense} | {date}")



def ensure_csv_file():
    filename = "expenses.csv"
    if not os.path.isfile(filename):
        with open(filename,mode="w",newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["category","expense","date"])

def view_all_expenses():
    with open("expenses.csv","r") as file:
        reader = csv.reader(file)
        headers = next(reader)
        data = list(reader)
        print(tabulate(data, headers=headers,tablefmt='psql'))

main()
