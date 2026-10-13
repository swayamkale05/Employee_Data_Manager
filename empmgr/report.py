from .storage import load_employees


def department_summary():


    employees = load_employees()
    departments = {}

    for employee in employees:
        department = employee["department"]
        salary = employee["salary"]

        if department not in departments:
            departments[department] = {
                "headcount": 0,
                "total_salary": 0.0
            }

        departments[department]["headcount"] += 1
        departments[department]["total_salary"] += salary

    summary = {}

    for department, data in departments.items():
        headcount = data["headcount"]
        average_salary = data["total_salary"] / headcount

        summary[department] = {
            "headcount": headcount,
            "average_salary": round(average_salary, 2)
        }

    return summary