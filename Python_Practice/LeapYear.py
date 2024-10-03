def is_leap_year(year):
    # Write your code here.
    if year%4 == 0:
        if year%100 != 0:
            return True
        if year%100 == 0 and year%400==0:
            return True
        else:
            return False
    else:
        return False
Year = int(input("Enter the year"))
print(is_leap_year(Year))