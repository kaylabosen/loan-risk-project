loan_amount = 20000
annual_rate = 0.06
years = 5

monthly_rate = annual_rate / 12
number_of_payments = years * 12

monthly_payment = (
    loan_amount * monthly_rate
    / (1 - (1 + monthly_rate) ** (-number_of_payments))
)

total_paid = monthly_payment * number_of_payments
total_interest = total_paid - loan_amount

total_monthly_debt = monthly_payment + other_monthly_debt
dti = total_monthly_debt / monthly_income

if dti < 0.36:
    risk = "Lower Risk"
elif dti < 0.50:
    risk = "Moderate Risk"
else:
    risk = "Higher Risk"

print("Loan Amount: $", loan_amount)
print("Monthly Payment: $", round(monthly_payment, 2))
print("Total Interest Paid: $", round(total_interest, 2))
print("Debt-to-Income Ratio:", round(dti * 100, 2), "%")
print("Risk Classification:", risk)

