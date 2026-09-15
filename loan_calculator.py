loan_amount = 20000
annual_rate = 0.06
years = 5

monthly_rate = annual_rate / 12
number_of_payments = years * 12

monthly_payment = (
    loan_amount * monthly_rate
    / (1 - (1 + monthly_rate) ** (-number_of_payments))
)

print("Loan Amount: $", loan_amount)
print("Monthly Payment: $", round(monthly_payment, 2))


