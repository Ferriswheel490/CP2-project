# Fairus time handling

from datetime import datetime

#function to get the timestamp
#shows the current timestamp
def get_current_timestamp():
    current_time = datetime.now()
    return current_time.strftime("%Y-%m-%d %H:%M:%S")