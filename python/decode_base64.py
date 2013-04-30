import sys
import base64
import math 

#arg1 is file in base 64, arg2 is decode file

f = open(sys.argv[1]).read()
open(sys.argv[2], 'wb').write(base64.b64decode(f))


