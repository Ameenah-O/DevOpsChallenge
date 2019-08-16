# Python3 code to that accepts an argument
# -S to captalize file names in a directory
# or -s to change the file names to lowercase

# importing os module
import os
import argparse

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("-s", help="change all the filename of the files in a directory to "
                               "small letter")
group.add_argument("-S", help="change all the filename of the files in a directory to "
                               "capital letter")
args = parser.parse_args()
if args.s !="None":
    print("")
elif args.S !="None":
    print("")
else:
    print("Please enter a valid argument")

# Function to rename multiple files
def capitalize():

	for filename in os.listdir("xyz"):
		dst =filename.upper()
		src ='xyz'+ filename
		dst ='xyz'+ dst

		# rename() function will
		# rename all the files
		os.rename(src, dst)

# Function to rename multiple files
def lowercase():

	for filename in os.listdir("xyz"):
		dst =filename.lower()
		src ='xyz'+ filename
		dst ='xyz'+ dst

		# rename() function will
		# rename all the files
		os.rename(src, dst)

# Driver Code
if __name__ == '__main__':

	# Calling main() function
	capitalize()
