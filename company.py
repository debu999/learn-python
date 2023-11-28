from employee import CommissionEmployee, Employee, HourlyEmployee, SalaryEmployee

class Company:
    def __init__(self):
        self.employees = []
        
    def add_employee(self, employee):
        self.employees.append(employee)
    
    def display_employees(self):
        print("Current employees:")
        for i in self.employees:
            print(i.fname, i.lname)
        print("----------------------------------------------------------------")
    def pay_employees(self):
        print("Paying Employees:")
        for i in self.employees:
            print("Paycheck for: ", i.fname, i.lname)  
            print(f"Amount: ${i.calculate_paycheck():,.2f}")
            print("----------------------------------------------------------------")

def main():
    my_company = Company()
    employee1 = SalaryEmployee("Debabrata", "Patnaik", 300000)
    employee2 = HourlyEmployee("Debabrata", "Patnaik1", 40, 100)
    employee3 = CommissionEmployee("Debabrata", "Patnaik2", 100000, 10, 50)
    
    my_company.add_employee(employee1)
    my_company.add_employee(employee2)
    my_company.add_employee(employee3)
    
    my_company.display_employees()
    my_company.pay_employees()


main()