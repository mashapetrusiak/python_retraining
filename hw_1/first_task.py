# Write a to_minutes function that returns the number of minutes for a given number of hours.
def to_minutes(hours):
    return hours * 60


# Write the to_hours function, which for a given number of minutes returns the number of hours in the form of a
# decimal fraction. In the case of an infinite fraction, round up to 4 decimal places.
def to_hours(minutes):
    return round(minutes / 60, 4)


# Write a function is_whole_div that checks whether a number is divisible by another number without a remainder.
def is_whole_div(divided, divisor):
    if divided % divisor == 0:
        return True
    else:
        return False
