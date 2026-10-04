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
from collections import defaultdict

inp_invoice_file = "data/homework_invoices.csv"
oup_invoices = "data/invoices-output.csv"
HIGH_VALUE_THRESHOLD = 100000
oup_vendor_file = "data/vendor-total-output.csv"


def read_invoice(path):
    with open(path, newline="") as f:
        rows = list(csv.DictReader(f))
    for row in rows:
        row["amount"] = row["amount"].strip() or None
    return rows


def validate_invoice(invoice):
    """Return (amount, reason); amount is None when missing/invalid."""
    try:
        return float(invoice["amount"]), None
    except TypeError:
        return None, "amount is missing"
    except ValueError:
        return None, f"invalid amount '{invoice['amount']}'"


def get_approver(amount):
    if amount > 500000:
        return "Finance Controller"
    elif amount > 100000:
        return "Manager"
    else:
        return "Standard"


def calculate_total(invoices):
    totals = defaultdict(float)
    for invoice in invoices:
        vendor = invoice["vendor"] or "UNKNOWN"
        totals[vendor] += invoice["amount"]
    return totals


def write_output(path, rows, fieldnames):
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main():
    try:
        invoices = read_invoice(inp_invoice_file)
    except FileNotFoundError:
        print(f"File not found: {inp_invoice_file}")
        return

    high_value = []
    skipped = []
    for invoice in invoices:
        amount, reason = validate_invoice(invoice)
        if amount is None:
            skipped.append((invoice["invoice_id"], reason))
            continue
        if amount > HIGH_VALUE_THRESHOLD:
            invoice["amount"] = amount
            invoice["approver"] = get_approver(amount)
            high_value.append(invoice)
            print(invoice["invoice_id"], invoice["vendor"], amount, invoice["approver"])

    write_output(oup_invoices, high_value, ["invoice_id", "vendor", "amount", "status", "approver"])

    totals = calculate_total(high_value)
    write_output(
        oup_vendor_file,
        [{"vendor": v, "total": round(t, 2)} for v, t in sorted(totals.items())],
        ["vendor", "total"],
    )
    print(f"\n{len(high_value)} high-value invoices written to {oup_invoices}")

    print("\nGroup totals by vendor")
    for vendor, total in sorted(totals.items()):
        print(f"{vendor}: {total:,.2f}")

    print(f"\nSkipped invoices ({len(skipped)})")
    for invoice_id, reason in skipped:
        print(f"{invoice_id}: {reason}")


main()