from writer import data_writer as l
# writer is imported so information on cards is written to a .txt
# file and easily accesed by user. 
# Information like how many months it will take to pay credit card, 
# how much should be paid each month in order to pay off card in a 
# certain amount of time, etc..
"""Simple program to practice python objects"""

class bankCards: 
    """This is a class which will create bank card objects."""

    def __init__(self, cardBank, cardApr, cardBal):
        """function that will be automatically 
        called when creating object."""
        self.name = cardBank
        self.apr = cardApr  
        self.bal = cardBal
        # do i want to instantiate logger here or make a method...
        # or i could make a method that would write everything at once...
        

    def __str__(self):
        """String function that will print out 
        a brief description of object."""
        return "{} card has {} balance with {}% APR.\n".format(self.name, self.bal, self.apr) 
        
    def get_apr(self):
        """Return card object's apr."""
        return self.apr
    
    def get_bal(self):
        """Return card object's balance."""
        return self.bal
    
    def get_name(self):
        """Return card object's name."""
        return self.name
    
    def set_bal(self, newbal):
        """Set card balance to user's input"""
        self.bal = newbal

    def get_total_interest(self):
        """Calculates total interest charge on credit card."""
        total_interest = self.get_bal() * (self.apr / 100)
        return total_interest
    
    def get_monthly_interest(self):
        """Attempt to get what we will pay in interest on card."""
        interest = self.get_bal() * (self.get_apr() / 100) # Multiply apr by balance to get interest.
        return interest / 12
    
    def make_paymt(self, payment):
        """Method that will make a payment towards card balance."""
        # subtracts payment passed to method from total balance.
        self.bal -= payment
    
    def add_late_fee(self):
        """Add late fee to balance if client does not pay."""
        late_fee = 40
        self.bal += late_fee
        # need to implement this method with Time module in order
        # to see if card should have added late fees. 

    def get_minimum_pymt(self):
        """This will calculate monthly minimum payment on CC."""
        # monthly minimum card payment
        min_payment = (self.get_bal() * 0.01) + self.get_monthly_interest()  
        return min_payment

        return months

    def write_data(self):
        """A method that will create a file for card object
        and write information for card in a new text file."""
        filename = "{}.txt".format(self.name)
        # initialize writer object 
        writer = l(filename)
        
        # storing data in variables to write to file 
        card_data = "{} card has {} balance with {}% APR.\n".format(self.name, self.bal, self.apr) 
        writer.write_to_file(card_data)
        
        minimum_pymt = "\nYour {} card's minimum payment is {:.2f}".format(self.name, self.get_minimum_pymt())
        writer.add_to_file(minimum_pymt)
        
        time_paid_off = "\n{} card will be paid off in {} months if only min \npayment is given.".format(self.name, self.pay_off_min_payments())
        writer.add_to_file(time_paid_off)

# Tried creating a dictionary class to complement this object and store
# object's information inside a nested dictionary. I will have to
# come back with a better understanding of dictionaries for that. j