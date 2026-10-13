def parse_salary(text):
 try:
  return float(text)
 except ValueError:
  return None