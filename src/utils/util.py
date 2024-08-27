# Python
from datetime import datetime

def generate_current_date_and_time():
    current_datetime = datetime.now().strftime('%d%m%Y%H')
    return current_datetime