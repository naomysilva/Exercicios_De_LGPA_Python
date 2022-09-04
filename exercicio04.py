# Make a program that asks how much you earn per hour and the number of hours worked in the month.
# Calculate and show the total of your salary in that month, knowing that 11% are deducted for the Income Tax,
# 8% for the INSS and 5% for the union, make a program that gives us: gross salary. How much did you pay the INSS?
# How much did you pay the union? the net salary. Calculate the discounts and the net salary.


hour_value = int(input("hour value:"))
work_hour = int(input("work hour:"))

sum = hour_value * work_hour

IR = sum * 0.11

INSS = sum * 0.08

union = sum * 0.05

net_Salary = sum - IR - INSS - union



print("Gross salary", sum)
print("IR", IR)
print("INSS", INSS)
print("TRADE UNION", union)
print("NET SALARY", net_Salary)
