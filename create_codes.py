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

		elif string.capwords(row['Orchestra']) == 'Symphony':
			# assign code
			code_assignment = symphony_instrument_codes[string.capwords(row['Instrument'])]
			symphony_codes_counter[code_assignment] += 1
			row['Code'] = code_assignment + str(symphony_codes_counter[code_assignment])
			
			# write to files
			codes_file.write(row['Code'] + '\n')
			writer.writerow(row)