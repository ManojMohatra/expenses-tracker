from datetime import datetime
from tabulate import tabulate
import csv
import os 
from collections import defaultdict
import sys

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
    print("")
    if choice  == "1":
        add_new_entry()
    elif choice == "2":
        view_all_expenses()
    elif choice == "3":
        view_summary()
    elif choice == "4":
        delete_expense()
    


def add_new_entry():
    category = input("Category(Food,Rent,Tution,Misc,...):").strip().lower()
    try:
        expense = float(input("Expense(Amount):").strip())
    except ValueError:
        print("Invalid expense amount.Please Enter a number")
        return

    date = input("Date(Leave it empty to set the date to now):").strip()
    print("")
    if not date:
        date = datetime.now().strftime("%Y-%m-%d")

    with open("expenses.csv",mode="a",newline="") as file:
        writer  = csv.writer(file)
        writer.writerow([category,expense,date])

    print(f"Added: {category} | {expense} | {date}",end="")



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
        if not data:
            print("No expenses to show")
        else:
            print(tabulate(data, headers=headers,tablefmt='psql'))

def view_summary():
    print("View Summary:\n")
    print("1. Total Expenses")
    print("2. Expense by category")
    print("3. Print Expense by date\n")

    choice  = input("What do you want to do? ").strip()
    print("")

    if choice == "1":
        print(f"The total expenses up to this point is:{total_expenses()}")
    elif choice  == "2":
        print_summary(calc_by_field("category"),["Category","Total"])
    elif choice == "3":
        print_summary(calc_by_field("date"),["Date","Total"])

def total_expenses():
    with open("expenses.csv","r") as file:
        reader = csv.DictReader(file)
        total = 0
        for row in reader:
            total += float(row["expense"])
    return total 


def calc_by_field(field):
    totals = defaultdict(float)
    with open("expenses.csv","r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            field_now = row[field]
            amount = float(row["expense"])
            totals[field_now] += amount
    return totals

def print_summary(data,headers):
    print(tabulate(data.items(),headers=headers,tablefmt="psql"))

def delete_expense():
    print("1.Delete last expense added to the database.")
    print("2.Manually select the expense to delete from the database.")

    choice = input("\nWhat do you want to do ? " ).strip()

    with open("expenses.csv","r",newline="") as file:
            reader = list(csv.reader(file))
                
    if choice ==  "1":
        if len(reader) > 1:
            delete_row(len(reader)-1,reader)
        else:
            print("Nothing to remove")
        
    elif choice == "2":
       for index,row in enumerate(reader):
                print(f"\nRow:{index} {row}")
       try:
            index = int(input("\nWhich row do you want do you want to delete? ").strip())
            if index >= len(reader) or index == 0:
                print("Invalid row number(0 is a header)")
       
            delete_row(index,reader)
       except ValueError:
            print("Invalid input.Please enter a valid number.")
            
       
             

def delete_row(choice,reader):
        choice = int(choice)
        deleted_row = reader[choice]

        with open("expenses.csv","w",newline="") as file:
            writer = csv.writer(file)
            for index,row in enumerate(reader):
                if index != choice:
                    writer.writerow(row)
        print(f"\nDeleted: {deleted_row}",end="")


main()
