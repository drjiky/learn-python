income = float(input("Enter the annual income: "))
if income<=85528:
    tax=((income/100)*18)-556.2
else:
    tax=14839.2+((income-85528)/100)*32
#
# Write your code here.
#

tax = round(tax, 0)
print("The tax is:", tax, "thalers")
