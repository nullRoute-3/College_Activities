yearly_salary = float(input("Type your yearly salary:"))

portion_saved = float(input("Percentage of monthly salary that you can save:"))

cost_of_dream_home = int(input("Cost of your dream house:"))

portion_down_payment = cost_of_dream_home*0.25

monthly_saved = (yearly_salary / 12) * portion_saved

amount_saved = 0

month = 0

r = 0.05

while amount_saved < portion_down_payment:
  amount_saved += amount_saved * (r/12)
  amount_saved += monthly_saved
  month += 1
  
print(f"You can pay the 25% portion_down_payment of the house in {month} month(s).")

