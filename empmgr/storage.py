import json
DATA_FILE = "data/employees.json"
def load_employees():
 try:
  with open(DATA_FILE, encoding="utf-8") as f:
   return json.load(f)
 except FileNotFoundError:
  return []
 
def save_employees(employees):
 with open(DATA_FILE, "w", encoding="utf-8") as f:
  json.dump(employees, f, indent=2)