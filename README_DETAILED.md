# Expense Tracker MCP Server

A clean and easy-to-understand expense tracker built with FastMCP with features for adding, removing, and summarizing expenses.

## 📁 Project Structure

```
.
├── expense_tracker.py    # Core business logic (testable functions)
├── main.py               # FastMCP server (MCP tools)
├── test.py               # Comprehensive test suite
├── pyproject.toml        # Project configuration
└── README.md             # This file
```

## 🎯 Core Features

### 1. **Add Expense** (`add_expense`)
Add a new expense with description, amount, and category.
- **Parameters**: 
  - `description` (str): What was spent on
  - `amount` (float): Amount spent (must be > 0)
  - `category` (str): Expense category (default: "General")
- **Returns**: Success response with expense details and ID

### 2. **Remove Expense** (`remove_expense`)
Remove an expense by its ID.
- **Parameters**: 
  - `expense_id` (int): The ID of expense to remove
- **Returns**: Removed expense details or error message

### 3. **Summarize Expenses** (`get_summary`)
Get a complete summary of all expenses.
- **Returns**: 
  - `total`: Total amount spent
  - `count`: Number of expenses
  - `by_category`: Breakdown by category
  - `expenses`: List of all expenses

### 4. **List All Expenses** (`get_all_expenses`)
View all tracked expenses.

### 5. **Clear Expenses** (`clear_all_expenses`)
Remove all expenses (useful for testing).

## 💻 Architecture

### Clean Separation of Concerns

**`expense_tracker.py`** - Pure Business Logic
- No FastMCP dependencies
- Easily testable
- Can be imported and used anywhere
- Functions: `add_expense`, `remove_expense`, `get_summary`, `get_all_expenses`, `clear_all_expenses`

**`main.py`** - FastMCP Server
- Exposes business logic as MCP tools
- Each tool wraps a core function
- Clean documentation for each tool

**`test.py`** - Test Suite
- Tests all core functionality
- Easy to understand
- Comprehensive coverage (9 test scenarios)

## 🧪 Running Tests

```bash
# Activate virtual environment (if needed)
source .venv/bin/activate  # Unix/Mac
.\.venv\Scripts\activate   # Windows

# Run tests
python test.py
```

Expected output:
```
==================================================
Running Expense Tracker Tests
==================================================
✓ Test 1: Add expense with category
✓ Test 2: Add expense with default category
✓ Test 3: Reject negative amount
✓ Test 4: Remove expense successfully
✓ Test 5: Handle removing non-existent expense
✓ Test 6: Summary calculation correct
✓ Test 7: List all expenses
✓ Test 8: Clear all expenses
✓ Test 9: Complete workflow
==================================================
✅ All tests passed!
==================================================
```

## 🚀 Running the MCP Server

```bash
python main.py
```

This will start the FastMCP server exposing the following tools:
- `add_expense_tool` - Add a new expense
- `remove_expense_tool` - Remove an expense
- `summarize_expenses` - Get expense summary
- `list_all_expenses` - List all expenses
- `clear_expenses` - Clear all expenses

## 📝 Usage Example

```python
from expense_tracker import (
    add_expense,
    remove_expense,
    get_summary,
    clear_all_expenses
)

# Clear for fresh start
clear_all_expenses()

# Add some expenses
add_expense("Coffee", 5.50, "Food")
add_expense("Bus ticket", 2.00, "Transport")
add_expense("Movie", 10.00, "Entertainment")

# Get summary
summary = get_summary()
print(f"Total spent: ${summary['total']}")
print(f"By category: {summary['by_category']}")
# Output:
# Total spent: $17.5
# By category: {'Food': 5.5, 'Transport': 2.0, 'Entertainment': 10.0}

# Remove an expense
remove_expense(1)

# Check updated summary
summary = get_summary()
print(f"Total after removing: ${summary['total']}")
```

## 🛠️ Development

### Adding a New Feature

1. Add the core logic to `expense_tracker.py`
2. Add tests in `test.py`
3. Run `python test.py` to verify
4. Wrap it as an MCP tool in `main.py`

### Example: Adding a "Get By Category" Feature

```python
# In expense_tracker.py
def get_expenses_by_category(category: str) -> dict:
    """Get all expenses for a specific category"""
    filtered = [e for e in expenses if e["category"] == category]
    return {
        "category": category,
        "count": len(filtered),
        "total": round(sum(e["amount"] for e in filtered), 2),
        "expenses": filtered
    }

# In main.py
@mcp.tool
def get_by_category(category: str) -> dict:
    """Get expenses by category"""
    return get_expenses_by_category(category)
```

## 📊 Data Structure

Each expense is stored as a dictionary:
```python
{
    "id": 1,
    "description": "Coffee",
    "amount": 5.50,
    "category": "Food"
}
```

## ✨ Key Design Principles

1. **Simplicity** - Easy to read and understand
2. **Testability** - Business logic separated from MCP layer
3. **Clean Code** - No unnecessary complexity
4. **Extensibility** - Easy to add new features
5. **Documentation** - Well-documented functions and tests

## 📦 Dependencies

- `fastmcp>=3.4.0` - MCP server framework

## License

MIT
