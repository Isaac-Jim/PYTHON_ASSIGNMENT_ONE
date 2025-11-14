# Given lists
employees = ["Kwame", "Akua", "Yaw", "Afia"]
salaries = [3200, 4000, 2800, 5000]

# 1. Combine lists into a dictionary (name → salary)
employee_salaries = {}

for i in range(len(employees)):
    employee_salaries[employees[i]] = salaries[i]

# 2. Adjust salaries using dictionary methods
for name, old_salary in employee_salaries.items():   # using .items()
    
    if old_salary < 3500:
        new_salary = old_salary * 1.07   # add 7%
    else:
        new_salary = old_salary * 1.04   # add 4%
    
    # update new salary back into dictionary
    employee_salaries.update({name: new_salary})

    # 3. Print formatted result for each employee
    print(f"{name} | Old: {old_salary:.2f} | New: {new_salary:.2f}")
