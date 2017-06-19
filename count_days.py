from datetime import *

def count_days(date1, date2):
    if date1 > date2:
        raise ValueError('Second date must be greater than first one.')
    delta = date2 - date1
    return delta.days
