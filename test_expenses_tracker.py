import csv
import os
import pytest
from expenses_tracker import calc_by_field, total_expenses, delete_row

TEST_CSV = "test_expenses.csv"

@pytest.fixture
def setup_test_csv():
    # Create test CSV file
    rows = [
        ["category", "expense", "date"],
        ["food", "10", "2025-08-01"],
        ["rent", "200", "2025-08-01"],
        ["food", "15", "2025-08-02"],
    ]
    with open(TEST_CSV, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    yield
    os.remove(TEST_CSV)

def test_calc_by_field(setup_test_csv):
    result = calc_by_field("category", filename=TEST_CSV)
    assert result == {"food": 25.0, "rent": 200.0}

def test_total_expenses(setup_test_csv):
    total = total_expenses(filename=TEST_CSV)
    assert total == 225.0

def test_delete_row():
    rows = [
        ["category", "expense", "date"],
        ["food", "10", "2025-08-01"],
        ["rent", "200", "2025-08-01"],
        ["food", "15", "2025-08-02"],
    ]
    updated, deleted = delete_row(2, rows,testing=True)
    assert deleted == ["rent", "200", "2025-08-01"]
    assert updated == [
        ["category", "expense", "date"],
        ["food", "10", "2025-08-01"],
        ["food", "15", "2025-08-02"],
    ]

