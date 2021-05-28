import datetime
import pytz

utc_now = pytz.utc.localize(datetime.datetime.utcnow())
my_time = utc_now.astimezone(pytz.timezone('US/Eastern'))
print(my_time)