from helpers import *

# tell program where to save files
print("Working...")

# open csv file called "roster" with last names, first names, orchestra name, and instruments
csv_path = 'Roster.csv'
with open(csv_path, 'r') as roster:
	readRoster(roster)

# generates codes in folders
codes = []
file = open('codes.txt', 'r')
for line in file:
	if not line.isspace():
		codes.append(line.strip())

# make folders
makeInstrumentFolders(codes)

print()
print("Success!")