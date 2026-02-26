import os
from datetime import datetime

def get_current_time() -> str:
    """
    Returns the current time in HH:MM:SS format.
    """
    return datetime.now().strftime(os.getenv("TIME_FORMAT", "%H:%M:%S"))