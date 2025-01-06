'''
This project is part of the kata chanllenges in CodeWars for Python beginners.
Att: Kevin Feliz Henríquez.
'''

def create_schedule(employees, month_year, n):
    month, year = int(month_year[:2]), int(month_year[2:])

    if month == 2:  
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            days_in_month = 29  
        else:
            days_in_month = 28
    elif month in [4, 6, 9, 11]:  
        days_in_month = 30
    else:  
        days_in_month = 31

    if len(employees) < n:
        return None

    schedule = []
    employee_index = 0

    for day in range(days_in_month):
        day_schedule = []
        for _ in range(n):
            assigned = False
            for _ in range(len(employees)):
                employee = employees[employee_index]
                employee_index = (employee_index + 1) % len(employees)
                if not schedule or employee not in schedule[-1]:
                    day_schedule.append(employee)
                    assigned = True
                    break
            if not assigned:
                return None  
        schedule.append(day_schedule)

    shifts_per_employee = {emp: 0 for emp in employees}
    for day_schedule in schedule:
        for emp in day_schedule:
            shifts_per_employee[emp] += 1

    max_shifts = max(shifts_per_employee.values())
    min_shifts = min(shifts_per_employee.values())
    if max_shifts - min_shifts > 1:
        return None

    return schedule

# Ejemplo de uso
employees = ["Feliz", "Adalberto", "Pedro", "Mario", "Jose", "Ramon"]
month_year = "012025"
n = 3

result = create_schedule(employees, month_year, n)
if result:
    print("\n".join(f"Day {day + 1}: {', '.join(shift)}" for day, shift in enumerate(result)))
else:
    print("None")