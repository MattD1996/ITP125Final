import md5
from itertools import permutations
from string import ascii_letters
from string import digits
from string import punctuation
import itertools
import time

#reads in all the unhashed passwords, hashes them and sends them to the
#md5 password brute forcer
def runthroughPasswordsInFile(document):
    try:
        readfile = open(document,"r")
		#reads through each word in the file, prints it out and sends it to
		#the password cracker
        for line in readfile:
			word = line.rstrip()
			#print "The original word is: " + word
			hashedWord = md5.new(word).hexdigest()
			md5breaker(hashedWord)
        readfile.close()
    except IOError:
		print "The file name your entered doesn't exist in your current directory. Please re-run the program and try again"

#cracks the hashed password by the brute force method, the time
#the passord takes to crack exponentially increases with each added digit
def md5breaker(hashedWord):
	#creates a list of all possible characters to be recombined
	allPossibleChars = list(ascii_letters + punctuation + digits)
	#records the starts time
	start_time = time.time()
	#our condition for exiting the cracker's loop
	hashFound = False
	while(hashFound == False):
		#an arbitrary range of digits from which to Check
		#our brute forcer will noticeably begin to slow down at 4 digits
        print "/***********************************/"
		for i in range(1, 16):
			#generates a list of all permutations of our allPossibleChars list
			values = ["".join(x) for x in itertools.permutations(allPossibleChars, i)]
			#loops through those values to see if we find a hash match
			for value in values:
				#if the two hashes match we exit
				if(hashedWord == md5.new(value).hexdigest()):
					#prints the time the operation takes
					print ("Time Elapsed: %s seconds" % (time.time() - start_time))
					#prints the password it found
					print("The password is %s" % value)
                    print "/***********************************/"
					return
#used to prompt the user for the password file
def main():
	#grabs teh passowrd file and sends it to our opening module
	fName = raw_input("Please enter your password file: ")
	runthroughPasswordsInFile(str(fName))
#a bit of code to force our main method to run
if __name__ == '__main__':
    main()
