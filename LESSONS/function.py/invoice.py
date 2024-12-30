def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount} is due: {due_date}")
    print()


display_invoice("William Dugell", 34.04, "03.04.2025")
display_invoice("Donald Suer", 53.35, "07.04.2027")
# display_invoice("Donald Suer 07.04.2027") --> mistake
