'''Age calculator in Python'''
import datetime
from datetime import date

# Months store total #days of each month.
Months = {
    1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31,
    8: 31, 9: 30, 10: 31, 11: 30, 12: 31
}


# Function that check if a year is leap year or not
def IsLeapYear(year):
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


current_date = datetime.date.today()
# current_date = datetime.datetime.strptime("2022-03-11", "%Y-%m-%d").date()
c_year = current_date.year
c_month = current_date.month
c_day = current_date.day

birth_date = datetime.datetime.strptime("1999-08-06", "%Y-%m-%d").date()
b_year = birth_date.year
b_month = birth_date.month
b_day = birth_date.day

if IsLeapYear(c_year):
    Months[2] = 29


total_age = current_date - birth_date
age_in_seconds = int(total_age.total_seconds())
age_in_minutes = int(age_in_seconds/60)
age_in_hours = int(age_in_minutes/60)
age_in_days = total_age.days
age_in_weeks_and_days = f"{int(age_in_days/7)} weeks {int(age_in_days%7)} days"
print("Seconds:", age_in_seconds)
print("Minutes:", age_in_minutes)
print("Hours:", age_in_hours)
print("Days:", age_in_days)
print("Weeks:", age_in_weeks_and_days)

total_years = c_year - b_year
if c_month > b_month or c_month == b_month:
    total_months = c_month - b_month
else:
    total_months = 12 - (b_month - c_month)
    total_years -= 1

if c_day > b_day or c_day == b_day:
    total_days = c_day - b_day
else:
    total_days = Months[c_month] - (b_day - c_day)
    total_months -= 1

print(f"You are {total_years} years {total_months} months and {total_days} days old")
