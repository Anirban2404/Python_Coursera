# 8.4 Open the file romeo.txt and read it line by line. For each line,
# split the line into a list of words using the split() function.
# The program should build a list of words. For each word on each line
# check to see if the word is already in the list and if not append it
# to the list. When the program completes, sort and print the resulting
# words in alphabetical order.
# You can download the sample data at http://www.pythonlearn.com/code/romeo.txt

# Use "romeo.txt" as the file name
fname = raw_input("Enter file name: ")
# Set the default file as "romeo.txt"
if len(fname) < 1:
    fname = "romeo.txt"
# Handler to make connection with the file
fh = open(fname)
# Initiating list to store the splitted words
lst = list()

for line in fh:
    # Strip the white spaces
    line = line.rstrip()
    # Split words by spaces
    words = line.split()
    for word in words:
        # if new word comes append it to list
        if word not in lst:
            lst.append(word)
# Print sorted list
print sorted(lst)

# 8.5 Open the file mbox-short.txt and read it line by line. When you find a line that starts
# with 'From ' like the following line:
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# You will parse the From line using split() and print out the second word in the line
# (i.e. the entire address of the person who sent the message). Then print out a count at the end.
# Hint: make sure not to include the lines that start with 'From:'.
# You can download the sample data at http://www.pythonlearn.com/code/mbox-short.txt

# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
# Set the default file as "mbox-short.txt"
if len(fname) < 1:
    fname = "mbox-short.txt"
# Handler to make connection with the file
fh = open(fname)
count = 0
# Reading the file line by line
for line in fh:
    # Strip the white spaces
    line = line.strip()
    # Selecting the lines start with From
    if line.startswith('From '):
        # Increment the count
        count = count + 1
        # Split words by spaces
        words = line.split()
        # print email_id
        print words[1]
        
print "There were", count, "lines in the file with From as the first word"
