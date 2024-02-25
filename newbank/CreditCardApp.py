from newCard import bankCards as cc
from create_dictionary import cardList as li
import payOffCard

# need new ideas for credit card project in order to be able to advance 
# it further with better ideas and not just basic python.

card_list = [] # instantiating empty list to fill with card objects

number_of_cards = int(input('Please enter how many cards you would like to input: '))

# for loop which will take input from user and automatically
# create card objects to add to list.
for card in range(number_of_cards):
    card_name = input('Name of card: ').capitalize()
    card_apr = input('Card APR: ')
    card_bal = input('Card balance: ')
    print() # print an empty line for easy readability

    # using float conversion for card numbers to make
    # calculations possible
    card_obj = cc(card_name, float(card_apr), float(card_bal))
    # add card object to list
    card_list.append(card_obj)

# initializing create_dictionary class
card_dict = li() 

# create dictionary by passing list of cards to dictionary class
card_dict.add_to_nested(card_list) 
card_dict.show_dictionary()

print("------------------------------")

# for loop reads card object and displays information for user
# on total interest to pay on cards
for card in card_list:
    print("{} card total interest: ${:.2f}".format(card.name, card.get_total_interest()))    
    # write info data of cards into .txt file
    card.write_data()
