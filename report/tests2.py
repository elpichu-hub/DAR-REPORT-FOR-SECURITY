import datetime
import pytz

utc_now = pytz.utc.localize(datetime.datetime.utcnow())
date = utc_now.astimezone(pytz.timezone('US/Eastern'))
print(date)