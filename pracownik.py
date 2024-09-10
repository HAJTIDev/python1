class Employee:
    count=0
    def __init__(self,name,surname,pay):
        Employee.count+=1
        self.name=name
        self.surname=surname
        self.pay=pay
        self.licznik=0
    
    def register_time(self,time):
        self.time=time
        self.licznik+=time

    def pay_salary(self):
        if self.time>8:
            print(self.licznik*self.pay*2-(self.licznik-2)*self.pay)
        else:
            print(self.licznik*self.pay)
        self.licznik=0
    def write(self):
        print(Employee.count)
    


employee=Employee('Jan','Nowak',100)
employee.register_time(5)
employee.pay_salary()
employee.pay_salary()
employee.register_time(10)
employee.pay_salary()
employee.write()


