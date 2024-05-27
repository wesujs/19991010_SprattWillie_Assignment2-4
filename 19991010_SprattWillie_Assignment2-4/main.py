# input statements
salary = float(input())
numDependents = float(input())

# calculate taxes here

# the variable "stateTax" will hold the variable "salary" multiplied by 0.065

stateTax = salary * 0.065

# the variable "federalTax" will hold the variable "salary" multiplied by 0.28

federalTax = salary * 0.28

# the variable "dependentDeduction" will hold the variable "salary" multiplied numDependents * 0.025 within parenthesis

dependentDeduction = salary * (numDependents * 0.025)

# The variable "totalWitholding" will holding will add the variables "stateTax", "federalTax", and "dependentDeduction"

totalWitholding = stateTax + federalTax + dependentDeduction

# the variable "takeHomePay" will hold the variable "salary" minus the variable "totalWitholding"

takeHomePay = salary - totalWitholding

# output statements
print("State Tax: $" + str(stateTax))
print("Federal Tax: $" + str(federalTax))
print("Dependents: $" + str(dependentDeduction))
print("Salary: $" + str(salary))
print("Take Home Pay: $" + str(takeHomePay))
