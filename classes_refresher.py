class Employee:
    def __init__ (self, employee_name, employee_id):
        self.employee_name=employee_name
        self.employee_id=employee_id
class Qualification:
    def __init__ (self, degree):
        self.degree=degree

class Scientist(Employee, Qualification):
    def __init__(self, employee_name, employee_id, degree, designation):
        Employee.__init__(self, employee_name, employee_id)
        Qualification.__init__(self, degree)
        self.designation=designation
    def display_sci_details(self):
       print(f"Scientist details\nName:{self.employee_name}\nID:{self.employee_id}\nDegree:{self.degree}\nDesignation:{self.designation}")

sci1=Scientist("Henry","0098", "Btech+AI_ML", "Lead Engineer_Research and Development Division" ) 
sci1.display_sci_details()




# import math

# class Circle:
#     def __init__ (self, radius):
#         self.radius=radius
#     def display_properties(self):
#         area=math.pi*self.radius**2
#         print(f"Area of circle: {area}")

# c1=Circle(float(input("Enter radius of circle: ")))
# c1.display_properties()


        

# class Person:
#     def __init__ (self, name, age):
#         self.name=name
#         self.age=age
#     def display_details(self):
#         print(f"Name: {self.name}\nAge: {self.age}")

# person1=Person("Henry", "21")
# person1.display_details()
