#problem
class Apple_hospital:
    def __init__(self, first_name, age, last_name):
        self.first_name = first_name
        self.age = age
        self.last_name = last_name

    def get_first_name(self):
        return self.first_name

    def get_age(self):
        return self.age

    def get_last_name(self):
        return self.last_name

class hospital_Employee(Apple_hospital):
    def __init__(self, first_name, age, last_name, salary):
        super().__init__(first_name, age, last_name)
        self.salary = salary

    def get_salary(self):
        return self.salary

class junior_doctor(hospital_Employee):
    def __init__(self, first_name, age, last_name, salary):
        super().__init__(first_name, age, last_name, salary)

    def get_position(self):
        return "Junior Doctor"

class senior_doctor(hospital_Employee):
    def __init__(self, first_name, age, last_name, salary):
        super().__init__(first_name, age, last_name, salary)

    def get_salary(self):
        return self.salary

    def get_position(self):
        return "Senior Doctor"

s_doctor = senior_doctor("Harsh", 75, "Rathi", 20)
print("(" + s_doctor.get_position() + ") " + s_doctor.get_first_name() + " " + s_doctor.get_last_name() + " (age " + str(s_doctor.get_age()) + ") - " + str(s_doctor.get_salary()))


s_doctor = senior_doctor("Tarun", 72, "nayak", 24)
print("(" + s_doctor.get_position() + ") " + s_doctor.get_first_name() + " " + s_doctor.get_last_name() + " (age " + str(s_doctor.get_age()) + ") - " + str(s_doctor.get_salary()))



s_doctor = senior_doctor("Ankush", 70, "Sharma", 22)
print("(" + s_doctor.get_position() + ") " + s_doctor.get_first_name() + " " + s_doctor.get_last_name() + " (age " + str(s_doctor.get_age()) + ") - " + str(s_doctor.get_salary()))


a1 = junior_doctor("Raja", 55, "Malviya", 10)
a2 = junior_doctor("kunal", 44, "Sharma", 10)
a3 = junior_doctor("Rakesh", 33, "Dubey", 8)
a4 = junior_doctor("Aditiya", 22, "Mehta", 10)
a5 = junior_doctor("Ravi", 22, "Joshi", 8)
a6 = junior_doctor("Virat", 22, "Yadav", 8)



junior_doctors = [a1, a2, a3, a4, a5, a6, ]


for doctor in junior_doctors:
    print("(" + doctor.get_position() + ") " + doctor.get_first_name() + " - " + str(doctor.get_salary()))
print("All salary amount in LPA (lakh per annum )")
