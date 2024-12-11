



class Employee :

    def __init__(self, eid, fname, lname):
        self.eid = eid
        self.fname = fname
        self.lname = lname
    @property
    def create_email(self):
        email =  f"{self.fname}.{self.lname}@company.com"
        self.email = email
    @create_email.setter
    def create_email(self, new_email):
        # james.bond@company.com
        self.fname = new_email.split('.')[0]
        self.lname = new_email.split('.')[1].split('@')[0]
        self.email = f"{self.fname}.{self.lname}@company.com"
    @create_email.deleter
    def create_email(self):
        del self.fname
        del self.lname
        del self.email
    def print_details(self):
        print(self.eid, self.fname, self.lname, self.email)

emp = Employee(1, 'John', 'Bond')

emp.create_email

emp.create_email = 'James.Pandit@company.com')
# Employee.create_email(emp, 'James.Pandit@company.com' )
emp.print_details()