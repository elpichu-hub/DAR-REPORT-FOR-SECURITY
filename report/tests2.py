import datetime
import pytz

utc_now = pytz.utc.localize(datetime.datetime.utcnow())
my_time = utc_now.astimezone(pytz.timezone('US/Eastern'))
print(my_time)


time = datetime.datetime(2021, 10, 30, 23)
print(time)

def test(*args):
    for arg in args:
        if arg == time:
            print(f'date and time is {time}')
        else:
            print('no')

test(time, utc_now)