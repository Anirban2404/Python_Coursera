# 9.4 Write a program to read through the mbox-short.txt and figure out who has
# the sent the greatest number of mail messages. The program looks for 'From ' lines and takes
# the second word of those lines as the person who sent the mail. The program creates a Python
# dictionary that maps the sender's mail address to a count of the number of times they appear
# in the file. After the dictionary is produced, the program reads through the dictionary
# using a maximum loop to find the most prolific committer.

# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
# Set the default file as "mbox-short.txt"
if len(fname) < 1:
    fname = "mbox-short.txt"
# Handler to make connection with the file
fh = open(fname)

# Initiating dictionary
counts = dict()

#Reading file line by line
for line in fh:
    line = line.strip()
    if line.startswith('From '):
        words = line.split()
        # If word exists increment the count,
        # else enlist new word
        counts[words[1]] = counts.get(words[1],0) + 1


most_occurrence = None
most_name = None
for name,occurrence in counts.items():
    # Finding most prolific committer
    if most_occurrence is None or most_occurrence < occurrence:
        most_occurrence = occurrence
        most_name = name

print most_name,most_occurrence
