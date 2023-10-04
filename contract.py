"""Employment Contracts"""
import employee

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
    