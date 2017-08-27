from helpers import *

# tell program where to save files
user = input('Enter user name from C:\\Users\\XXXX\\Dropbox\\ (type what is in place of XXXX)): ')
print()
print("Working...")

# open csv file called "roster" with last names, first names, orchestra name, and instruments
csv_path = 'Roster.csv'
with open(csv_path, 'r') as roster:
	readRoster(roster, user)

# generates codes in folders
codes = []
file = open('codes.txt', 'r')
for line in file:
	if not line.isspace():
		codes.append(line.strip())

# make folders
makeInstrumentFolders(codes, user)

print()
print("Success!")