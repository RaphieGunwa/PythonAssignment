def pay(salary, hours_worked):
    normal_hours = min(8, hours_worked)
    overtime_hours = max(0, hours_worked - 8)
    return (salary * normal_hours) + (1.5 * salary * overtime_hours)

# Test the pay method
print(pay(3.5, 8))  
print(pay(7.0, 15)) 
