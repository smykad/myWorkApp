import csv
from datetime import date

def myData(myFile):
    """Function to read data from CSV and returns 3 lists."""
    with open(myFile) as f: # Open CSV file
        reader = csv.reader(f)  # Read CSV File
        rooms = []
        for row in reader:
            try: 
                room = int(row[4])  # get room number
               
                rooms.append(room)  # append rooms to list

            except ValueError:
                pass
        return rooms # Return the lists

def myRooms(myList1, f):
    """Method to write data to text file."""
    cBox = '☐'
    if len(myList1) > 0:
        for i in range(len(myList1)):
            if i > 0 and i % 5 == 0:
                f.write('\n')
                f.write(f'\t\tRoom: {myList1[i]}\t\t{cBox}\n')
            else:
                f.write(f'\t\tRoom: {myList1[i]}\t\t{cBox}\n')

today = date.today()
cBox = '☐'
eBox = cBox.encode("utf8")
myFile = 'data/Book3.csv' # CSV File


rooms = myData(myFile)

# Set a header displaying total arrivals and the date
arrival = f'  \t  In House Guests   {today}'
# get the length of the the arrival message and multiply by 1.5
mult = len(arrival)
mult *= 1.5
# round the multiplyer to 0 decimals
x = round(mult, 0)
# Generate a seperator for formatting 
seperator = '*'*int(x)
# add a new line to seperator
seperator += '\n'
# add formatting to arrival
arrival += '\n' 

with open('inHouse.txt', 'w', encoding="utf-8") as f:
    f.write(seperator)
    f.write(arrival)
    f.write(seperator)
    myRooms(rooms, f)