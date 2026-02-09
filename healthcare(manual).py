from abc import ABC,abstractmethod
class User():
    def __init__(self,name,email):
        self.Name=name
        self.Email=email
        
    def login(self):
        print("Name:",self.Name)
        print("Email:",self.Email)
        print("Login successfully")         

class patient(User):
    def __init__(self, name, email, healthID):
        self.Name=name   
        self.Email=email     
        self.__healthID=healthID

    def get(self):
        print("name:",self.Name)
        print("email:",self.Email)
        print("healthID:",self.__healthID)

    def set(self,newName,newEmail):
        self.Name=newName
        self.Email=newEmail
        print("your in update page")

class Doctor(User):
    def __init__(self, name, email, specialization):
        super().__init__(name, email)      
        self.Specialization = specialization

    def __str__(self):
        return f"Doctar \nName:{self.Name}\nEmail:{self.Email}\nspecialization:{self.Specialization}"
    
class consulation(ABC):
    @abstractmethod
    def prescription(self):
        pass    

class general_checkup(consulation):
    def prescription(self):
        print("prescription: take medicine regularly ")

class surgery(consulation):
    def prescription(self):
        print("specialist surgery:heart surgery")
 
obj=User("shabu","abi@gmail.com")  
obj.login()
obj=patient("shabu","abi@gmail.com",12345)
obj.set("abi","shaby@6625")
obj.get()
print("message: updated successfully")
D=Doctor("dr.arun","arun@1233","heart")
print(D)
consulation=[general_checkup(),surgery()]
for c in consulation:
    c.prescription()
    


