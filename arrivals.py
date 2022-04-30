import csv, os, msvcrt
from datetime import timedelta, date


def myData(myFile):
    """Function to read data from CSV and returns 3 lists."""
    with open(myFile) as f: # Open CSV file
        reader = csv.reader(f)  # Read CSV File
        nights, rooms, names = [], [], []   # retrieve nights, rooms, names
        duplicates = 0
        for row in reader:
            try:
                if int(row[6]) in rooms or row[0] == 'UNKNOWN, UNKNOWN': # catches duplicate rooms
                    duplicates += 1
                    pass
                else:
                    night = int(row[5]) # get length of stay
                    room = int(row[6])  # get room number
                    nights.append(night)    # append nights to list
                    rooms.append(room)  # append rooms to list
                    name = row[0]   # get names
                    names.append(name)  # append names to list
            except ValueError:
                pass
        return nights, rooms, names, duplicates # Return the lists

def myNames(myList, myInt):
    """Function to get split first and last names."""
    rets = []   # return
    for i in range(len(myList)):    # Iterate throught list
        ret = myList[i].split()[myInt].replace(',','').title()  # split first/last name, remove commas, format text
        rets.append(ret)    # add either first or last name to a list
    return rets # return the list
def myBreakfast(myList):
    """Function to get total number of nights."""
    ret = 0
    for i in range(len(myList)):
        ret += myList[i]
    return ret
def header(seperator, myString, f):
    """Creates a formatted header that takes in a string paramater."""
    f.write(seperator)
    f.write(f'\t\t{myString}\n')
    f.write(seperator)


def myRooms(myList1, myList2, myList3, myList4, f):
    """Method to write data to text file."""
    if len(myList1) > 0:
        f.write(f'\tRoom\tDeparture\tGuest Name\n\n')
        for i in range(len(myList1)):
            if i > 0 and i % 5 == 0:
                f.write('\n')
                f.write(f'\t{myList1[i]}\t{myList2[i]}\t{myList3[i]} {myList4[i]}\n')
            else:
                f.write(f'\t{myList1[i]}\t{myList2[i]}\t{myList3[i]} {myList4[i]}\n')

def setMyDate(myInt):
    today = date.today() + timedelta(days=myInt)
    return today

def createFile(myFile, myInt):
    # Set the date, 0 if you're doing for today, 1 for tomorrow, etc
    today = setMyDate(myInt)
    # Make lists retrieved from file
    nights, rooms, names, duplicates = myData(myFile)

    # Make a list for first and last names
    lastNames, firstNames = myNames(names, 0), myNames(names, 1)

    # Get total number of nights
    totalNights = myBreakfast(nights)

    # Get total number of rooms
    totalRooms = len(rooms)

    # Lists to append to for sorting the data
    oneNightStays, twoNightStays, threeNightStays, extendedStays = [], [], [], []
    oneNightRooms, twoNightRooms, threeNightRooms, extendedRooms = [], [], [], []
    oneNightLNames, twoNightLNames, threeNightLNames, extendedLNames = [], [], [], []
    oneNightFNames, twoNightFNames, threeNightFNames, extendedFNames = [], [], [], []

    # iterate through the data
    # Seperate the data based on number of nights staying
    # 1 night, 2 night, 3 nights or more than 3 nights
    for night in range(len(nights)):
        match nights[night]:
            case 1:
                departureDate = str(today + timedelta(days=nights[night]))
                room = rooms[night]
                lName = lastNames[night]
                fName = firstNames[night]
                oneNightStays.append(departureDate)
                oneNightRooms.append(room)
                oneNightLNames.append(lName)
                oneNightFNames.append(fName)
            case 2:
                departureDate = str(today + timedelta(days=nights[night]))
                room = rooms[night]
                lName = lastNames[night]
                fName = firstNames[night]
                twoNightStays.append(departureDate)
                twoNightRooms.append(room)
                twoNightLNames.append(lName)
                twoNightFNames.append(fName)
            case 3:
                departureDate = str(today + timedelta(days=nights[night]))
                room = rooms[night]
                lName = lastNames[night]
                fName = firstNames[night]
                threeNightStays.append(departureDate)
                threeNightRooms.append(room)
                threeNightLNames.append(lName)
                threeNightFNames.append(fName)
            case _:
                departureDate = str(today + timedelta(days=nights[night]))
                room = rooms[night]
                lName = lastNames[night]
                fName = firstNames[night]
                extendedStays.append(departureDate)
                extendedRooms.append(room)
                extendedLNames.append(lName)
                extendedFNames.append(fName)
                
    
    # Set a header displaying total arrivals and the date
    arrival = f'  \t  Arrivals: {totalRooms}  Date:  {today}'

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
    arrival += '\n\n'
    
    # Getting the number of stays for the lists so I can know if it's 0 or not
    myOnes = len(oneNightRooms)
    myTwos = len(twoNightRooms)
    myThrs = len(threeNightRooms)
    myExts = len(extendedRooms)

    # Here we create the text file using the methods from the top
    with open('arrivals.txt', 'w') as f:
        f.write(arrival)
        if myOnes > 0:
            header(seperator, f'One night stays: {myOnes}', f)
            myRooms(oneNightRooms, oneNightStays, oneNightFNames, oneNightLNames, f)
        if myTwos > 0:
            header(seperator, f'Two night stays: {myTwos}', f)
            myRooms(twoNightRooms, twoNightStays, twoNightFNames, twoNightLNames, f)
        if myThrs > 0:
            header(seperator, f'Three night stays: {myThrs}', f)
            myRooms(threeNightRooms, threeNightStays, threeNightFNames,threeNightLNames, f)
        if myExts > 0:
            header(seperator, f'Extended stays: {myExts}', f)
            myRooms(extendedRooms, extendedStays, extendedFNames, extendedLNames, f)
        header(seperator, f'Breakast Forms Needed: {totalNights}', f)
        if duplicates > 0:
            header('\n', f'Duplicate rooms found: {duplicates}', f)

def isValidInt():
    """Function to determine if valid int and if its within a valid range of 0 to 1"""
    isItInt = False
    while isItInt is False:
        ret = input()
        try:
            int(ret)
            isItInt = True
        except ValueError:
            print("Please enter a digit", end=': ')
        match int(ret):
            case 0:
                isItInt = True
            case 1:
                isItInt = True
            case _:
                isItInt = False
                print('Enter either 0 or 1', end=': ')

    return ret

def isValidFile():
    """Determines if CSV file exists"""
    myBool = False
    while myBool is False:
        ret = 'data/' # Set folder location
        ret += input()  # concantnate the filename to the path
        ret += '.csv'
        try:
            open(ret, "r")
            myBool = True
        except IOError:
            print("Error: File does not appear to exist, enter valid file", end=': ')
    return ret

def myChoice(myInt):
    """Function to determine if doing arrivals for today or tomorrow"""
    match int(myInt):
        case 0:
            ret = 'today\'s'
        case 1:
            ret = 'tomorrow\'s'
    return ret
             

def main():
    """Main Method for the script to take user input, validate and create a file"""
    print('Enter file name', end=': ')
    myFile = isValidFile()
    print('Type 0 if doing arrivals for today or 1 for tomorrow: ', end='')
    ret = isValidInt()
    myString = myChoice(ret)
    print(f'Creating {myFile} for {myString} arrivals')
    createFile(myFile, int(ret))
    print('File has been written, press any key to print') 
    msvcrt.getch() # waits for 1 key to be pressed
    os.startfile("arrivals.txt", "print") # Prints the file that was created
    
main()
# EOF