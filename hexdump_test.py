import os
import sys
from subprocess import call
import os
from subprocess import Popen, PIPE

def getHexDump(execPath):

	# Define hexdump command and its arguments. Importantly, we need to define its format for outputting hex.
	command = 'hexdump -v -e \' "0x" 1/1 "%02X" "," \' ' + execPath

	# Use Popen() in order to run hexdump and grab the hexadecimal bytes of the program. Without shell=True, Popen crashes, even though we don't use the shell.
	hexDump = Popen(command, stdout=PIPE, stderr=None, shell=True)

	# Capture standard output and error streams from PIPE to to subprocess. This makes it blocking.
	stdout, stderr = hexDump.communicate()

	# If hexdump ran successfully, return the string retrieved witout a trailing comma ([:-1]). Otherwise, return None.
	if stderr == None:
		return stdout[:-1]
	else:
		return None


print getHexDump('/bin/pwd')
print getHexDump('/bin/ls')




