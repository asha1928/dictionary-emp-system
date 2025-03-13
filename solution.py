class EmployeeManagementSystem:
    def _init_(self):
        self.employees = {} 

    def add_employee(self, emp_id, name, age, department, salary):
        if emp_id in self.employees:
            print("Error: Employee ID already exists!")
            return
         if not name.strip() or not isinstance(age, int) or age < 18 or age > 65:
            print("Error: Invalid employee details!")
            return
        
        self.employees[emp_id] = {
            "Name": name,
            "Age": age,
            "Department": department,
            "Salary": salary
        }
        print(f"Employee {name} added successfully!")

    def update_employee(self, emp_id, **kwargs):
        if emp_id not in self.employees:
            print("Error: Employee not found!")
            return
          for key, value in kwargs.items():
            if key in self.employees[emp_id]:
                self.employees[emp_id][key] = value
        print(f"Employee {emp_id} updated successfully!")

    def remove_employee(self, emp_id):
        if emp_id in self.employees:
            del self.employees[emp_id]
            print(f"Employee {emp_id} removed successfully!")
        else:
            print("Error: Employee ID not found!")

    def search_employee(self, emp_id)
        return self.employees.get(emp_id, "Employee not found!")

    def sort_employees(self, criteria="Name", reverse=False):
        if not self.employees:
            print("No employees to sort!")
            return []
          if criteria not in ["Name", "Age", "Department", "Salary"]:
            print("Error: Invalid sorting criteria!")
            return []
 sorted_employees = sorted(self.employees.items(), key=lambda x: x[1][criteria], reverse=reverse)
        return sorted_employees
 def display_all(self):
        """Displays all employee records."""
        if not self.employees:
            print("No employees in the system.")
            return
        for emp_id, details in self.employees.items():
            print(f"ID: {emp_id}, {details}")
if _name_ == "_main_":
    ems = EmployeeManagementSystem()
    ems.add_employee(101, "Asha", 29, "HR", 55000)
    ems.add_employee(102, "Anusha", 35, "IT", 70000)
    ems.display_all()
    ems.update_employee(101, Salary=60000)
    print(ems.search_employee(101))
    print("Sorted Employees:", ems.sort_employees("Salary", reverse=True))
    ems.remove_employee(102)
    ems.display_all()
