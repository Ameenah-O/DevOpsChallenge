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

# Function to rename multiple files
def capitalize_filenames(directory):
    for filename in os.listdir(directory):
        dst =filename.upper()
        src =directory+ filename
        dst =directory+ dst

        # rename() function will
        # rename all the files
        os.rename(src, dst)

# Function to rename multiple files
def uncapitalize_filenames(directory):
    for filename in os.listdir(directory):
        dst =filename.lower()
        src =directory+ filename
        dst =directory+ dst

        # rename() function will
        # rename all the files
        os.rename(src, dst)

if args.s !="None":
    uncapitalize_filenames(args.s)
elif args.S !="None":
    capitalize_filenames(args.S)
else:
    print("Please enter a valid argument")


# Driver Code
#if __name__ == '__main__':

    # Calling main() function
#    capitalize_filenames()
