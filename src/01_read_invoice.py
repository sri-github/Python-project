# Please use the shared homework_invoices.csv file and complete the following task.

# 1. Create a Python program named:
#    01_read_invoice.py

# 2. Read all invoice records from the given CSV file using Python.

# 3. For each invoice, read and check the following details:
#    - Vendor
#    - Amount
#    - Status

# 4. Check the invoice amount:
#    - Identify invoices where the amount is greater than 100,000.
#    - Identify missing or invalid amount values.

# 5. Use try / except to handle invalid amount values so that the program continues processing the remaining records.

# 6. Print a simple summary at the end:
#    - Total invoices read
#    - Number of invoices greater than 100,000
#    - Number of invoices with missing/invalid amount

# Expected Flow:

# Read CSV → Read Each Invoice → Check Amount → Handle Invalid Data → Print Summary
import csv

inp_invoice_file = "data/homework_invoices.csv"
HIGH_VALUE_THRESHOLD = 100000


def read_invoices(path):
    with open(path, newline="") as f:
        return list(csv.DictReader(f))


def validate_amount(amount):
    try:
        return float(amount)
    except (TypeError, ValueError):
        return None


def main():
    try:
        invoices = read_invoices(inp_invoice_file)
    except FileNotFoundError:
        print(f"File not found: {inp_invoice_file}")
        return

    total_invoices = 0
    high_value_invoices = 0
    invalid_amounts = 0

    for invoice in invoices:
        total_invoices += 1

        vendor = invoice.get("vendor", "")
        amount = invoice.get("amount", "")
        status = invoice.get("status", "")

        print(
            f"Vendor: {vendor}, "
            f"Amount: {amount}, "
            f"Status: {status}"
        )

        amount_value = validate_amount(amount)

        if amount_value is None:
            invalid_amounts += 1
            print("  -> Invalid or missing amount")
            continue

        if amount_value > HIGH_VALUE_THRESHOLD:
            high_value_invoices += 1
            print("  -> Amount greater than 100,000")

    print("\n===== SUMMARY =====")
    print(f"Total invoices read: {total_invoices}")
    print(f"Invoices greater than 100,000: {high_value_invoices}")
    print(f"Invoices with missing/invalid amount: {invalid_amounts}")


main()