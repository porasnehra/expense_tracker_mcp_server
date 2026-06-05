"""
FastMCP Expense Tracker Server
Exposes expense tracking functionality as MCP tools
"""

from fastmcp import FastMCP
from expense_tracker import (
    add_expense,
    remove_expense,
    get_summary,
    get_all_expenses,
    clear_all_expenses
)

# Initialize FastMCP server
mcp = FastMCP("Expense Tracker Server")


# ============ MCP TOOLS ============

@mcp.tool
def add_expense_tool(description: str, amount: float, category: str = "General") -> dict:
    """Add a new expense to tracker.
    
    Args:
        description: Brief description of the expense
        amount: Amount spent (must be > 0)
        category: Category of expense (e.g., Food, Transport, Entertainment)
    
    Returns:
        Success response with expense details
    """
    return add_expense(description, amount, category)


@mcp.tool
def remove_expense_tool(expense_id: int) -> dict:
    """Remove an expense by ID.
    
    Args:
        expense_id: The ID of the expense to remove
    
    Returns:
        Success response with removed expense details
    """
    return remove_expense(expense_id)


@mcp.tool
def summarize_expenses() -> dict:
    """Get expense summary with total, count, and category breakdown.
    
    Returns:
        Summary including total amount, expense count, and breakdown by category
    """
    return get_summary()


@mcp.tool
def list_all_expenses() -> dict:
    """List all expenses.
    
    Returns:
        All tracked expenses with their details
    """
    return get_all_expenses()


@mcp.tool
def clear_expenses() -> dict:
    """Clear all expenses (useful for testing/resetting).
    
    Returns:
        Confirmation message
    """
    return clear_all_expenses()


if __name__ == "__main__":
    mcp.run()
