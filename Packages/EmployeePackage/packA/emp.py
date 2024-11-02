class Employee:
    def __init__(self,eid,name,sal):
        self.eid=eid
        self.ename=name
        self.salary=sal
    def displayEmp(self):
        print(self.eid,self.ename,self.salary)