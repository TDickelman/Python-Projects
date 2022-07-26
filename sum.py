# Edit the code below
theSum = 0.0
average = 0.0
count = 0.0

data = input("Enter a number: ")
while data != "":
    count = count + 1.0
    number = float(data)
    theSum += number
    data = input("Enter the next number: ")
    average = theSum / count

print("The sum is", theSum)
print("The average is", average)
