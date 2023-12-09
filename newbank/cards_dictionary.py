import pprint
from writer import logger as log
"""Creating a dictionary of credit cards to manipulate data"""

class cardList:
    """List of credit cards so it can be used to compare info"""

    def __init__(self):
        """Initializes an empty dictionary that will be filled
        by user."""
        # self.card_list = card_list
        self.cards = {}

    def add_to_nested(self, card_list): 
        """Try to add to nested dictionary."""
        for card in card_list:
            # initialize and fill parameters..
            card_apr = card.get_apr()
            card_bal = card.get_bal()
            card_name = card.get_name()
            new_Card = {card_name: {'apr': card_apr, 'balance': card_bal}} 
            self.cards.update(new_Card)

        logger = log('cardList.json')
        logger.write_dictionary(self.cards)

    def show_dictionary(self):
        """Print dictionary to screen."""
        pprint.pprint(self.cards)    
    