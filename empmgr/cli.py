from .storage import load_employees
from .validators import parse_salary
from .models import add_employee
from .storage import save_employees

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


if __name__ == "__main__":
   main()