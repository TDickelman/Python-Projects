# Put your code here
wage = input("Enter your wage: ")
regularHoursWorked = input("Enter number of normal hours worked: ")
overtimeHoursWorked = input("Enter number of overtime hours worked: ")

normalPay = float(wage) * float(regularHoursWorked)
overtimePay = float(wage)

totalOvertimePay = overtimePay * 1.5

finalOvertimePay = totalOvertimePay * float(overtimeHoursWorked)

totalPay = finalOvertimePay + normalPay

print(f'The total weekly pay is ${totalPay}')
