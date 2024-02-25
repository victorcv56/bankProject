class payOffCard():
    """Branching out methods inside card creation class and placing
    them here for better code readability."""
    
    
    def pay_off_min_payments(self):
        """Loop that will pay off credit card and return months taken to pay off debt
        only giving minimum payments to card."""
        months = 0
        temp_bal = self.get_bal()
        min_payment = self.get_minimum_pymt()
        # while loop that will run until balance is paid off
        while temp_bal >= 100: 
            # calls on the make payment method to simulate a payment being made            
            temp_bal -= min_payment
            # will add monthly fee on credit card
            temp_bal += self.get_monthly_interest(temp_bal)
            # add 1 every iteration to months var to simulate monthly payments
            months += 1
            # print('Remaining balance: {:.2f}'.format(self.bal))
            
        return months
    

    def pay_off_in_given_time(self):
        """Method will return how much user will have to pay monthly
        if they want to pay off debt in given amount of time."""
        
        months = int(input("Time needed to pay off {} card(months): ".format(self.name)))
        temp_bal = self.get_bal()

        # user will be asked for months(int) needed to pay off card
        pymt = (temp_bal / months) + self.get_monthly_interest()
        # payment will be calculated by dividing balance by months given
        # and add monthly interest
        for month in range(months):
            temp_bal -= pymt 
            # makes payment towards balance
            print("Made payment of {:.2f}, balance is now: {:.2f}".format(pymt, temp_bal))
            temp_bal += self.get_monthly_interest() 
            # adds in monthly interest fee every iteration
            print("Added {:.2f} interest charge to balance. Balance is now: {:.2f}\n".format(self.get_monthly_interest(), temp_bal))
            if temp_bal < pymt:
                print("If {:.2f} is paid monthly towards {} card, it will take "
                    "{} months to pay off.".format(pymt, self.name, month))
                break


    