import json # import to write dicitonary to .txt 
import payOffCard
# from newCard import bankCards as card
"""An attempt to create a filewriter object to be able to document all credit card objects."""

class data_writer:
    """Will contain different method to which we will be able to write and 
    append to new files our data.
    This will write data to a JSON file in order to have access to python
    dictionary containing data on diferent credir card objects."""

    def __init__(self, filename):
        """Initializes object and lets user know."""
        self.filename = filename
        # print("Initializing writer method.")

    def create_new_file(self):
        """Asks user if they want to create a new file to write to."""
        f = open(self.filename, 'x')
        print("Created new file {}.".format(self.filename))
        f.close()
    
    def write_dictionary(self, dictionary):
        """Write dictionary to JSON into .txt"""
        with open(self.filename, 'w') as fo:
            for cards in dictionary.items():
                fo.write(json.dumps(cards) + "\n")

    def write_to_file(self, data):
        """Write info to file, overwriting other data."""
        f = open(self.filename, 'w')
        f.write(data)
        f.close()

    def add_to_file(self, data):
        "Appends data to existing file."
        f = open(self.filename, 'a')
        f.write(data + "\n")
        f.close()

    def read_from_file(self):
        """Will read data from file."""
        f = open(self.filename, 'r')
        print(f.read())
        f.close()

    def write_data(self, card):
        
        """A method that will create a file for card object
        and write information for card in a new text file."""
        # initialize writer object 
        
        # storing data in variables to write to file 
        card_data = "{} card has {} balance with {}% APR.\n".format(card.get_name(), card.get_bal(), card.get_apr()) 
        self.write_to_file(card_data)
        
        minimum_pymt = "\nYour {} card's minimum payment is {:.2f}".format(card.get_name(), card.get_minimum_pymt())
        self.add_to_file(minimum_pymt)
        
        time_paid_off = "\n{} card will be paid off in {} months if only min \npayment is given.".format(card.get_name(), payOffCard.pay_off_min_payments())
        self.add_to_file(time_paid_off)