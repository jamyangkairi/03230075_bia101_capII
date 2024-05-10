class Employee_Income:
    def __init__(self, employee_income, life_insurance, child_education_allowance, bonus):
        self.employee_income = employee_income
        self.life_insurance = life_insurance
        self.child_education_allowance = child_education_allowance
        self.bonus = bonus

    def calculate_PIT(self):
        total_deductions = self.child_education_allowance + self.life_insurance
        gross_income = self.employee_income + self.bonus  # Add bonus to gross income

        PIT = gross_income * 0.3 
        
        if gross_income <= 300000:
            PIT = 0 # in the terminal if user input amount less than the 300000 the pit would be 0 since they dont have to file for tax
        elif gross_income <= 400000:
            PIT *= 0.10
        elif gross_income <= 650000:
            PIT *= 0.15
        elif gross_income <= 1000000:
            PIT *= 0.20
        elif gross_income <= 1500000:
            PIT *= 0.25

        # charge extra tax for  1 million+
        if PIT >= 1000000:
            surcharge = PIT * 0.10
            PIT += surcharge

        return PIT

class Employee_Marital_Status: # check the status of employer and see if they have school going children. they can have tax deductible for child education purpose
    def __init__(self, married, single, child):
        self.married = married
        self.single = single
        self.child = child

    def child_education_allowance(self):
        if self.child <= 1:
            return 350000 # the child education get allowance of nu 350000 at max
        else:
            return 0

class EmployeeBonus:
    def __init__(self, employee_income):
        self.employee_income = employee_income

    def employee_bonus(self):
        if self.employee_income <= 100000:
            return 0.1 * self.employee_income
        else:
            return 0  #no bonus for more than 1000000 salary 

class deduction:
    child_education_allowance = 350000
    gis = 40000 

    @staticmethod
    def calculate_deduction(employee):
        total_deduction = 0
    
        return total_deduction

try:
    employee_name = input("Enter your name: ")
    income = int(input("Enter your annual income: "))
    job_type = input("Enter job type, government or private: ")
    status = input("State your marital status (single or married): ")
    child = int(input("State the number of your children at school: "))
    life_insurance = int(input("Enter your insurance amount (if any): "))
    bonus = int(input("Enter your bonus amount: "))

    marital_status = Employee_Marital_Status(status == "married", status == "single", child) # this will help  computer to see if they are eligible for the childeducation allowance.
    child_education_allowance = marital_status.child_education_allowance()

    employee_bonus = EmployeeBonus(income).employee_bonus() # bonus is added to gross salary 
    total_deduction = deduction.calculate_deduction(income)

    employee = Employee_Income(income, life_insurance, child_education_allowance, bonus)
    PIT = employee.calculate_PIT()

    print(f"{employee_name}'s Personal Income Tax (PIT) is: {PIT}")

except ValueError: # value error will help users to remind them to type correct input instead of showing the errors in the terminal
    print("Please enter valid numerical inputs.") 
