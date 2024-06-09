'''
Seconds in an hour calculator
'''

seconds_per_minute = 60
minutes_per_hour = 60
hours_per_day = 24

seconds_per_hour = seconds_per_minute * minutes_per_hour

seconds_per_day = seconds_per_hour * hours_per_day

'''Hours per day calculation pt 2'''
print(seconds_per_day // seconds_per_hour)