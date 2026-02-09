from abc import ABC, abstractmethod
import uuid
class User:
    def __init__(self, name, email):
        self.Name = name
        self.Email = email

    def login(self):
        print("\nLOGIN DETAILS")
        print("Name:", self.Name)
        print("Email:", self.Email)
        print("Login successfully")

class patient(User):
    def __init__(self, name, email, healthID):
        super().__init__(name, email)
        self.__healthID = uuid.uuid4()

    choice = input("\nDo you want to update patient profile?")

    if choice == "update":
        new_name = input("Enter new name: ")
        new_email = input("Enter new email: ")
        self.Name = new_name
        self.Email = new_email
        self.show()

    else:
        print("\nNoupdation update selected")

    print("\nProgram completed")        


    def get(self):
        print("\nPATIENT DETAILS")
        print("Name:", self.Name)
        print("Email:", self.Email)
        print("Health ID:", uuid.uuid4())

    def set(self, newName, newEmail):
        self.Name = newName
        self.Email = newEmail
        print("\nYour details are updated")

class Doctor(User):
    def __init__(self, name, email, specialization):
        super().__init__(name, email)
        self.Specialization = specialization

    def __str__(self):
        return (
            "\nDOCTOR DETAILS"
            f"\nName: {self.Name}"
            f"\nEmail: {self.Email}"
            f"\nSpecialization: {self.Specialization}"
        )
class consulation(ABC):
    @abstractmethod
    def prescription(self):
        pass


class general_checkup(consulation):
    def prescription(self):
        print("\nPrescription: Take medicine regularly ")


class surgery(consulation):
    def prescription(self):
        print("\nPrescription: Heart surgery required and get oppoinment tomorrow")

# User Login
name = input("Enter user name: ")
email = input("Enter user email: ")
u = User(name, email)
u.login()

# Patient Details
p_name = input("\nEnter patient name: ")
p_email = input("Enter patient email: ")
health_id = uuid.uuid4()
p = patient(p_name, p_email, health_id)

# Update Patient
new_name = input("\nEnter new patient name: ")
new_email = input("Enter new patient email: ")
p.set(new_name, new_email)
p.get()

# Doctor Details
d_name = input("\nEnter doctor name: ")
d_email = input("Enter doctor email: ")
d_spec = input("Enter doctor specialization: ")

d = Doctor(d_name, d_email, d_spec)
print(d)

# Consultation Choice
print("\nCONSULTATION TYPE")
print("1. General Checkup")
print("2. Surgery")

choice = int(input("Enter your choice: "))

if choice == 1:
    c = general_checkup()
elif choice == 2:
    c = surgery()
else:
    print("Invalid choice")
    exit()

c.prescription()

