# 3.1 Write a program to prompt the user for hours and rate per hour
# using raw_input to compute gross pay. Pay the hourly rate for the
# hours up to 40 and 1.5 times the hourly rate for all hours worked
# above 40 hours. Use 45 hours and a rate of 10.50 per hour to test
# the program (the pay should be 498.75). You should use raw_input
# to read a string and float() to convert the string to a number.
# Do not worry about error checking the user input - assume
# the user types numbers properly.

hrs = raw_input("Enter Hours:")
h = float(hrs)
rates = raw_input("Enter Rates:")
r = float(rates)
if h <= 40: # for normal hours work
    total_pay = h * r;
    print total_pay
else:  # for overtime work
    extra = h - 40
    normal_pay = 40 * r
    extra_pay = extra * r * 1.5
    total_pay = normal_pay + extra_pay
    print total_pay

# 3.3 Write a program to prompt for a score between 0.0 and 1.0.
# If the score is out of range, print an error. If the score is
# between 0.0 and 1.0, print a grade using the following table:
# Score Grade
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F
# If the user enters a value out of range, print a suitable error
# message and exit. For the test, enter a score of 0.85.

i = raw_input('Enter Points:')
# Converting to float
points = float(i)
# Calculating the grades
if points <0.6:
    print 'F'
elif points >= 0.6 and points < 0.7:
    print 'D'
elif points >= 0.7 and points < 0.8:
    print 'C'
elif points >= 0.8 and points < 0.9:
    print 'B'
elif points >=0.9 and points <=1:
    print 'D'
else: #Points OutofRange
    print 'Invalid Points'