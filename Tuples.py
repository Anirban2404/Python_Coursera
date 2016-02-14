# 10.2 Write a program to read through the mbox-short.txt and figure out
# the distribution by hour of the day for each of the messages. You can pull the hour out
# from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

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
        # Split the words
        words = line.split()
        # Splitting the string a second time using a colon
        time = words[5].split(':')
        # If hour exists increment the count,
        # else enlist new hour
        counts[time[0]] = counts.get(time[0],0) + 1

# print the counts for each hour, sorted by hour
for hour,occurrence in sorted([(hour,occurrence) for hour,occurrence in counts.items()]):
    print hour,occurrence