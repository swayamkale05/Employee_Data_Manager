import re


def parse_salary(text):
 try:
  return float(text)
 except ValueError:
  return None


def validate_employee(salary, email):
    errors = []

    if salary < 0:
        errors.append("Salary cannot be negative.")

    email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    if not re.match(email_pattern, email):
        errors.append("Malformed email address.")

    return errors or ["Valid"]