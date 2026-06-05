"""
Test suite for Expense Tracker
Demonstrates how to use the expense tracker functionality
"""

from expense_tracker import (
    add_expense,
    remove_expense,
    get_summary,
    get_all_expenses,
    clear_all_expenses
)


def test_add_expense():
    """Test adding expenses"""
    clear_all_expenses()
    
    # Add first expense
    result1 = add_expense("Coffee", 5.50, "Food")
    assert result1["success"] == True
    assert result1["expense"]["description"] == "Coffee"
    assert result1["expense"]["amount"] == 5.50
    assert result1["expense"]["category"] == "Food"
    print("✓ Test 1: Add expense with category")
    
    # Add second expense with default category
    result2 = add_expense("Bus ticket", 2.0)
    assert result2["success"] == True
    assert result2["expense"]["category"] == "General"
    print("✓ Test 2: Add expense with default category")
    
    # Test invalid amount
    result3 = add_expense("Invalid", -10)
    assert "error" in result3
    print("✓ Test 3: Reject negative amount")


def test_remove_expense():
    """Test removing expenses"""
    clear_all_expenses()
    
    # Add and remove an expense
    add_result = add_expense("Movie tickets", 15.00, "Entertainment")
    expense_id = add_result["expense"]["id"]
    
    remove_result = remove_expense(expense_id)
    assert remove_result["success"] == True
    assert remove_result["removed"]["description"] == "Movie tickets"
    print("✓ Test 4: Remove expense successfully")
    
    # Try to remove non-existent expense
    result = remove_expense(999)
    assert "error" in result
    print("✓ Test 5: Handle removing non-existent expense")


def test_get_summary():
    """Test summary calculation"""
    clear_all_expenses()
    
    # Add multiple expenses
    add_expense("Coffee", 5.50, "Food")
    add_expense("Lunch", 12.00, "Food")
    add_expense("Taxi", 8.00, "Transport")
    add_expense("Movie", 10.00, "Entertainment")
    
    summary = get_summary()
    
    assert summary["count"] == 4
    assert summary["total"] == 35.50
    assert summary["by_category"]["Food"] == 17.50
    assert summary["by_category"]["Transport"] == 8.00
    assert summary["by_category"]["Entertainment"] == 10.00
    print("✓ Test 6: Summary calculation correct")


def test_get_all_expenses():
    """Test getting all expenses"""
    clear_all_expenses()
    
    # Add expenses
    add_expense("Milk", 3.00, "Grocery")
    add_expense("Bread", 2.50, "Grocery")
    
    all_expenses = get_all_expenses()
    
    assert all_expenses["count"] == 2
    assert len(all_expenses["expenses"]) == 2
    print("✓ Test 7: List all expenses")


def test_clear_expenses():
    """Test clearing all expenses"""
    add_expense("Something", 100, "Test")
    
    result = clear_all_expenses()
    assert result["success"] == True
    
    summary = get_summary()
    assert summary["count"] == 0
    assert summary["total"] == 0
    print("✓ Test 8: Clear all expenses")


def test_workflow():
    """Test a complete workflow"""
    clear_all_expenses()
    
    # Month 1: Add various expenses
    add_expense("Lunch", 10.00, "Food")
    add_expense("Snacks", 5.00, "Food")
    add_expense("Train pass", 50.00, "Transport")
    add_expense("Movie", 12.00, "Entertainment")
    
    # Check summary
    summary1 = get_summary()
    assert summary1["count"] == 4
    assert summary1["total"] == 77.00
    
    # Remove one expense
    all_exp = get_all_expenses()
    first_id = all_exp["expenses"][0]["id"]
    remove_expense(first_id)
    
    # Check updated summary
    summary2 = get_summary()
    assert summary2["count"] == 3
    
    print("✓ Test 9: Complete workflow")


def run_all_tests():
    """Run all tests"""
    print("\n" + "="*50)
    print("Running Expense Tracker Tests")
    print("="*50 + "\n")
    
    try:
        test_add_expense()
        test_remove_expense()
        test_get_summary()
        test_get_all_expenses()
        test_clear_expenses()
        test_workflow()
        
        print("\n" + "="*50)
        print("✅ All tests passed!")
        print("="*50 + "\n")
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}\n")
        raise


if __name__ == "__main__":
    run_all_tests()
