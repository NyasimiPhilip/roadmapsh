import argparse
import json
from datetime import datetime

EXPENSE_FILE = 'expenses.json'

# Load existing expenses from file
def load_expenses():
    try:
        with open(EXPENSE_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save expenses to file
def save_expenses(expenses):
    with open(EXPENSE_FILE, 'w') as file:
        json.dump(expenses, file, indent=4)

# Add an expense with category and currency
def add_expense(description, amount, category=None, currency=None, conversion_rate=1.0):
    expenses = load_expenses()
    expense_id = len(expenses) + 1
    converted_amount = amount * conversion_rate
    expense = {
        'id': expense_id,
        'date': datetime.now().strftime('%Y-%m-%d'),
        'description': description,
        'amount': round(converted_amount, 2),
        'category': category if category else 'General',  # Default category if not provided
        'currency': currency if currency else 'USD',  # Default currency if not provided
        'original_amount': round(amount, 2)
    }
    expenses.append(expense)
    save_expenses(expenses)
    print(f"Expense added successfully (ID: {expense_id})")

# List all expenses
def list_expenses():
    expenses = load_expenses()
    if not expenses:
        print("No expenses found.")
        return
    
    print(f"{'ID':<4} {'Date':<12} {'Description':<15} {'Category':<12} {'Amount':<8} {'Currency':<8}")
    for expense in expenses:
        print(f"{expense['id']:<4} {expense['date']:<12} {expense['description']:<15} {expense['category']:<12} ${expense['amount']:<8} ({expense['currency']})")

# Show summary of total expenses and breakdown by category
def show_summary(month=None):
    expenses = load_expenses()
    total = 0
    category_totals = {}

    for expense in expenses:
        if month:
            if int(expense['date'].split('-')[1]) == month:
                total += expense['amount']
                category_totals[expense['category']] = category_totals.get(expense['category'], 0) + expense['amount']
        else:
            total += expense['amount']
            category_totals[expense['category']] = category_totals.get(expense['category'], 0) + expense['amount']

    if month:
        print(f"Total expenses for month {month}: ${total}")
    else:
        print(f"Total expenses: ${total}")
    
    print("\nCategory breakdown:")
    for category, total in category_totals.items():
        print(f"{category}: ${total}")

# Delete an expense by ID
def delete_expense(expense_id):
    expenses = load_expenses()
    new_expenses = [exp for exp in expenses if exp['id'] != expense_id]
    save_expenses(new_expenses)
    print(f"Expense deleted successfully")

# Edit an expense by ID
def edit_expense(expense_id, description=None, amount=None, category=None, currency=None, conversion_rate=1.0):
    expenses = load_expenses()
    for expense in expenses:
        if expense['id'] == expense_id:
            if description:
                expense['description'] = description
            if amount is not None:  # Check if amount is provided
                expense['original_amount'] = amount
                expense['amount'] = round(amount * conversion_rate, 2)
            if category:
                expense['category'] = category
            if currency:
                expense['currency'] = currency
            save_expenses(expenses)
            print(f"Expense {expense_id} updated successfully")
            return
    print(f"Expense with ID {expense_id} not found")

# Search expenses by description or category
def search_expenses(keyword):
    expenses = load_expenses()
    results = [exp for exp in expenses if keyword.lower() in exp['description'].lower() or keyword.lower() in exp['category'].lower()]
    
    if not results:
        print(f"No expenses found matching '{keyword}'.")
        return

    print(f"Search results for '{keyword}':")
    print(f"{'ID':<4} {'Date':<12} {'Description':<15} {'Category':<12} {'Amount':<8} {'Currency':<8}")
    for expense in results:
        print(f"{expense['id']:<4} {expense['date']:<12} {expense['description']:<15} {expense['category']:<12} ${expense['amount']:<8} ({expense['currency']})")

# Argument parser
def main():
    parser = argparse.ArgumentParser(description="Expense Tracker")

    subparsers = parser.add_subparsers(dest='command')

    # Add command
    add_parser = subparsers.add_parser('add', help='Add an expense')
    add_parser.add_argument('--description', required=True, help='Description of the expense')
    add_parser.add_argument('--amount', required=True, type=float, help='Amount of the expense')
    add_parser.add_argument('--category', help='Category of the expense (e.g., food, travel)')  # Made optional
    add_parser.add_argument('--currency', help='Currency of the expense (e.g., USD, EUR)')  # Made optional
    add_parser.add_argument('--conversion-rate', type=float, default=1.0, help='Conversion rate to base currency (default: 1)')

    # List command
    subparsers.add_parser('list', help='List all expenses')

    # Summary command
    summary_parser = subparsers.add_parser('summary', help='Show total expenses')
    summary_parser.add_argument('--month', type=int, help='Show total expenses for a specific month')

    # Delete command
    delete_parser = subparsers.add_parser('delete', help='Delete an expense')
    delete_parser.add_argument('--id', required=True, type=int, help='ID of the expense to delete')

    # Edit command
    edit_parser = subparsers.add_parser('edit', help='Edit an expense')
    edit_parser.add_argument('--id', required=True, type=int, help='ID of the expense to edit')
    edit_parser.add_argument('--description', help='New description of the expense')
    edit_parser.add_argument('--amount', type=float, help='New amount of the expense')
    edit_parser.add_argument('--category', help='New category of the expense')
    edit_parser.add_argument('--currency', help='New currency of the expense')
    edit_parser.add_argument('--conversion-rate', type=float, default=1.0, help='Conversion rate to base currency (default: 1)')

    # Search command
    search_parser = subparsers.add_parser('search', help='Search expenses by description or category')
    search_parser.add_argument('--keyword', required=True, help='Keyword to search for in description or category')

    args = parser.parse_args()

    if args.command == 'add':
        if args.amount < 0:
            print("Amount cannot be negative")
        else:
            add_expense(args.description, args.amount, args.category, args.currency, args.conversion_rate)
    elif args.command == 'list':
        list_expenses()
    elif args.command == 'summary':
        show_summary(args.month)
    elif args.command == 'delete':
        delete_expense(args.id)
    elif args.command == 'edit':
        edit_expense(args.id, args.description, args.amount, args.category, args.currency, args.conversion_rate)
    elif args.command == 'search':
        search_expenses(args.keyword)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
