from .storage import load_employees
from .validators import parse_salary
from .models import add_employee
from .storage import save_employees
from rich.console import Console
from rich.table import Table

def main():
 employees = load_employees()
 while True:
  print("\n=== Employee Manager ===")
  print("1. List employees")
  print("2. Add employee")
  print("3. Quit")
  choice = input("Choose an option: ").strip()
  if choice == "1":
     for e in employees:
      print(e["id"], e["name"], e["department"], e["salary"])
  elif choice == "2":
       name = input("Name: ").strip()
       email = input("Email: ").strip()
       department = input("Department: ").strip()
       salary = parse_salary(input("Salary: "))
       if not name or salary is None:
         print("Invalid input - employee not added.")
         continue
       add_employee(employees, name, email, department, salary)
       save_employees(employees)
  elif choice == "3":
     break
  else:
   print("Invalid option.")



def show_employees() -> None:
 table = Table(title="Employees")
 for col in ("ID", "Name", "Department", "Salary"):
  table.add_column(col)
 for emp in load_employees():
  table.add_row(str(emp["id"]), emp["name"],
 emp["department"], f"{emp['salary']:,.2f}")
 Console().print(table)


if __name__ == "__main__":
    main()
    show_employees()