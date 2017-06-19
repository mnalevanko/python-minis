from datetime import datetime
dt = datetime(2016, 1, 5, 13, 30)

def appendix_to_day(datet):
    if str(datet.day)[-1] == '1':
        return 'st'
    elif str(datet.day)[-1] == '2':
        return 'nd'
    else:
        return 'th'


def format_datetime(dt):
    return datetime.strftime(dt, '%A, %B %d{}, %Y at %H:%M hs'.format(appendix_to_day(dt)))

print(format_datetime(dt))
