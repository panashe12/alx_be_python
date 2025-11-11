# finance_calculator.py

# Prompt the user for monthly income and expenses
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# Assume a simple annual interest rate of 5%
annual_interest_rate = 0.05

# Project annual savings including interest
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * annual_interest_rate)

# Display results
print(f"Your monthly savings are ${monthly_savings}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings}.")
