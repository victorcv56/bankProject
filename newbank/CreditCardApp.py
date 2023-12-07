from newCard import bankCards as cc
from cards_dictionary import cardList as li


barclays = cc("Barclays", 29.99, 1511.65)
print(barclays)
# card_list.append(barclays) # add card object to list

wells = cc("Wells", 19.24, 10141.16)
print(wells)
# card_list.append(wells) # add card object to list

amazon = cc("Amazon", 27.49, 6748.22)
print(amazon)
# card_list.append(amazon) # add card object to list


# card_dict = li() # initializing dictionary
# print("type of card_dict is: ", end='')
# print(type(card_dict))



print("")
wells_interest = "{} card total interest: ${:.2f}".format(wells.name, wells.get_total_interest())
print(wells_interest)

barclays_interest = "{} card total interest: ${:.2f}".format(barclays.name, barclays.get_total_interest())
print(barclays_interest)

amazon_interest = "{} card total interest: ${:.2f}".format(amazon.name, amazon.get_total_interest())
print(amazon_interest)

amazon.write_data()
barclays.write_data()
wells.write_data()

amazon_apr = "{}'s APR: {}%".format(amazon.name, amazon.apr)
print(amazon_apr)

