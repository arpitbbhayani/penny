from datetime import datetime

def date(d):
    """
    Returns human readable date from datetime.date object
    """
    return d.strftime('%d %B')

def time(t):
    """
    Returns human readable time from datatime.time object
    """
    return t.strftime('%I:%M %p')

def from_ts(timestamp):
    """
    Returns human readable date-time format from timestamp
    """
    d = datetime.fromtimestamp(timestamp)
    return d.strftime('%I:%M:%S %p on %d, %b %Y')

def fromBytes(bytes):
    """
    Returns Human readable size of the file from bytes
    """
    index = 0
    units = ['B', 'KB', 'MB', 'GB']

    while int(bytes/1024.0) > 0:
        bytes /= 1024.0
        index = index + 1

    print type(bytes)
    if type(bytes) == int or (bytes).is_integer():
        return "%d %s" % (bytes, units[index])
    else:
        return "%.2f %s" % (bytes, units[index])
