class Employee:
    def __init__(self, employee_id, name, department):
        self._id = employee_id
        self._name = name
        self._department = department
        self._subordinates = []

    def add_subordinate(self, employee):
        self._subordinates.append(employee)

    def remove_subordinate(self, employee_id):
        if len(self._subordinates) == 0:
            return False
        for index, employee in enumerate(self._subordinates):
            if employee.get_id() == employee_id:
                self._subordinates.pop(index)
                return True
            else:
                result = employee.remove_subordinate(employee_id)
                if result == True:
                    return result
        return False

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def __str__(self):
        result = f'Name: {self._name}\n'
        for employee in self._subordinates:
            result+= f"\t{employee.get_name()}"
        return result

e1 = Employee(1, "Max", "IT")
e2 = Employee(2, "Mike", "IT")
e3 = Employee(3, "Jake", "IT")
e4 = Employee(4, "James", "IT")
e5 = Employee(5, "Blake", "IT")
e6 = Employee(6, "Brandon", "IT")
e1.add_subordinate(e2)
e1.add_subordinate(e3)
e2.add_subordinate(e4)
e2.add_subordinate(e5)
e2.add_subordinate(e6)

print(e2)
e1.remove_subordinate(5)
print(e2)