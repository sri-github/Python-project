invoice_amt = 60000
# invoice_approver

# invoice_amount = 50000
# invoice_approver => Manager / Supervisor / Director

#  amount < 1000 -> Sup
#  amount > 25000 -> Manager 
#  amount > 50000 -> Manager and Director

# 1) Write python program using if condition block and convert to match case
# 2) List of employee id, name, salary and then print only those names with length > 6 and salary < 250000

if invoice_amt < 1000:
    print("Invoice approver is Supervisor")
elif invoice_amt > 25000 and invoice_amt <= 50000:
    print("Invoice approver is Manager")
else:
    print("Invoice approver is Manager and Director")

match invoice_amt:
    case amt if amt < 1000:
        print("Invoice approver is Supervisor")
    case amt if amt > 25000 and amt <= 50000:
        print("Invoice approver is Manager")
    case _:
        print("Invoice approver is Manager and Director")
    