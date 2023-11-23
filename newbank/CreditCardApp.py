from newCard import bankCards as cc
from writer import logger as l

barclays = cc("Barclays", 29.99, 1511.65)
print(barclays)
wells = cc("Wells Fargo", 19.24, 10141.16)
print(wells)
amazon = cc("Amazon", 27.49, 6748.22)
print(amazon)

print("")
wells_interest = wells.get_total_interest()
print(wells_interest)

barclays_interest = barclays.get_total_interest()
print(barclays_interest)

amazon_interest = amazon.get_total_interest()
print(amazon_interest)


print("")
prompt = input("Would you like to create a new file(y/n):\n ")

if prompt == 'y':
    filename = input("Please enter name of file: ")
    fo = l(filename)
    fo.create_new_file()
else:
    filename = input("Please enter name of existing file:\n ")
    fo = l(filename)

fo.add_to_file(wells_interest)
fo.add_to_file(amazon_interest)
fo.add_to_file(barclays_interest)
#fo.write_to_file(barclays_interest) # write_to_file method will overwrite all data...
fo.read_from_file()