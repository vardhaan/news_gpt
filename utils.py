from datetime import datetime

# function that converts UTC string into datetime object
def convert_utc_string_to_datetime(utc_string):
    return datetime.strptime(utc_string, '%Y-%m-%dT%H:%M:%SZ')


# function that converts datetime object into UTC string
def convert_datetime_to_utc_string(datetime_obj):
    return datetime_obj.strftime('%Y-%m-%dT%H:%M:%SZ')


