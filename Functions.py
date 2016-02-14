# 4.6 Write a program to prompt the user for hours and rate per hour
# using raw_input to compute gross pay. Award time-and-a-half for the
# hourly rate for all hours worked above 40 hours. Put the logic to do
# the computation of time-and-a-half in a function called computepay()
# and use the function to do the computation. The function should
# return a value. Use 45 hours and a rate of 10.50 per hour to test
# the program (the pay should be 498.75). You should use raw_input
# to read a string and float() to convert the string to a number.
# Do not worry about error checking the user input unless you want
# to - you can assume the user types numbers properly.


# Defining Function to calculate pay
def computepay(h,r):
    if h <= 40:
        pay = h * r
        # print pay
    else:
        extra = h - 40
        normal_pay = 40 * r
        extra_pay = extra * r * 1.5
        pay = normal_pay + extra_pay
        # print pay
    return pay

hrs = raw_input("Enter Hours:")
h = float(hrs)
rates = raw_input("Enter Rates:")
r = float(rates)
# Calling the function
pay = computepay(h,r)
print pay