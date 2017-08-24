import os

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
	
	# creates first half of path (example: C:\Users\finle\Dropbox)
	dropbox_location = 'C:\\Users\\finle\\Dropbox\\'

	# creates last half of path (example: Concert Seating Auditions\Violin)
	if code_prefix[0] == 'c':
		instrument = concert_codes[code_prefix]
		orchestra_folder = 'Concert Seating Auditions\\'
	elif code_prefix[0] == 's':
		instrument = symphony_codes[code_prefix]
		orchestra_folder = 'Symphony Seating Auditions\\'


	return (dropbox_location + orchestra_folder + instrument + '\\' + code)