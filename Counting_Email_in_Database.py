# Counting Organizations
# This application will read the mailbox data (mbox.txt) count up the number email messages per organization
# (i.e. domain name of the email address) using a database with the following schema to maintain the counts.

# CREATE TABLE Counts (org TEXT, count INTEGER)
# When you have run the program on mbox.txt upload the resulting database file above for grading.
# If you run the program multiple times in testing or with dfferent files, make sure to empty out the data before each run.

# You can use this code as a starting point for your application: http://www.pythonlearn.com/code/emaildb.py.

# The data file for this application is the same as in previous assignments: http://www.pythonlearn.com/code/mbox.txt.

# Because the sample code is using an UPDATE statement and committing the results to the database as each record
# is read in the loop, it might take as long as a few minutes to process all the data. The commit insists on completely
# writing all the data to disk every time it is called.

# The program can be speeded up greatly by moving the commit operation outside of the loop. In any database program,
# there is a balance between the number of operations you execute between commits and the importance of not losing
# the results of operations that have not yet been committed.

# import the sqlite3 database functionalities
import sqlite3
# Import Regular Expression
import re

# Making connection to database
conn = sqlite3.connect('anirban.sqlite')
# Creating the cursor
cur = conn.cursor()

# Cursor to access database
cur.execute('''
DROP TABLE IF EXISTS Counts''')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

# Enter the filename
fname = raw_input('Enter file name: ')
# if file name is blank, take mbox-short.txt as default file
if ( len(fname) < 1 ) : fname = 'mbox-short.txt'
# Creating the file connection
fh = open(fname)
# Read line by line from file
for line in fh:
    # Ignore the lines do not start with 'From'
    if not line.startswith('From: ') : continue
    # Find the email domain
    email_domain = re.findall('@([a-zA-Z.]+)',line.strip())
    # print email_domain[0]
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (email_domain[0],))
    row = cur.fetchone()
    if row is None:
        # Insert into Count table
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES ( ?, 1 )''', ( email_domain[0], ) )
    else :
        # Update the count column
        cur.execute('UPDATE Counts SET count=count+1 WHERE org = ?',
            (email_domain[0], ))
    # This statement commits outstanding changes to disk each
    # time through the loop - the program can be made faster
    # by moving the commit so it runs only after the loop completes
    conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

print
print "Counts:"
for row in cur.execute(sqlstr) :
    print str(row[0]), row[1]

cur.close()

