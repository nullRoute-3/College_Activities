yearly_salary = float(input("Enter your yearly salary:"))

portion_saved = float(input("Enter the monthly salary you can save in decimal:"))

cost_of_dream_home = float(input("Enter the cost of your dream house:"))

semi_annual_raise = float(input("Enter your ma your raise every 6 months in decimal"))

portion_down_payment = cost_of_dream_home*0.25

monthly_salary = yearly_salary/12

monthly_saved = monthly_salary * portion_saved

amount_saved = 0

month = 0

r = 0.05

while amount_saved < portion_down_payment:
  
  amount_saved += amount_saved * (r/12)
  amount_saved += monthly_saved
  month += 1
  
  if month % 6 == 0:
      monthly_salary += monthly_salary*semi_annual_raise
    
      monthly_saved = monthly_salary * portion_saved
  
print(f"You can pay the 25% payment of the house in {month} month(s).")

