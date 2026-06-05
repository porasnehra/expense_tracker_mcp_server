"""
Expense Tracker Module - Core business logic
Clean and testable implementation
"""

# In-memory expense storage
expenses = []


def add_expense(description: str, amount: float, category: str = "General") -> dict:
    """
    Add a new expense to the tracker.
    
    Args:
        description: Brief description of the expense
        amount: Amount spent (positive number)
        category: Category of expense (default: "General")
    
    Returns:
        Dictionary with expense details and id
    """
    if amount <= 0:
        return {"error": "Amount must be greater than 0"}
    
    expense = {
        "id": len(expenses) + 1,
        "description": description,
        "amount": amount,
        "category": category,
    }
    expenses.append(expense)
    return {"success": True, "expense": expense}


def remove_expense(expense_id: int) -> dict:
    """
    Remove an expense by its ID.
    
    Args:
        expense_id: ID of the expense to remove
    
    Returns:
        Dictionary with success status and removed expense details
    """
    global expenses
    for i, expense in enumerate(expenses):
        if expense["id"] == expense_id:
            removed = expenses.pop(i)
            return {"success": True, "removed": removed}
    
    return {"error": f"Expense with ID {expense_id} not found"}


def get_summary() -> dict:
    """
    Get a summary of all expenses.
    
    Returns:
        Dictionary with total amount, count, and breakdown by category
    """
    if not expenses:
        return {
            "total": 0,
            "count": 0,
            "by_category": {},
            "expenses": []
        }
    
    total = sum(e["amount"] for e in expenses)
    by_category = {}
    
    for expense in expenses:
        category = expense["category"]
        by_category[category] = by_category.get(category, 0) + expense["amount"]
    
    return {
        "total": round(total, 2),
        "count": len(expenses),
        "by_category": {k: round(v, 2) for k, v in by_category.items()},
        "expenses": expenses
    }


def get_all_expenses() -> dict:
    """Get all tracked expenses."""
    return {
        "count": len(expenses),
        "expenses": expenses
    }


def clear_all_expenses() -> dict:
    """Clear all expenses (useful for testing)."""
    global expenses
    expenses = []
    return {"success": True, "message": "All expenses cleared"}
