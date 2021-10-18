"""
This code creates a datetime.time object from a string.

- Is it easy to verify that it works correctly?
- Do you see any obvious errors?
- How would you modify it to be easier to read?
"""

import datetime

def create_time_from_timestamp(timestamp: str) -> datetime.time:
    """Create a datetime.time object from a string in the form 'hh:mm:ss'.

    Args:
    timestamp - string containing a timestamp in the format 'hh:mm:ss'

    Returns:
    a datetime.time object with value equal to the timestamp

    Raises:
    ValueError if timestamp is not a string in form "hh:mm:ss"

    Example:
    >>> t = createTimeFromTimestamp("9:23:15")
    >>> type(t)
    <class 'datetime.time'>
    >>> print(t)
    09:23:15
    """
    timestamps = timestamp.split(":")
    if len(timestamps) != 3:
        raise ValueError('Timestamp must be "hh:mm:ss"')
    # if the timestamp is not valid, this may raise TypeError or ValueError
    if (is_valid_time(timestamps)):
        return datetime.time(int(timestamps[0]), int(timestamps[1]), int(timestamps[2]))

def is_valid_time(timestamps):
    """Verify the timestamp component are valid time"""
    return 0 <= int(timestamps[0]) <= 23 and 0 <= int(timestamps[1]) < 60 and 0 <= int(timestamps[2]) < 60
