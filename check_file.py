# Python3 code to that accepts an argument
# -S to captalize file names in a directory
# or -s to change the file names to lowercase

# imports
import os
import argparse

#Parser to fetch command line arguements
parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("-s", help="change all the filename of the files in a directory to "
                              "small letter")
group.add_argument("-S", help="change all the filename of the files in a directory to "
                              "capital letter")
args = parser.parse_args()

# Function to change all the filename of the files in a directory to
# capital letter
def capitalize_filenames(directory):
    for filename in os.listdir(directory):
        dst =filename.upper()
        src =directory+ filename
        dst =directory+ dst

        # rename the file
        os.rename(src, dst)

# Function to change all the filename of the files in a directory to
# small letter
def uncapitalize_filenames(directory):
    for filename in os.listdir(directory):
        dst =filename.lower()
        src =directory+ filename
        dst =directory+ dst

        # rename the file
        os.rename(src, dst)

#checks command line argument to capitalize or uncapitalize file  vnames
if args.s !=None:
    uncapitalize_filenames(args.s)
    print("Successful")
elif args.S !=None:
    capitalize_filenames(args.S)
    print("Successful")
else:
    print("Please enter a valid argument")

