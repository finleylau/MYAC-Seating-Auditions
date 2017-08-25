import os
import pydub
import glob

# get mp4 files from input folder
mp4_files = glob.glob('input/*.mp4')

# convert to mp3 file
for mp4 in mp4_files:
	mp3_file = 'output/' + os.path.split(os.path.splitext(mp4)[0])[1] + '.mp3'
	sound = pydub.AudioSegment.from_file(mp4)
	sound.export(mp3_file, format='mp3')

print("Conversion complete!")