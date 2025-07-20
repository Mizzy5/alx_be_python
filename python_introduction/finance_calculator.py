# Prompt the user for income and expenses
income = int(input("Enter your monthly income: "))
expenses = int(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = income - expenses

# Project savings over one year with 5% interest
annual_savings = monthly_savings * 12
projected_savings = annual_savings + (annual_savings * 0.05)

# Display results
print("Your monthly savings are", "$",monthly_savings)
print("Projected savings after one year, with interest, is: ", "$",projected_savings)