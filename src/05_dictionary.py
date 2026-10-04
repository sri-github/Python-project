invoice = {
    "invoice_number": "INV-001",
    "customer_name": "John Doe",
    "amount": 100.00
}
print(f"Invoice Number: {invoice['invoice_number']}")
print(f"Customer Name: {invoice['customer_name']}")
print(f"Invoice Amount: ${invoice['amount']:.2f}")