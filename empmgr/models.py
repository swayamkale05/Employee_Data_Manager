def add_employee(employees, name, email, department, salary):
 next_id = max((e["id"] for e in employees), default=0) + 1
 employees.append({"id": next_id, "name": name, "email": email,
 "department": department, "salary": salary})