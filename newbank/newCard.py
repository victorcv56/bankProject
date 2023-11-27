from writer import logger as l
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
        
    
    def get_total_interest(self):
        """Calculates total interest charge on credit card."""
        total_interest = self.bal * (self.apr / 100)
        # return "Total interest on {} card is {:.2f}".format(self.name, total_interest)
        return total_interest
    
    def get_monthly_interest(self):
        """Attempt to get what we will pay in interest on card."""
        interest = self.bal * (self.apr / 100) # Multiply apr by balance to get interest.
        #print("You will pay a total of {:.2f} monthly interest.".format(interest / 12))
        return interest / 12
    
    def make_paymt(self, payment):
        """Method that will make a payment towards card balance."""
        # payment = int(input("Payment amount: "))
        self.bal -= payment
        # print("{:.2f} paid towards card. \nNew balance is {:.2f}".format(payment, self.bal))    
    
    def add_late_fee(self):
        """Add late fee to balance if client does not pay."""
        late_fee = 40
        self.bal += late_fee

    def get_minimum_pymt(self):
        """This will calculate monthly minimum payment on CC."""
        fee = (self.bal * 0.01) + self.get_monthly_interest()  #monthly interest paid
        print("minimum payment will be {:.2f}".format(fee))
        return fee

    def pay_off_min_payments(self):
        """Loop that will pay off credit card and return months taken to pay off debt
        only giving minimum payments to card."""
        months = 0
        min_payment = self.get_minimum_pymt()
        while self.bal >= 100: 
            # while loop that will run until balance is paid off
            self.make_paymt(min_payment) 
            # calls on the make payment method to simulate a payment being made
            self.bal += self.get_monthly_interest()
            # will add monthly fee on credit card
            months += 1
            # print('Remaining balance: {:.2f}'.format(self.bal))
            
        return months

    def pay_off_in_given_time(self):
        """Method will return how much user will have to pay monthly
        if they want to pay off debt in given amount of time."""
        months = int(input("Time needed to pay off card(months): "))
        pymt = (self.bal / months) + self.get_monthly_interest()
        for month in range(months):
            self.bal -= pymt # makes payment towards balance
            # print("Made payment of {:.2f}, balance is now: {:.2f}".format(pymt, self.bal))
            self.bal += self.get_monthly_interest() # adds in monthly interest fee
            # print("Added {:.2f} interest charge to balance. Balance is now: {:.2f}\n".format(self.get_monthly_interest(), self.bal))
            if self.bal < pymt:
                print("If {:.2f} is paid monthly towards {} card, it will take "
                      "{} months to pay off.".format(pymt, self.name, month))
                break

    def write_data(self):
        """A method that will create a file for card object
        and write information for card in a new text file."""
        filename = "{}.txt".format(self.name)
        # initialize writer object 
        writer = l(filename)
        
        # storing data in variables to write to file 
        data = "{} card has {} balance with {}% APR.\n".format(self.name, self.bal, self.apr) 
        writer.write_to_file(data)

        minimum_pymt = "\nYour {} card's minimum payment is {:.2f}".format(self.name, self.get_minimum_pymt())
        writer.add_to_file(minimum_pymt)

        more_data = "\n{} card will be paid off in {} months if only min \npayment is given.".format(self.name, self.pay_off_min_payments())
        writer.add_to_file(more_data)
        
        
        

        
# This class only has to have methods that pertain to things a credit card
# can do or can be done to like getting certain calculations nd
# showing different traits
