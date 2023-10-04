"""Employment Contracts"""

# Salary contacts do not have hours
# Bonus contracts do not have commission count
class Contract:
    def __init__(self, pay, hours = 0, commission = 0, commission_count = 0):
        self.pay = pay
        self.hours = hours
        self.commission = commission
        self.commission_count = commission_count

    def get_pay(self):
        contract_pay = self.pay
        if (self.hours):
            contract_pay = contract_pay * self.hours

        commission_pay = self.commission
        if (self.commission_count):
            commission_pay = commission_pay * self.commission_count

        return contract_pay + commission_pay
    
    def __str__(self):
        return_string = "a"
        if (self.hours):
            return_string += f" contract of {self.hours} hours at {self.pay}/hour"
        else:
            return_string += f" monthly salary of {self.pay}" 

        if (self.commission):
            if (self.commission_count):
                return_string += f" and receives a commission for {self.commission_count} contract(s) at {self.commission}/contract"
            else:
                return_string += f" and receives a bonus commission of {self.commission}"
        
        return_string += "."
        return return_string
