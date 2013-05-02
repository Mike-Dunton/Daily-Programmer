###############################################################################
#On standard input, you will be given two strings in quotes:
#the first will be the text file location, with the second
#being which format you want it output to.
#Note that this second string will always either be "Windows" or "Unix".
#Windows line endings will always be CR+LF (carriage-return and then newline),
#while Unix endings will always be just the LF (newline character).
###############################################################################

import sys
import os.path

def getMode(fileInput):
	if(fileInput.lower() == "windows"):
		return 0;
	elif(fileInput.lower() == "unix"):
		return 1;
	else:
		return -1;

def run(txtf, mode):
	with open(txtf, 'r') as f:
		line = f.read();
		if(mode == 0):
			print line.replace("\n", "\r\n");
		if(mode == 1):
			print line.replace("\r\n", "\n");
		if(mode == -1):
			sys.exit(mode);

if(len(sys.argv) != 3):
	print "Usage: newLinesTrouble.py /path/to/file.txt unix|windows"
else:
	if(os.path.isfile(sys.argv[1])):
		run(sys.argv[1], getMode(sys.argv[2]));
	else:
		print "That file doesn't exist!";



 
