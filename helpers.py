import csv
import string
import os

# reads roster as a csv file
def readRoster(roster):

	reader = csv.DictReader(roster, delimiter=',')

	# create instrument codes dictionary
	concert_instrument_order = ['Violin 1', 'Violin 2', 'Viola', 'Cello', 'Bass', 'Flute', 'Oboe', 'Clarinet', 'Bassoon', 'Horn', 'Trumpet', 'Trombone', 'Tuba', 'Percussion']
	concert_instrument_letter = ['caa', 'cab', 'cb', 'cc', 'cd', 'ce', 'cf', 'cg', 'ch', 'ci', 'cj', 'ck', 'cl', 'cm']
	concert_instrument_codes = {}
	for i in range(len(concert_instrument_order)):
		concert_instrument_codes[concert_instrument_order[i]] = concert_instrument_letter[i]

	symphony_instrument_order = ['Violin 1', 'Violin 2', 'Viola', 'Cello', 'Bass', 'Flute', 'Oboe', 'Clarinet', 'Bassoon', 'Horn', 'Trumpet', 'Trombone', 'Tuba', 'Percussion']
	symphony_instrument_letter = ['saa', 'sab', 'sb', 'sc', 'sd', 'se', 'sf', 'sg', 'sh', 'si', 'sj', 'sk', 'sl', 'sm']
	symphony_instrument_codes = {}
	for i in range(len(symphony_instrument_order)):
		symphony_instrument_codes[symphony_instrument_order[i]] = symphony_instrument_letter[i]

	# create counter codes dictionary
	concert_codes_counter = {}
	symphony_codes_counter = {}
	for i in range(len(concert_instrument_letter)):
		concert_codes_counter[concert_instrument_letter[i]] = 0
	for i in range(len(symphony_instrument_letter)):
		symphony_codes_counter[symphony_instrument_letter[i]] = 0

	# delete output files they already exist
	if os.path.isfile('codes.txt'):
		os.remove('codes.txt')
	if os.path.isfile('assignedcodes.csv'):
		os.remove('assignedcodes.csv')

	# open files in write mode
	codes_file = open('codes.txt', 'w')
	assignedcodes_file = open('assignedcodes.csv','w', newline='')
	fieldnames = ['Last Name', 'First Name', 'Orchestra', 'Instrument', 'Code']
	writer = csv.DictWriter(assignedcodes_file, fieldnames = fieldnames)
	writer.writeheader()
	

	# for each person, assign them a code, then print code to an output file called codes.txt and print entire file to an output file called assignedcodes.csv
	for row in reader:
		if string.capwords(row['Orchestra']) == 'Concert':
			# assign code
			code_assignment = concert_instrument_codes[string.capwords(row['Instrument'])]
			concert_codes_counter[code_assignment] += 1
			row['Code'] = code_assignment + str(concert_codes_counter[code_assignment])
			
			# write to files
			codes_file.write(row['Code'] + '\n')
			writer.writerow(row)
			makeStudentFolder(row)

		elif string.capwords(row['Orchestra']) == 'Symphony':
			# assign code
			code_assignment = symphony_instrument_codes[string.capwords(row['Instrument'])]
			symphony_codes_counter[code_assignment] += 1
			row['Code'] = code_assignment + str(symphony_codes_counter[code_assignment])
			
			# write to files
			codes_file.write(row['Code'] + '\n')
			writer.writerow(row)
			makeStudentFolder(row)

# creates individualized folder path
def makeStudentFolder(student):

	path = os.path.join("Seating Audition Folders with Names", string.capwords(student['Orchestra']), string.capwords(student['Instrument']), string.capwords(student['Last Name']) + ", " + string.capwords(student['First Name']))
	if not os.path.exists(path):
		os.makedirs(path)

# takes in a list of codes as a input and creates folders for each code
def makeInstrumentFolders(codes):

	# create dictionary for concert order
	concert_instrument_order = ['Violin 1', 'Violin 2', 'Viola', 'Cello', 'Bass', 'Flute', 'Oboe', 'Clarinet', 'Bassoon', 'Horn', 'Trumpet', 'Trombone', 'Tuba', 'Percussion']
	concert_instrument_letter = ['caa', 'cab', 'cb', 'cc', 'cd', 'ce', 'cf', 'cg', 'ch', 'ci', 'cj', 'ck', 'cl', 'cm']
	concert_instrument_codes = {}
	for i in range(len(concert_instrument_order)):
		concert_instrument_codes[concert_instrument_letter[i]] = concert_instrument_order[i]

	symphony_instrument_order = ['Violin 1', 'Violin 2', 'Viola', 'Cello', 'Bass', 'Flute', 'Oboe', 'Clarinet', 'Bassoon', 'Horn', 'Trumpet', 'Trombone', 'Tuba', 'Percussion']
	symphony_instrument_letter = ['saa', 'sab', 'sb', 'sc', 'sd', 'se', 'sf', 'sg', 'sh', 'si', 'sj', 'sk', 'sl', 'sm']
	symphony_instrument_codes = {}
	for i in range(len(symphony_instrument_order)):
		symphony_instrument_codes[symphony_instrument_letter[i]] = symphony_instrument_order[i]

	# iterate through codes list and for each code, make a file path and create a directory if it doesnt exist
	for code in codes:
		code_path = makeCodeFilePath(code, concert_instrument_codes, symphony_instrument_codes)
		if not os.path.exists(code_path):
			os.makedirs(code_path)

# takes in a code from list of codes, and then two dictionaries containing the codes and corresponding instrument values for Concert and Symphony
def makeCodeFilePath(code, concert_codes, symphony_codes):

	# strips off numbers in code to just leave the prefix (example: saa1 becomes saa)
	code_prefix = ''.join([i for i in code if not i.isdigit()])
	
	# creates last half of path (example: Concert Seating Auditions\Violin)
	if code_prefix[0] == 'c':
		instrument = concert_codes[code_prefix]
		orchestra_folder = 'Concert Seating Auditions'
	elif code_prefix[0] == 's':
		instrument = symphony_codes[code_prefix]
		orchestra_folder = 'Symphony Seating Auditions'


	return os.path.join(orchestra_folder, instrument, code)