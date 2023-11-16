"""An attempt to create a filewriter object to be able to document all credit card objects."""

class logger:
    """Will contain different method to which we will be able to write and 
    append to new files our data."""

    def __init__(self, filename):
        """Initializes object and lets user know."""
        self.filename = filename
        print("Initializing writer method.")

    def create_new_file(self):
        """Create a new file to write to. 
        Will overwrite any information on file."""
        f = open(self.filename, "x")
        f.close()
        return f
    
    def write_to_file(self, data):
        """Write info to file."""
        f = open(self.filename, 'w')
        f.write(data)


newLog = logger("newfile.txt")
newLog.write_to_file()
