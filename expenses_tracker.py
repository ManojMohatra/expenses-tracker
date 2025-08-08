from datetime import datetime
from tabulate import tabulate
import csv
import os 
from collections import defaultdict
import sys
import json
# Using 'wait()' after each action to pause before returning to main menu

def main():
    ensure_csv_file()  
    while True:
        # Clear terminal screen
        os.system("cls" if os.name == "nt" else "clear")

        print("\nWelcome to expenses tracker!\n")
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
        elif choice == "5":
            export()
        elif choice == "6":
            print("Thanks for using the app.")
            break
        else:
            print("Invalid Choice")
            wait()

    


def add_new_entry():
    category = input("Category(Food,Rent,Tution,Misc,...):").strip().lower()
    try:
        expense = float(input("Expense(Amount):").strip())
    except ValueError:
        print("Invalid expense amount.Please Enter a number")
        wait()
        return
    date = input("Date(Format:YYYY-MM-DD(Leave it empty to set the date to now):").strip()
    print("")

    # Default to today's date if user leaves input empty
    if not date:
        date = datetime.now().strftime("%Y-%m-%d")

    # Validate date format — prevents garbage from being written
    try:
        datetime.strptime(date,"%Y-%m-%d")
    except ValueError:
        print("Invalid date.Please use YYYY-MM-DD(eg., 2025-02-03)")
        wait()
        return 

    with open("expenses.csv",mode="a",newline="") as file:
        writer  = csv.writer(file)
        writer.writerow([category,expense,date])

    print(f"Added: {category} | {expense} | {date}",end="")
    wait() 


def ensure_csv_file():
    # Create file and header only if it doesn't already exist
    filename = "expenses.csv"
    if not os.path.isfile(filename):
        with open(filename,mode="w",newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["category","expense","date"])

def view_all_expenses():
    with open("expenses.csv","r") as file:
        reader = csv.reader(file)
        # Skip header row so it's not duplicated in data
        headers = next(reader)

        data = list(reader)
        if not data:
            print("No expenses to show")
        else:
            print(tabulate(data, headers=headers,tablefmt='psql'))
    wait()

def view_summary():
    # User selects summary type; next few functions handles logic
    print("View Summary:\n")
    print("1. Total Expenses")
    print("2. Expense by category")
    print("3. Print Expense by date\n")

    choice  = input("What do you want to do? ").strip()
    print("")

    if choice == "1":
        print(f"The total expenses up to this point is:{total_expenses()}")
        wait()
    elif choice  == "2":
        print_summary(calc_by_field("category"),["Category","Total"])
    elif choice == "3":
        print_summary(calc_by_field("date"),["Date","Total"])
    else:
        print("Invalid choice")
        wait()

def total_expenses(filename="expenses.csv"):
    with open(filename,"r") as file:
        reader = csv.DictReader(file)
        total = 0
        for row in reader:
            total += float(row["expense"])
    return total 


def calc_by_field(field,filename="expenses.csv"):
    totals = defaultdict(float)
    with open(filename,"r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            field_now = row[field]
            amount = float(row["expense"])
            totals[field_now] += amount
    return totals

def print_summary(data,headers):
    print(tabulate(data.items(),headers=headers,tablefmt="psql"))
    wait()

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
            wait()
        
    elif choice == "2":
       # Read all rows into memory to allow deletion by index
       for index,row in enumerate(reader):
                print(f"\nRow:{index} {row}")
       try:
            index = int(input("\nWhich row do you want do you want to delete? ").strip())
            # Prevent deleting header or non-existent row
            if index >= len(reader) or index == 0:
                print("Invalid row number(0 is a header)")
                wait()
                return
       
            delete_row(index,reader)
       except ValueError:
            print("Invalid input.Please enter a valid number.")
            wait()
            return
            
       
             

def delete_row(choice, reader, testing=False):
    choice = int(choice)
    deleted_row = reader[choice]
    updated_rows = [row for index, row in enumerate(reader) if index != choice]
    
    print(f"\nDeleted: {deleted_row}", end="")
    
    if not testing:
        with open("expenses.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(updated_rows)
        wait()
    
    return updated_rows, deleted_row  

def export():
    print("1.Export as CSV")
    print("2.Export as JSON")
    
    choice = input("\nWhat do you want to do? ").strip()
    correct_choice=["1","2"]
    if choice  not in correct_choice:
            print("Invalid choice")
            wait()
            return              
    export_filename = input("What do you want your filename as? ").strip() 
    source_file = "expenses.csv"

    # Prevent accidental overwrite of existing export files
    if os.path.exists(export_filename + ".csv") or os.path.exists(export_filename + ".json"):
        overwrite = input("File exists. Overwrite? (y/n): ").strip().lower()
        if overwrite != "y":
            print("Cancelled export.")
            wait()
            return

    if  not export_filename.strip():
        print("Filename cannot be empty.")
        wait()
        return
    if choice == "1":
            export_csv(export_filename)
            print("Export Sucessfull!")
            wait()
    else:
        export_json(export_filename) 
        print("Export Sucessfull!")
        wait()
            
def export_csv(export_filename):
    with open("expenses.csv", "r", newline="") as source, open(export_filename + ".csv", "w", newline="") as export:
        export.write(source.read())           

def export_json(export_filename):
    data = []
    with open("expenses.csv", "r", encoding="utf-8") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data.append(row)
    with open(export_filename + ".json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

def wait():
    input("\nPress any key to return to main menu...")

if __name__ == "__main__":    
    main()
