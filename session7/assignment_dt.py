from datetime import datetime
from datetime import date

# datetime to string
def datetime_to_str_1(dt):
    # Convert to format "2023-07-19"
    dates = dt.strftime("%Y-%m-%d")
    return dates


def datetime_to_str_2(dt):
    # Convert to format "23-07-19"
    dates = dt.strftime("%y-%m-%d")
    return dates


def datetime_to_str_3(dt):
    # Convert to format "July 19, 2023"
    dates = dt.strftime("%B %d, %Y")
    return dates


def datetime_to_str_4(dt):
    # Convert to format "Jul 19, 2023"
    dates = dt.strftime("%b %d, %Y")
    return dates

def datetime_to_str_5(dt):
    # Convert to format "19 July 2023"
    dates = dt.strftime("%d %B %Y")
    return dates

def datetime_to_str_6(dt):
    # Convert to format "Wednesday July 19, 2023"
    dates = dt.strftime("%A %B %d, %Y")
    return dates

def datetime_to_str_7(dt):
    # Convert to format "Wed July 19, 2023"
    dates = dt.strftime("%a %B %d, %Y")
    return dates

def datetime_to_str_8(dt):
    # Convert to format "2023-07-19 10:30:45"
    dates = dt.strftime("%Y-%m-%d %H:%M:%S")
    return dates

def datetime_to_str_9(dt):
    # Convert to format "10:30:45"
    dates = dt.strftime("%H:%M:%S")
    return dates

def datetime_to_str_10(dt):
    # Convert to format "10:30 AM"
    dates = dt.strftime("%H:%M %p")
    return dates

# string to datetime
def str_to_datetime_1(s):
    # Convert from format "2023-07-19"
    dates = datetime.strptime(s,"%Y-%m-%d")
    return dates

def str_to_datetime_2(s):
    # Convert from format "23-07-19"
    dates = datetime.strptime(s,"%y-%m-%d")
    return dates

def str_to_datetime_3(s):
    # Convert from format "July 19, 2023"
    dates = datetime.strptime(s,"%B %d, %Y")
    return dates

def str_to_datetime_4(s):
    # Convert from format "Jul 19, 2023"
    dates = datetime.strptime(s,"%b %d, %Y")
    return dates

def str_to_datetime_5(s):
    # Convert from format "19 July 2023"
    dates = datetime.strptime(s,"%d %B %Y")
    return dates

def str_to_datetime_6(s):
    # Convert from format "Wednesday July 19, 2023"
    dates = datetime.strptime(s,"%A %B %d, %Y")
    return dates

def str_to_datetime_7(s):
    # Convert from format "Wed July 19, 2023"
    dates = datetime.strptime(s,"%a %B %d, %Y")
    return dates

def str_to_datetime_8(s):
    # Convert from format "2023-07-19 10:30:45"
    dates = datetime.strptime(s,"%Y-%m-%d %H:%M:%S")
    return dates

def str_to_datetime_9(s):
    # Convert from format "10:30:45"
    dates = datetime.strptime(s,"%H:%M:%S")
    return dates
def str_to_datetime_10(s):
    # Convert from format "10:30 AM"
    dates=datetime.strptime(s,"%H:%M %p")
    return dates
