import json # import to write dicitonary to .txt 
"""An attempt to create a filewriter object to be able to document all credit card objects."""

class logger:
    """Will contain different method to which we will be able to write and 
    append to new files our data."""

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

