#Decode or Encode files to base64
#usage:base64.py e|d fileIn fileOut
#

import sys
import base64
import math 


def encode(fin, fout):
	open(fout, 'wb').write(base64.b64encode(open(fin).read()));

def decode(fin, fout):
	open(fout, 'wb').write(base64.b64decode(open(fin).read()));



if( len(sys.argv) != 4):
	print "Usage:base64.py e|d fileIn fileOut";
else:
	if(sys.argv[1].lower() == "e"):
		encode(sys.argv[2], sys.argv[3]);
	elif(sys.argv[1].lower() == "d"):
		decode(sys.argv[2], sys.argv[3]);
	else:
		print "Usage:base64.py e|d fileIn fileOut";


