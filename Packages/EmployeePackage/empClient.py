import sys
sys.path.append("D:/Selenium-Practice/Packages/EmployeePackage/packA")
sys.path.append("D:/Selenium-Practice/Packages/EmployeePackage/packB")


import emp
empobj=emp.Employee(101,'Sid',5000)
empobj.displayEmp()


import stu
empobj=stu.Student(101,'Jatan',5000)
empobj.displayStudent()