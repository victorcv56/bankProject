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
    
    def make_paymt(self, payment):
        """Method that will make a payment towards card balance."""
        # payment = int(input("Payment amount: "))
        self.bal -= payment
        print("{} paid towards card. \nNew balance is {:.2f}".format(payment, self.bal))

    # figured out monthly minimum payment algo
    def monthly_interest_charge(self):
        """Method that calculates the monthly interest payment for card."""
        fee = (self.bal * 0.01) + (self.get_interest() / 12) #monthly interest paid
        print(fee)
    
    
    def minimum_pymt(self):
        """This will calculate monthly minimum payment on CC."""
        fee = (self.bal * 0.01) + (self.get_interest() / 12) #monthly interest paid
        print("fee will be {}".format(fee))
        return fee

    def pay_off_min_payments(self):
        """Loop that will pay off credit card and return months taken to pay off debt."""
        months = 0
        while self.bal >= 1: # while loop that will run until balance is paid off
            self.make_paymt(self.minimum_pymt()) # calls on the make payment method to simulate a payment being made
            months += 1
            print('Remaining balance: {}'.format(self.bal))
            
        return months

    # def pay_off_in_given_time(self):
    #     """Method will return how much user will have to pay monthly
    #     if they want to pay off debt in given amount of time."""
    #     months = int(input("Time needed to pay off card(months): "))
    #     monthly_bal = self.bal / months
    #     print(monthly bal)


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
print('Monthly minimum payment is {}'.format(monthly_fee))

