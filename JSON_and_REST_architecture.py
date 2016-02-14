# Extracting Data from JSON

# In this assignment you will write a Python program somewhat similar
# to http://www.pythonlearn.com/code/json2.py. The program will prompt
# for a URL, read the JSON data from that URL using urllib and then
# parse and extract the comment counts from the JSON data, compute
# the sum of the numbers in the file and enter the sum below:
# We provide two files for this assignment. One is a sample file where
# we give you the sum for your testing and the other is the actual data
# you need to process for the assignment.

# Sample data: http://python-data.dr-chuck.net/comments_42.json (Sum=2482)
# Actual data: http://python-data.dr-chuck.net/comments_236587.json (Sum ends with 24)
# You do not need to save these files to your folder since your program will
# read the data directly from the URL. Note: Each student will have a distinct
# data url for the assignment - so only use your own data url for analysis.
# Data Format
# The data consists of a number of names and comment counts in JSON as follows:
'''
{
  comments: [
    {
      name: "Matthias"
      count: 97
    },
    {
      name: "Geomer"
      count: 97
    }
    ...
  ]
}
'''
# The closest sample code that shows how to parse JSON and extract a list
# is json2.py. You might also want to look at geoxml.py to see how to prompt
# for a URL and retrieve data from a URL.

# Sample Execution

# $ python solution.py
# Enter location: http://python-data.dr-chuck.net/comments_42.json
# Retrieving http://python-data.dr-chuck.net/comments_42.json
# Retrieved 2733 characters
# Count: 50
# Sum: 2482

# Importing urllib
import urllib
# Importing the JSON parser
import json

# Enter the URL
url = raw_input("Enter URL: ")
# if URL is blank, take http://python-data.dr-chuck.net/comments_42.json
# as default URL
if len(url) < 1:
    url = 'http://python-data.dr-chuck.net/comments_42.json'
print 'Retrieving', url

# Reading the JSON file
_json = urllib.urlopen(url).read()
# Print the length of JSON file
print 'Retrieved',len(_json),'characters'

# Parsing JSON
load_json = json.loads(str(_json))

sum = 0
count=0

# Extracting data from JSON
for value in load_json['comments']:
    # Find the value related to 'count'
    number = (int)(value['count'])
    # Calculating the sum
    sum = sum + number
    count +=1

print 'Count: ', count
print 'Sum: ', sum

