# Part A: Saving for a House

You have just graduated from MIT and have a job! You move to the Bay Area and decide that you want to start saving for a home. Houses are fairly expensive, so you start saving up for the down payment on your dream home.

Your goal is to find the number of months it takes to save up for a down payment. The cost of your down payment is calculated by multiplying the total cost of your dream house by the down payment percentage.

## User Inputs
Ask the user to enter the following variables and cast them as floats. They must be initialized in the following order at the beginning of your program, before declaring other variables:
1. The starting yearly salary (`yearly_salary`)
2. The portion of salary to be saved (`portion_saved`). This variable should be in decimal form (e.g., `0.1` for 10%).
3. The cost of your dream home (`cost_of_dream_home`)

## Writing the Program
You will need to determine how many months it will take given the following information:
1. `yearly_salary`, as described above.
2. `portion_saved`, as described above.
3. `cost_of_dream_home`, as described above.
4. `portion_down_payment`, the percentage of the total cost needed for a down payment. Assume `portion_down_payment = 0.25` (25%).
5. The amount that you have saved thus far is `amount_saved`, which starts at `$0`.
6. You get an annual rate of return `r`. In other words, at the end of each month, you receive an additional `amount_saved * (r/12)` funds for your savings (the 12 is because `r` is an annual rate). Assume `r = 0.05` (5%).
7. At the end of each month, your savings increase by:
   - A percentage of your monthly salary, and
   - The monthly return on your investment. 
   
*(Note: The investment amount used to calculate the monthly return is the amount you had saved at the start of each month.)*

## Output
1. Your program should store the number of months required to save for the down payment using a variable called `months`.

## Notes
- Be careful about values that represent annual amounts versus monthly amounts.
- If the number of months your program returns is off by one, reread the highlighted text above.
- Assume that users enter valid inputs (e.g., no string inputs when expecting a float).
- Your program should print outputs in the same format as the test cases below. If you're using Spyder, you might see extra lines in between outputs. Don't worry about them!

# Part B: Saving with a Raise

In Part A, we assumed that your salary did not change over time. However, as an MIT graduate, you are going to be worth more to your company over time! In this part, we build on your solution from Part A by adding a salary raise every six months. Copy over your solution from Part A into the corresponding sections in `ps1b.py`.

## User Inputs
There is one additional user input in Part B. Remember to cast these inputs as floats and collect them in the following order before declaring other variables:

1. **`yearly_salary`**: The starting yearly salary.
2. **`portion_saved`**: The portion of salary to be saved.
3. **`cost_of_dream_home`**: The cost of your dream home.
4. **`semi_annual_raise`**: The semi-annual salary raise, which is a decimal percentage (e.g., `0.1` for 10%).

## Writing the Program
Write a program to calculate how many months it will take for you to save up for a down payment. You can reuse much of the code from Part A. 

* Assume that your investments earn an annual rate of return $r = 0.05$ (or 5%).
* Assume `portion_down_payment = 0.25` (or 25%).
* `yearly_salary` increases by `semi_annual_raise` at the end of every six months.

## Output
* Store the number of months required to save up for your down payment using a variable called `months`.

## Notes
* The investment amount used to calculate the monthly return is the amount you had saved at the start of each month.
* Be careful about values that represent annual amounts versus monthly amounts.
* Raises should only happen at the end of the 6th, 12th, 18th month, and so on.
* If the number of months your program returns is off by one, double-check when your raises are being applied.
* Assume that users enter valid inputs (e.g., no string inputs when expecting a float).
* Your program should print outputs in the same format as the test cases.
