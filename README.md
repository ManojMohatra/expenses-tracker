# Expense Tracker CLI
#### Video Demo: https://www.youtube.com/watch?v=dqlwQlPJHFQ
#### Description:

Expense Tracker CLI is a simple yet functional command-line application for recording, viewing, summarizing, deleting, and exporting personal expenses. It is written entirely in Python and stores all data persistently in a CSV file, allowing the user to manage expenses across multiple sessions. The project is designed to be lightweight, portable, and usable on any system with Python 3 installed.

This program allows a user to:
- Add new expense records with a category, amount, and date.
- View all expenses in a tabular format.
- View summaries of expenses, such as total expenses, totals by category, and totals by date.
- Delete expenses, either the most recently added or a specific one by row number.
- Export stored expenses to CSV or JSON format for backup or external use.

All features are accessible from a text-based menu interface. The program ensures valid input formats for numbers and dates, and it prevents common user errors such as overwriting files accidentally or entering invalid row numbers when deleting.

---

## Files in This Project

**`project.py`**  
This is the main Python script that contains the entire logic of the application. It is organized into functions for each action:
- `main()` — Displays the menu, routes user input to the correct feature.
- `add_new_entry()` — Prompts the user for category, expense amount, and date, then stores the record in `expenses.csv`.
- `ensure_csv_file()` — Creates `expenses.csv` with a header if it doesn’t already exist.
- `view_all_expenses()` — Displays all recorded expenses in a neatly formatted table using the `tabulate` library.
- `view_summary()` — Shows summaries based on total expenses, category totals, or date totals.
- `total_expenses()` — Calculates the sum of all recorded expenses.
- `calc_by_field()` — Groups expenses by either category or date and calculates totals.
- `print_summary()` — Displays summary data in a table format.
- `delete_expense()` — Allows deletion of either the last added expense or a specific expense by row index.
- `delete_row()` — Removes the chosen row from the CSV and updates the file.
- `export()` — Provides an option to export data as either CSV or JSON.
- `export_csv()` — Copies `expenses.csv` to a new CSV file.
- `export_json()` — Converts `expenses.csv` to a JSON file with proper formatting.
- `wait()` — Pauses until the user presses a key, used after each action for better UX.

**`expenses.csv`** 

The persistent data storage file for this program. It contains three columns:  
`category`, `expense`, `date`. The first row is always the header.

---

## Libraries Used
- `datetime` — For date validation and default date generation.
- `tabulate` — For cleanly formatted tables in the terminal.
- `csv` — For reading and writing CSV files.
- `os` — For clearing the screen and checking file existence.
- `collections.defaultdict` — For easy aggregation of totals.
- `sys` and `json` — For JSON export and potential future enhancements.

---

## Design Choices

1. **CSV as Primary Storage**  
   I chose CSV because it is lightweight, human-readable, and easy to manipulate both in code and manually if necessary. It also integrates well with Python’s built-in `csv` module.

2. **Tabulate for Formatting**  
   While printing tables manually is possible, using `tabulate` drastically improves readability and gives the program a professional appearance without extra complexity.

3. **Menu-Driven CLI**  
   The program runs in a loop with a numbered menu so the user can perform multiple operations without restarting the script.

4. **Error Handling**  
   The program validates numerical input for expenses and checks that dates are in the `YYYY-MM-DD` format. Deleting expenses includes safeguards against deleting the header or non-existent rows.

5. **Single File Implementation**  
   For simplicity in submission and running, all logic is contained in a single file, though in a larger project it could be split into modules.

---

## How to Run

1. Install Python 3 if not already installed.
2. Install the `tabulate` library:  
   ```bash
   pip install tabulate
3. Place project.py in your desired folder.

4. Run the program:
    python project.py

5. Follow the on-screen menu prompts.


