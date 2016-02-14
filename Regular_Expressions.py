# Finding Numbers in a Haystack
# In this assignment you will read through and parse a file with text and numbers.
# You will extract all the numbers in the file and compute the sum of the numbers.
# Data Files
# We provide two files for this assignment.
# One is a sample file where we give you the sum for your testing and
# the other is the actual data you need to process for the assignment.
# Sample data: http://python-data.dr-chuck.net/regex_sum_42.txt
# (There are 116 values with a sum=597873)
# Actual data: http://python-data.dr-chuck.net/regex_sum_236581.txt
# (There are 86 values and the sum ends with 47)
# These links open in a new window. Make sure to save the file into
# the same folder as you will be writing your Python program.
# Data Format
# The file contains much of the text from the introduction of the textbook
# except that random numbers are inserted throughout the text.
# Here is a sample of the output you might see:
# Why should you learn to write programs? 7746
# 12 1929 8827
# Writing programs (or programming) is a very creative
# 7 and rewarding activity.  You can write programs for
# many reasons, ranging from making your living to solving
# 8837 a difficult data analysis problem to having fun to helping 128
# someone else solve a problem.  This book assumes that
# everyone needs to know how to program ...
# The sum for the sample text above is 27486. The numbers can appear
# anywhere in the line. There can be any number of numbers in each line (including none).
# Handling The Data
# The basic outline of this problem is to read the file, look for integers
# using the re.findall(), looking for a regular expression of '[0-9]+' and
# then converting the extracted strings to integers and summing up the integers.

# Import the Regular Expression library
import re

fname = raw_input("Enter Filename: ")
if len(fname) < 1:
    fname = "regex_sum_42.txt"
# Connecting the file by handler
fh = open(fname)

# Larger Code
''''
count = 0
sum = 0

# Reading the file line by line
for line in fh:
    line = line.strip()
    # Regular Expression to find the digits
    numbers = re.findall('[0-9]+',line)

    if len(numbers)>=0:
        for number in numbers:
            # Calculating the sum
            sum = sum + int(number)
            # Counting the number incrementally
            count = count + 1

print "There are %d values with a sum=%d" % (count, sum)
'''
# Awesome One Liner Code
# There are a number of different ways to approach this problem.
# While we don't recommend trying to write the most compact code possible,
# it can sometimes be a fun exercise. Here is a a redacted version of
# two-line version of this program using list comprehension:

print sum([int(number) for number in re.findall('[0-9]+',fh.read())])