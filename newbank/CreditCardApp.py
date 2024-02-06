from newCard import bankCards as cc
from cards_dictionary import cardList as li

# need new ideas for credit card project in order to be able to advance 
# it further with better ideas and not just basic python.

card_list = [] # instantiating empty list to fill with card objects

number_of_cards = int(input('Please enter how many cards you would like to input: '))

# for loop which will take input from user and automatically
# create card objects to add to list.
for card in range(number_of_cards):
    card_name = input('Name of card: ')
    card_apr = input('Card APR: ')
    card_bal = input('Card balance: ')
    print() # print an empty line for easy readability

    # using float conversion for card numbers to make
    # calculations possible
    card_obj = cc(card_name, float(card_apr), float(card_bal))
    # add card object to list
    card_list.append(card_obj)
    

card_dict = li() # initializing dictionary class

# use list of cards to instantiate imported dictionary class.
card_dict.add_to_nested(card_list) 
card_dict.show_dictionary()


print("")

# for loop reads card object and displays information for user
# on total interest to pay on cards
for card in card_list:
    print("{} card total interest: ${:.2f}".format(card.name, card.get_total_interest()))
    # write info data of cards into .txt file
    card.write_data()

# amazon_apr = "{}'s APR: {}%".format(amazon.name, amazon.apr)
# amazon_apr = amazon.get_apr()
# print(amazon_apr)


def payOffFirst(cards):
    """Method will compare card APRs and decide which one user should 
    pay off first."""
    temp_apr = 0
    for card in cards:
        # temp_apr = 0
        if card.apr > temp_apr:
            temp_apr = card.apr
    print("Highest APR is: {}%".format(temp_apr))

    for card in cards:
        if temp_apr == card.apr:
            print("Pay off {} card first.".format(card.name))


payOffFirst(card_list)
# Add time methods? learn python time lib to be able to assimilate to 
# an actual app that keeps track of time to be able to use missed payment
# and late fees. 