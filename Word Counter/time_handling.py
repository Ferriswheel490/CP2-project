# Fairus time handling

from datetime import datetime

#to get the current timestamp
def get_current_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
