from newBank import bankCards as creditCard

barclays = creditCard("Barclays", 29.99, 1511.65)
print(barclays)
wells = creditCard("Wells Fargo", 19.24, 9942.73)
print(wells)

wells_interest = wells.get_monthly_interest()
print("{:.2f}".format(wells_interest))
wells.pay_off_in_given_time()