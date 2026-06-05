# Quick Start Guide - Expense Tracker

## 📦 File Overview

| File | Purpose |
|------|---------|
| `expense_tracker.py` | Core functions - pure Python, no dependencies |
| `main.py` | FastMCP server wrapper |
| `test.py` | Tests and usage examples |

## ⚡ Quick Commands

```bash
# Run all tests
python test.py

# Start MCP server
python main.py
```

## 🔧 Core Functions

### Add Expense
```python
from expense_tracker import add_expense

result = add_expense("Coffee", 5.50, "Food")
# Returns: {"success": True, "expense": {"id": 1, ...}}
```

### Remove Expense
```python
from expense_tracker import remove_expense

result = remove_expense(1)  # Remove expense with ID 1
# Returns: {"success": True, "removed": {...}}
```

### Get Summary
```python
from expense_tracker import get_summary

summary = get_summary()
# Returns: {
#   "total": 77.00,
#   "count": 4,
#   "by_category": {"Food": 17.50, "Transport": 8.00, ...},
#   "expenses": [...]
# }
```

### List All Expenses
```python
from expense_tracker import get_all_expenses

all_exp = get_all_expenses()
# Returns: {"count": 4, "expenses": [...]}
```

### Clear All
```python
from expense_tracker import clear_all_expenses

clear_all_expenses()
```

## 📋 Example Workflow

```python
from expense_tracker import *

# Start fresh
clear_all_expenses()

# Track daily expenses
add_expense("Breakfast", 8.00, "Food")
add_expense("Bus pass", 50.00, "Transport")
add_expense("Dinner", 15.00, "Food")

# See what you spent
summary = get_summary()
print(f"Total: ${summary['total']}")
print(f"By Category: {summary['by_category']}")
# Output: Total: $73.0, By Category: {'Food': 23.0, 'Transport': 50.0}

# Made a mistake? Remove it
all_exp = get_all_expenses()
remove_expense(all_exp['expenses'][0]['id'])
```

## ✅ Test Coverage

- ✓ Add with category
- ✓ Add with default category
- ✓ Reject negative amounts
- ✓ Remove by ID
- ✓ Handle missing ID
- ✓ Summary calculation
- ✓ List all expenses
- ✓ Clear all expenses
- ✓ Complete workflow

All tests pass! ✅
