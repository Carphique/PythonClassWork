from datetime import datetime

def get_current_timestamp():
    return int(
        datetime.timestamp(
            datetime.now()
        )
    )