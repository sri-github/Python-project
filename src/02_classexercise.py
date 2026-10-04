
# invoice_amount = 50000
# invoice_approver => Manager / Supervisor / Director

#  amount < 1000 -> Sup
#  amount > 25000 -> Manager 
#  amount > 50000 -> Manager and Director

# 1) Write python program using if condition block and convert to match case
# 2) List of employee id, name, salary and then print only those names with length > 6 and salary < 250000

employees = [
    {"id": 1, "name": "John Smith", "salary": 200000},
    {"id": 2, "name": "Jane Doe", "salary": 300000},
    {"id": 3, "name": "Michael Johnson", "salary": 150000},
    {"id": 4, "name": "Emily Davis", "salary": 250000},
    {"id": 5, "name": "William Brown", "salary": 180000},
    {"id": 6, "name": "Olivia Wilson", "salary": 220000},
    {"id": 7, "name": "James Taylor", "salary": 280000},
    {"id": 8, "name": "Sophia Anderson", "salary": 240000},
    {"id": 9, "name": "Benjamin Thomas", "salary": 260000},
    {"id": 10, "name": "Ava Martinez", "salary": 190000}
]

# Print names with length > 6 and salary < 250000
for employee in employees:
    if len(employee["name"]) > 6 and employee["salary"] < 250000:
        print(employee["name"])
        