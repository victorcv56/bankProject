def pay_off_min_payments(card):
    """Loop that will pay off credit card and return months taken to pay off debt
    only giving minimum payments to card."""
    months = 0
    temp_bal = card.get_bal()
    min_payment = card.get_minimum_pymt()
    # while loop that will run until balance is paid off
    while temp_bal >= 100: 
        # calls on the make payment method to simulate a payment being made            
        temp_bal -= min_payment
        # will add monthly fee on credit card
        temp_bal += card.get_monthly_interest(temp_bal)
        # add 1 every iteration to months var to simulate monthly payments
        months += 1
        # print('Remaining balance: {:.2f}'.format(card.bal))
            
    return months
    

def pay_off_in_given_time(card):
    """Method will return how much user will have to pay monthly
    if they want to pay off debt in given amount of time."""
    
    months = int(input("Time needed to pay off {} card(months): ".format(card.name)))
    temp_bal = card.get_bal()
    # user will be asked for months(int) needed to pay off card
    pymt = (temp_bal / months) + card.get_monthly_interest()
    # payment will be calculated by dividing balance by months given
    # and add monthly interest
    for month in range(months):
        temp_bal -= pymt 
        # makes payment towards balance
        print("Made payment of {:.2f}, balance is now: {:.2f}".format(pymt, temp_bal))
        temp_bal += card.get_monthly_interest() 
        # adds in monthly interest fee every iteration
        print("Added {:.2f} interest charge to balance. Balance is now: {:.2f}\n".format(card.get_monthly_interest(), temp_bal))
        if temp_bal < pymt:
            print("If {:.2f} is paid monthly towards {} card, it will take "
                "{} months to pay off.".format(pymt, card.name, month))
            break


def payOffFirst(cards):
    """Method will compare card APRs and decide which one user should 
    pay off first."""
    # temporary apr to store highest apr from list of cards
    temp_apr = 0    
    # for loop that will compare different card apr's and find the max
    for card in cards:
        if card.apr > temp_apr:
            temp_apr = card.apr
    print("Highest APR is: {}%".format(temp_apr))

    # for loop will find matching apr and print out which card it belongs to
    for card in cards:
        if temp_apr == card.apr:
            print("Pay off {} card first.".format(card.name))
            card.pay_off_in_given_time()
