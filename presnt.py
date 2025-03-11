from datetime import datetime

class Company:
    def __init__(self, company_id, name, industry, balance=0.0):
        self.company_id = company_id
        self.name = name
        self.industry = industry
        self.balance = balance
        self.transactions = []
        self.employees = []

    def deposit(self, amount):
        self.balance += amount
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.transactions.append(f"{timestamp} - Deposited {amount}. New balance: {self.balance}")
        print(f"{timestamp} - Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds. Withdrawal failed.")
            return
        self.balance -= amount
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.transactions.append(f"{timestamp} - Withdrew {amount}. New balance: {self.balance}")
        print(f"{timestamp} - Withdrew {amount}. New balance: {self.balance}")

    def add_employee(self, employee):
        self.employees.append(employee)

    def get_transaction_history(self):
        if not self.transactions:
            return "No transactions found."
        return "\n".join(self.transactions)

    def get_details(self):
        details = f"\nCompany ID: {self.company_id}\nName: {self.name}\nIndustry: {self.industry}\nBalance: {self.balance}\n"
        details += "Transactions:\n" + (self.get_transaction_history() if self.transactions else "No transactions yet.") + "\n"
        details += "Employees:\n" + "\n".join(emp.get_details() for emp in self.employees) + "\n"
        return details

class Employee:
    def __init__(self, emp_id, name, position, salary):
        self.emp_id = emp_id
        self.name = name
        self.position = position
        self.salary = salary

    def get_details(self):
        return f"  Employee ID: {self.emp_id}, Name: {self.name}, Position: {self.position}, Salary: {self.salary}"

class Bank:
    def __init__(self, name):
        self.name = name
        self.companies = {}

    def add_company(self, company):
        self.companies[company.company_id] = company
        print(f"Company {company.name} added successfully.")
    
    def remove_company(self, company_id):
        if company_id in self.companies:
            removed_company = self.companies.pop(company_id)
            print(f"Company {removed_company.name} removed successfully.")
        else:
            print("Company ID not found. Removal failed.")

    def get_company_by_id(self, company_id):
        return self.companies.get(company_id, None)
    
    def get_company_by_name(self, company_name):
        for company in self.companies.values():
            if company.name.lower() == company_name.lower():
                return company
        return None

    def get_all_companies(self):
        return "\n".join(company.get_details() for company in self.companies.values())

    def perform_transaction(self, company_id, transaction_type, amount):
        company = self.get_company_by_id(company_id)
        if company is None:
            print("Invalid Company ID. Transaction failed.")
            return
        
        if transaction_type == "deposit":
            company.deposit(amount)
        elif transaction_type == "withdraw":
            company.withdraw(amount)
        else:
            print("Invalid transaction type. Transaction failed.")

# Example Usage
bank = Bank("Tecrix Bank")

# add companies with employees
company1 = Company(1, "TechCorp", "Technology", 100000)
company1.add_employee(Employee(101, "Habib", "Engineer", 6000))
company1.add_employee(Employee(102, "altaf", "Manager", 8000))
company1.add_employee(Employee(103, "kuldeep", "Developer", 7000))

company2 = Company(2, "Tecrix", "Technology", 500000)
company2.add_employee(Employee(201, "Arif Farooqui", "Chef", 5000))
company2.add_employee(Employee(202, "Tassawar abbas", "manager", 300000))
company2.add_employee(Employee(203, "Ali Hamza", "Instructor", 400000))

company3 = Company(3, "suncorp", "Technology", 100000)
company3.add_employee(Employee(104, "Habib", "Engineer", 6000))
company3.add_employee(Employee(105, "altaf", "Manager", 8000))
company3.add_employee(Employee(106, "kuldeep", "Developer", 7000))

bank.add_company(company1)
bank.add_company(company2)
bank.add_company(company3)

while True:
    print("\nBank Transaction Menu:")
    print("1. Deposit Money")
    print("2. Withdraw Money")
    print("3. Show All Companies")
    print("4. Get Company Details by Name")
    print("5. Get Transaction History of a Company")
    print("6. Add a Company")
    print("7. Remove a Company")
    print("8. Exit")
    choice = input("Enter your choice: ")
    
    if choice in ["1", "2"]:
        try:
            company_id = int(input("Enter Company ID: "))
            amount = float(input("Enter Amount: "))
            transaction_type = "deposit" if choice == "1" else "withdraw"
            bank.perform_transaction(company_id, transaction_type, amount)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    elif choice == "3":
        print(bank.get_all_companies())
    elif choice == "4":
        company_name = input("Enter Company Name: ")
        company = bank.get_company_by_name(company_name)
        if company:
            print(company.get_details())
        else:
            print("Company not found")
    elif choice == "5":
        company_id = int(input("Enter Company ID: "))
        company = bank.get_company_by_id(company_id)
        if company:
            print("Transaction History:\n" + company.get_transaction_history())
        else:
            print("Company not found")
    elif choice == "6":
        company_id = int(input("Enter New Company ID: "))
        name = input("Enter Company Name: ")
        industry = input("Enter Industry Type: ")
        balance = float(input("Enter Initial Balance: "))
        new_company = Company(company_id, name, industry, balance)
        bank.add_company(new_company)
        
        add_employees = input("Do you want to add employees to this company? (yes/no): ").strip().lower()
        while add_employees == "yes":
            emp_id = int(input("Enter Employee ID: "))
            emp_name = input("Enter Employee Name: ")
            position = input("Enter Position: ")
            salary = float(input("Enter Salary: "))
            new_employee = Employee(emp_id, emp_name, position, salary)
            new_company.add_employee(new_employee)
            add_employees = input("Do you want to add another employee? (yes/no): ").strip().lower()
    elif choice == "7":
        company_id = int(input("Enter Company ID to Remove: "))
        bank.remove_company(company_id)
    elif choice == "8":
        break
    else:
        print("Invalid choice, please try again.")
