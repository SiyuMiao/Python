#Siyu Miao
#set class of Man, the people who has name and phone
class Man(object):
    def __init__(self,name,phone):
        self.name = name
        self.phone = phone

    def Info_p(self):
        return "Person "+str(self.name)+" has phone "+str(self.phone)
#set class of student, and let class Man into the student, and add gpa
class Student(Man):

    gpa_total = []

    def __init__(self,name,phone,gpa):
        Man.__init__(self,name,phone)
        self.gpa=gpa
        Student.gpa_total.append(self.gpa)
#Calculate the mean gpa
    @staticmethod
    def mean_gpa():
        return sum(Student.gpa_total)/float(len(Student.gpa_total))

    def info_gpa(self):
        reply = self.Info_p()
        reply+= "\n\tand is a Student with gpa "+str(self.gpa)
        return reply

    def __str__(self):
        return self.info_gpa()

#Set class man into the class employee, and add salary
class Employee(Man):
    emp_total = []
    def __init__(self,name,phone,employee):
        Man.__init__(self,name,phone)
        self.employee=employee
        Employee.emp_total.append(self.employee)

#Calculate the total salary
    @staticmethod
    def total_salary():
        return sum(Employee.emp_total)
        
    def info_em(self):
        reply = self.Info_p()
        reply+= "\n\tand is an Employee with salary "+str(self.employee)
        return reply


#Set class employee into the class staff, and add title
class Staff(Employee):
    def __init__(self,name,phone,employee,staff):
        Employee.__init__(self,name,phone,employee)
        self.staff=staff

    def info_staff(self):
        reply = self.info_em()
        reply+= "\n\tand is Staff with title "+str(self.staff)
        return reply

    def __str__(self):
        return self.info_staff()
#Set class employee into the class professor, and add the course
class Professor(Employee):
    def __init__(self,name,phone,employee,assigned):
        Employee.__init__(self,name,phone,employee)
        self.assigned=assigned

    def Info_M(self):
        reply = self.info_em()
        reply+="\n\tand is a Professor assigned to class "+str(self.assigned)
        return reply

    def __str__(self):
        return self.Info_M()




#main code
People = [Student("Sandy","326-8324",3.65),Student("Jordan","632-7434",3.1),\
          Professor("Leslie","985-2363",50000.00,"Info 501"),\
          Staff("Alex","743-4638",25000.00,"Editor")]

print "These are the people in the university: "
for person in People:
    print person
print


print"Our total university payroll budget is: "+str(Employee.total_salary())
print"Our average student GPA is: "+str(Student.mean_gpa())
