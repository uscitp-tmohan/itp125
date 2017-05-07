# Name: Tanuja Mohan
# Class: ITP 125 - Hackers to CEOs
# Final Assignment - Old Spice Voicemail

#!/usr/bin/python
import getopt
import sys
import urllib
import os

soundOrder = []

def main():
	# variables that will hold user input
	gender = ''
	phone_number = ''
	reason = ''
	ending = ''
	output_filename = ''
	phone_number_valid = '0'
	reasoning_valid = '0'
	ending_valid = '0'

	# gets the command line arguments
	options, remainder = getopt.getopt(sys.argv[1:],'g:n:r:e:o')

	#used to check if all command line arguments are given and if not then error message displayed
	if len(sys.argv) < 11:
		print 'Missing command line argument'
	elif sys.argv[1] != '-g' or sys.argv[3] != '-n' or sys.argv[5] != '-r' or sys.argv[7] != '-e' or sys.argv[9] != '-o':
		print 'Incorrect command line arguments'
		print 'Make sure your order of arguments is: -g, -n, -r, -e, -o and that each argument has a value'
	else:
		#read in the arguments from the command line
		for opt, arg in options:
			if opt in ('-g'):
				gender = arg
			elif opt in ('-n'):
				phone_number = arg
				phone_number = cleanPhoneNumber(phone_number) #remove symbols
				phone_number_valid = checkPhoneNumber(phone_number) #check if number is valid
			elif opt in ('-r'):
				reason = arg
				reasoning_valid = checkReasoning(reason) #check if reason numbers are valid
			elif opt in ('-e'):
				ending = arg
				ending_valid = checkEnding(ending, gender) #check if ending numbers are valid
			elif opt in ('-o'):
				output_filename = sys.argv[10]

		#error checking for all arguments
		if gender != 'm' and gender != 'f': #gender error checking
			print 'Must select a valid gender - enter either \'m\' for male or \'f\' for female'
		elif phone_number_valid == '0': #phone number error checking
			print 'Invalid format of phone number'
			print 'Phone number must be in one of the following formats:'
			print '012-345-6789'
			print '(012) 345-6789'
			print '012.345.6789'
			print '0123456789'
		elif reason == '': #reason error checking
			print 'You must select at least 1 reason'
		elif reasoning_valid == '0':
			print 'Invalid reason argument. Make sure your reasons are between the values 0 and 4 inclusive'
		elif ending == '': #ending error checking
			print 'You must select at least 1 ending'
		elif ending_valid == '0':
			print 'Invalid ending values given'
			print 'If female, then choose either 1 or 2'
			print 'If male, then choose a value between 1 and 5 inclusive'
		else: #print a summary of the user input
			print 'Here is a summary of your inputs'
			print 'GENDER        :', gender
			print 'PHONE NUMBER  :', phone_number
			print 'REASON        :', reason
			print 'ENDING        :', ending
			print 'OUT FILE      :', output_filename
			print 'Does this summary look correct? (y/n)'
			try:
				user_input = raw_input()
			except Exception, e:
				print 'Please make sure to suround your answer with single quotes'
				cleanFolder()
				sys.exit()
			readInput(user_input, output_filename, gender, phone_number, reason, ending)

#reads the user input of 'y' or 'n' and then call generate file function
def readInput(user_input, output_filename, gender, phone_number, reason, ending):
	user_input = user_input.lower()
	if user_input == 'n':
		print 'Restarting. Use the command line to enter in your values'
		cleanFolder()
		sys.exit()
	elif user_input == 'y':
		print 'Generating your mp3 now'
		generateFile(output_filename, gender, phone_number, reason, ending)
	else:
		print 'Character not recognized. Next time please enter either \'n\' or \'y\''

#download the mp3 files needed to create the output
def generateFile(output_filename, gender, phone_number, reason, ending):
	global soundOrder
	tempFile = open(output_filename, 'w')

	#get the gender mp3 files
	if gender == 'm':
		tempFile.write('male\n')
		getMP3('m-b1-hello.mp3')
		soundOrder.append('m-b1-hello.mp3')
		getMP3('m-b2-have_dialed.mp3')
		soundOrder.append('m-b2-have_dialed.mp3')
	elif gender == 'f':
		tempFile.write('female\n')
		getMP3('f-b1-hello_caller.mp3')
		soundOrder.append('f-b1-hello_caller.mp3')
		getMP3('f-b2-lady_at.mp3')
		soundOrder.append('f-b2-lady_at.mp3')

	for n in phone_number:
		tempFile.write(n + '.mp3\n')
		getMP3(n + '.mp3')
		soundOrder.append(n + '.mp3')

	#get the reason mp3 files
	for s in reason:
		fileName = gender + '-r' + s + '-'
		if gender == 'm':
			#if statements for all numbers and then append the file name
			if s == '0':
				fileName += 'cannot_come_to_phone.mp3'
			elif s == '1':
				fileName += 'building.mp3'
			elif s == '2':
				fileName += 'cracking_walnuts.mp3'
			elif s == '3':
				fileName += 'polishing_monocole.mp3'
			elif s == '4':
				fileName += 'ripping_weights.mp3'
		elif gender == 'f':
			#if statements for all numbers and then append the file name
			if s == '1':
				fileName += 'ingesting_old_spice.mp3'
			elif s == '2':
				fileName += 'listening_to_reading.mp3'
			elif s == '3':
				fileName += 'lobster_dinner.mp3'
			elif s == '4':
				fileName += 'moon_kiss.mp3'
			elif s == '5':
				fileName += 'riding_a_horse.mp3'
			
		tempFile.write(fileName + '\n')
		getMP3(fileName)
		soundOrder.append(fileName)

	#get the ending mp3 files
	for e in ending:
		fileName = gender + '-e' + e + '-'
		if gender == 'm':
			if e == '1':
				fileName += 'horse.mp3'
			elif e == '2':
				fileName += 'jingle.mp3'
			elif e == '3':
				fileName += 'on_phone.mp3'
			elif e == '4':
				fileName += 'swan_dive.mp3'
			elif e == '5':
				fileName += 'voicemail.mp3'
		elif gender == 'f':
			if e == '1':
				fileName += 'she_will_get_back_to_you.mp3'
			elif e == '2':
				fileName += 'thanks_for_calling.mp3'
		tempFile.write(fileName + '\n')
		getMP3(fileName)
		soundOrder.append(fileName)

	tempFile.close()
	mergeSounds()

#concatenate the mp3 files
def mergeSounds():
	command = 'cat '
	for s in soundOrder:
		command += s + ' '
	command += '> output.mp3'
	os.system(command)

#get the mp3 files from the website
def getMP3(fileName):
	url = 'http://www-bcf.usc.edu/~chiso/itp125/project_version_1/' + fileName
	urllib.urlretrieve(url, fileName)

#removes symbols from the number 
def cleanPhoneNumber(phone_number):
	phone_number = phone_number.replace('(', '')
	phone_number = phone_number.replace('.', '')
	phone_number = phone_number.replace('-', '')
	return phone_number

#checks that the number is the correct length and all integers
def checkPhoneNumber(phone_number): #parantheses currently causing an error
	phone_valid = '1'
	
	if len(phone_number) != 10:
		print 'Phone number must consist of 10 integers'
		phone_valid = '0'

	for i in phone_number:
		try:
			i = int(i)
		except Exception, e:
			print 'Phone number must only consist of integers'
			phone_valid = '0'
	return phone_valid

#checks that reasons are valid numbers
def checkReasoning(reason):
	reason_valid = '1'
	reason_split = list(reason)
	for c in reason_split:
		try:
			c = int(c)
		except Exception, e:
			print 'Reasoning values must be integers'
			reason_valid = '0'
		if (c < 0 or c > 4) and reason_valid != '0':
			reason_valid = '0'
	return reason_valid

#checks that endings are valid numbers
def checkEnding(ending, gender):
	gender = gender             
	ending_valid = '1'
	ending_split = list(ending)
	if ending_split == '':
		ending_valid = '0'
	elif gender == 'm': #male has different ending numbers
		for c in ending_split:
			try:
				c = int(c)
			except Exception, e:
				print 'Ending values must be integers'
				ending_valid = '0'
			if (c < 0 or c > 5) and ending_valid != '0':
				ending_valid = '0'
	elif gender == 'f': #female has different ending numbers
		for c in ending_split:
			try:
				c = int(c)
			except Exception, e:
				print 'Ending values must be integers'
				ending_valid = '0'
			if (c < 1 or c > 2) and ending_valid != '0':
				ending_valid = '0'
	return ending_valid

#removes all the mp3s from the file
def cleanFolder():
	dirPath = os.path.dirname(os.path.abspath(__file__))
	print dirPath
	for root, dirs, files in os.walk(dirPath):
		for currentFile in files:
				exts = ('.mp3', '.txt')
				if any(currentFile.lower().endswith(ext) for ext in exts):
					os.remove(os.path.join(root, currentFile))

if __name__ == '__main__':main()







