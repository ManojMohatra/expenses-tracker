# 💰 Expense Tracker CLI


Expense Tracker CLI is a simple yet functional **command-line application** for recording, viewing, summarizing, deleting, and exporting personal expenses.  
It is written in **Python 3**, stores data in a **CSV file**, and works on any system with Python installed.

---

## ✨ Features
- 📌 Add new expense records (category, amount, date)
- 📊 View all expenses in a clean tabular format
- 📈 Summarize expenses by total, category, or date
- 🗑️ Delete expenses (last added or by row number)
- 💾 Export data to CSV or JSON for backup
- ✅ Input validation for dates and amounts

---

## 📂 Files in This Project
### `expenses_tracker.py`
Main script containing:
- `main()` – Menu loop and routing
- `add_new_entry()` – Add expenses
- `view_all_expenses()` – Display records
- `view_summary()` – Show summaries
- `delete_expense()` – Remove records
- `export()` – Save to CSV or JSON

### `expenses.csv`
Persistent storage with three columns:

---

## 🛠 Libraries Used
- `datetime` – Date validation
- `tabulate` – Pretty terminal tables
- `csv` – Read/write CSV files
- `os` – Screen clearing & file checks
- `collections.defaultdict` – Summarization
- `json` – JSON export

---

## 🚀 How to Run

```bash
# 1. Install Python 3 if not already installed
# 2. Install dependencies
pip install tabulate

# 3. Run the program
python expenses_tracker.py

