# 7.1 Write a program that prompts for a file name, then opens that file
# and reads through the file, and print the contents of the file in upper
# case. Use the file words.txt to produce the output below. You can download
# the sample data at http://www.pythonlearn.com/code/words.txt

# Use words.txt as the file name
fname = raw_input("Enter file name: ")
# Set the default file as "words.txt"
if len(fname) < 1:
    fname = "words.txt"
# Handler to make connection with the file
fh = open(fname, 'r')
# read the file and strip the white spaces
read = fh.read().strip()
print read.upper()


# 7.2 Write a program that prompts for a file name, then opens that file
# and reads through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines
# and compute the average of those values and produce an output as shown below.
# You can download the sample data at http://www.pythonlearn.com/code/mbox-short.txt
# when you are testing below enter mbox-short.txt as the file name.

# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
# Set the default file as "mbox-short.txt"
if len(fname) < 1:
    fname = "mbox-short.txt"
count =0
sum = 0
# Handler to make connection with the file
fh = open(fname)
# Reading the file line by line
for line in fh:
    # If line doesn't start with "X-DSPAM-Confidence:"
    # start over the loop
    if not line.startswith("X-DSPAM-Confidence:") : continue
    # Find the position
    pos = line.find(":")
    # Strip the number as string
    number = line[ pos + 1:].strip()
    # Convert number as float Calculate the sum
    sum = sum + float(number)
    # Calculate count incrementally
    count = count + 1

print "Average spam confidence:", sum / count