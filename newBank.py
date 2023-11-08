import math
"""Simple program to practice python objects"""

class bankCards: 
    """This is a class which will create bank card objects."""

    def __init__(self, cardBank, cardApr, cardBal):
        """function that will be automatically 
        called when creating object."""
        self.name = cardBank
        self.apr = cardApr #converts to decimal for easy calculation
        self.bal = cardBal

    def __str__(self):
        """String function that will print out 
        a brief description of object."""
        return "{} card has {}% APR and {} balance.".format(self.name, self.apr, self.bal)
    
    def get_interest(self):
        """Attempt to get what we will pay in interest on card."""
        interest = self.bal * (self.apr / 100) # Multiply apr by balance to get interest.
        #print("You will pay a total of {:.2f} monthly interest.".format(interest / 12))
        return interest
    
    def make_paymt(self):
        """Method that will make a payment towards card balance."""
        payment = int(input("Payment amount: "))
        self.bal -= payment
        print("{} paid towards card. \nNew balance is {:.2f}".format(payment, self.bal))

    def minimum_pymt(self):
        """This will calculate monthly fee of credit card."""
        fee = (self.bal * 0.01) + (self.get_interest() / 12)
        #monthly_minimum = fee 
        print("fee will be {}".format(fee))
        return fee

# This class only has to have methods that pertain to things a credit card
# can do or can be done to like getting certain calculations nd
# showing different traits

# I want to come up with a method that lets me make payments considering
# the monthly charge made.

# Initializes card with given attributes
barclays = bankCards('Barclays', 29.99, 1511.06)
print(barclays)
print(barclays.get_interest())
monthly_fee = barclays.minimum_pymt()
print('Monthly min pament is {}'.format(monthly_fee))