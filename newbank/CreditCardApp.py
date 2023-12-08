from newCard import bankCards as cc
from cards_dictionary import cardList as li

card_list = [] # new card list holding objects

barclays = cc("Barclays", 29.99, 1511.65)
card_list.append(barclays) # add card object to list

wells = cc("Wells", 19.24, 10141.16)
card_list.append(wells) # add card object to list

amazon = cc("Amazon", 27.49, 6748.22)
card_list.append(amazon) # add card object to list

card_dict = li() # initializing dictionary
card_dict.add_to_nested(card_list)
card_dict.show_dictionary()


print("")
# Calculates card's interest using class method, 
# then displays it for user
wells_interest = "{} card total interest: ${:.2f}".format(wells.name, wells.get_total_interest())
print(wells_interest)

barclays_interest = "{} card total interest: ${:.2f}".format(barclays.name, barclays.get_total_interest())
print(barclays_interest)

amazon_interest = "{} card total interest: ${:.2f}".format(amazon.name, amazon.get_total_interest())
print(amazon_interest)

amazon.write_data() # writes data to .txt file
barclays.write_data() # writes data to .txt file
wells.write_data() # writes data to .txt file

amazon_apr = "{}'s APR: {}%".format(amazon.name, amazon.apr)
print(amazon_apr)

# Add time methods? learn python time lib to be able to assimilate to 
# an actual app that keeps track of time to be able to use missed payment
# and late fees. 