import calendar

# Prompt the user for the year and month
year = int(input("Enter year: "))
month = int(input("Enter month: "))

# Generate the calendar for the given year and month
cal = calendar.monthcalendar(year, month)

# Display the calendar
print(calendar.month_name[month], year)
print("Mo Tu We Th Fr Sa Su")
for week in cal:
    week_str = ""
    for day in week:
        if day == 0:
            week_str += "   "
        else:
            week_str += "{:2d} ".format(day)
    print(week_str)
