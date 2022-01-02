leap = """
 ____                    _                               _   _
|  _ \  __ _ _   _ ___  (_)_ __    _ __ ___   ___  _ __ | |_| |__
| | | |/ _` | | | / __| | | '_ \  | '_ ` _ \ / _ \| '_ \| __| '_  |
| |_| | (_| | |_| \__ \ | | | | | | | | | | | (_) | | | | |_| | | |
|____/ \__,_|\__, |___/ |_|_| |_| |_| |_| |_|\___/|_| |_|\__|_| |_|
             |___/
"""

# art created by figlet
print(leap)


def is_leap(year):
    """checks if the year is a leap year it means it has 29 days in febriary"""
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def find_days_in_month(year, month):
    """Finds how many days are in a month base on leap year"""
    if month > 12 or month < 1:
        return "Invalid month"
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    is_leap_year = is_leap(year)
    if is_leap_year and month == 2:
        return 29
    return month_days[month - 1]


print(find_days_in_month(int(input("Enter a year: ")), int(input("Enter a month: "))))
