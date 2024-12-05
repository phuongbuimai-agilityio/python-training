# The time module provides a function, also called time,
# that returns returns the number of seconds since the "Unix epoch",
# which is January 1, 1970, 00:00:00 UTC (Coordinated Universal Time).
#
# Use integer division and the modulus operator to compute the number of days since January 1, 1970 
# and the current time of day in hours, minutes, and seconds.

import time

# Get the current time in seconds
current_time = int(time.time())

# Compute the number of days since January 1, 1970
days_since_epoch = current_time // 86400

# Compute the current time of day in seconds
seconds_today = current_time % 86400

# Convert seconds to hours, minutes, and seconds
hours = seconds_today // 3600
minutes = (seconds_today % 3600) // 60
seconds = seconds_today % 60

# Results
print("Days since January 1, 1970: ", days_since_epoch)

# I met an error when use this syntax: print("Current time: {hours}:{minutes}:{seconds}").
# Because this is a string literal with placeholders in curly braces {}, it doesn't automatically 
# substitute the values of variables. 
# So I should format strings in Python like below by the way use f-strings
# - f": tells Python to interpret variables inside {}
# - :02 formats the values to always show two digits (e.g., 05 instead of 5)
# Beside that, we have other ways to fix the issue:
# - Using the .format() method
# - Using the % operator
print(f"Current time: {hours:02}:{minutes:02}:{seconds:02}")
