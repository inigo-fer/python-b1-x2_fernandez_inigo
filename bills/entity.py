from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, dni: str, email: str, mobile: str):
        self.dni=dni
        self.email=email
        self.mobile=mobile
        pass

    @abstractmethod
    def print(self):
        pass

    def __eq__(self, another):
       # Do not change this method
       return hasattr(another, 'dni') and self.dni == another.dni
    
    def __hash__(self):
       # Do not change this method
       return hash(self.dni)

class Buyer(Person):
    def __init__(self, dni: str, email: str, mobile: str, full_name: str, age: int, address: str):
        super().__init__(dni, email, mobile)
        self.full_name=full_name
        self.age=age
        self.address=address
        pass

    def print(self):
        # Do not change this method
        print(f"Buyer: {self.dni}, email:{self.email}")

class Seller(Person):
    # Write the parameters in the next line
    def __init__(self, dni: str, email: str, mobile: str, bussines_name: str, bussines_address: str):
        super().__init__(dni, email, mobile)
        self.bussines_address=bussines_address
        self.bussines_name=bussines_name        
        pass
        
    def print(self):
        # Do not change this method
        print(f"Seller: {self.dni} , email:{self.email} ")
