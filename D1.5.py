#wap to check whether a given year is a leap year or not....
year = int(input("Enter the year:"))

if (year % 4 ==0 and year % 100 != 0):
    print("%d is a leap year" %year)
else:
    print("%d is not a leap year" %year)
