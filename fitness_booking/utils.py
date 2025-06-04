from datetime import datetime
import pytz

def convert_to_timezone(dt_str, target_tz):
    ist = pytz.timezone('Asia/Kolkata')
    target = pytz.timezone(target_tz)

    dt = ist.localize(datetime.fromisoformat(dt_str))
    return dt.astimezone(target).isoformat()
