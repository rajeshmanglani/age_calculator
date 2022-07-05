from flask import Flask, request, redirect, render_template, send_file, jsonify
import glob, os

app = Flask(__name__)

import datetime


class AgeCalculator:
    def __init__(self):
        # Months store total #days of each month.
        self.Months = {
            1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31,
            8: 31, 9: 30, 10: 31, 11: 30, 12: 31
        }

    # Function that check if a year is leap year or not
    def IsLeapYear(self, year):
        try:
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
        except Exception as e:
            return e

    def check_age(self, birth_date):
        try:
            current_date = datetime.date.today()
            c_year = current_date.year
            c_month = current_date.month
            c_day = current_date.day

            birth_date = datetime.datetime.strptime(birth_date, "%Y-%m-%d").date()
            b_year = birth_date.year
            b_month = birth_date.month
            b_day = birth_date.day

            if self.IsLeapYear(c_year):
                self.Months[2] = 29

            total_age = current_date - birth_date
            age_in_seconds = int(total_age.total_seconds())
            age_in_minutes = int(age_in_seconds/60)
            age_in_hours = int(age_in_minutes/60)
            age_in_days = total_age.days
            age_in_weeks_and_days = f"{int(age_in_days/7)} weeks {int(age_in_days%7)} days"

            total_years = c_year - b_year
            if c_month > b_month or c_month == b_month:
                total_months = c_month - b_month
            else:
                total_months = 12 - (b_month - c_month)
                total_years -= 1

            if c_day > b_day or c_day == b_day:
                total_days = c_day - b_day
            else:
                total_days = self.Months[c_month] - (b_day - c_day)
                total_months -= 1

            return f"You are {total_years} years {total_months} months and {total_days} days old"
        except Exception as e:
            return "Something went wrong"


@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == "POST":
        birth_date = request.form['birth_date']
        age_calculator_obj = AgeCalculator()
        age = age_calculator_obj.check_age(birth_date)
        return render_template('index.html', data=age)
    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
