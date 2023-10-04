"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

from contract import Contract
class Employee:
    def __init__(self, name, contract):
        self.name = name
        self.contract = contract

    def get_pay(self):
        return self.contract.get_pay()

    def __str__(self):
        return self.name


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie_contract = Contract(pay = 4000)
billie = Employee('Billie', billie_contract)


# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie_contract = Contract(pay = 25, hours = 100)
charlie = Employee('Charlie', charlie_contract)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee_contract = Contract(pay = 3000, commission = 200, commission_count = 4)
renee = Employee('Renee', renee_contract)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan_contract = Contract(pay = 25, hours = 150, commission = 220, commission_count = 3)
jan = Employee('Jan',jan_contract)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.

roobbie_contract = Contract(pay = 2000, commission = 1500)
robbie = Employee('Robbie', roobbie_contract)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel_contract = Contract(pay = 30, hours = 120, commission = 600)
ariel = Employee('Ariel', ariel_contract)
