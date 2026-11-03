import datetime
import pytz

# d = datetime.date(2016, 7, 24)

# tday = datetime.date.today()

# # print(d)
# # print(tday.day)
# # print(tday.weekday())       # Monday 0 Sunday 6
# # print(tday.isoweekday())    # Monday 1 Sunday 7


# tdelta = datetime.timedelta(days=7)
# # print(tday - tdelta)

# # date2 = date1 + timedelta
# # timedelta = date1 + date2

# bday = datetime.date(2016, 9, 24)

# till_bday = bday - tday
# print(till_bday.days)
# print(till_bday.total_seconds())


# t = datetime.time(9, 30, 45, 100000)
# print(t)
# print(t.hour)


# dt = datetime.datetime(2016, 7, 24, 12, 30, 45, 100000)
# # print(dt)
# # print(dt.date())
# # print(dt.time())

# tdelta = datetime.timedelta(days=7, hours=10)

# print(dt+tdelta)


# dt_today = datetime.datetime.today()
# dt_now = datetime.datetime.now()
# dt_utcnow = datetime.datetime.utcnow()

# print(dt_today)
# print(dt_now)
# print(dt_utcnow)


# dt = datetime.datetime(2016, 7, 27, 12, 30, 45, tzinfo=pytz.UTC)

# print(dt)

# dt_now = datetime.datetime.now(tz=pytz.UTC)
# print(dt_now)

# dt_utcnow = datetime.datetime.now(datetime.timezone.utc)
# print(dt_utcnow)

# dt_vn = dt_utcnow.astimezone(pytz.timezone("Asia/Ho_Chi_Minh"))
# print(dt_vn)

# for tz in pytz.all_timezones:
#     print(tz)


# dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
# print(dt_utcnow)

# # dt_mtn = dt_utcnow.astimezone(pytz.timezone("US/Mountain"))
# # print(dt_mtn)

# dt_mtn = datetime.datetime.now()

# mtn_tz = pytz.timezone("US/Mountain")

# dt_mtn = mtn_tz.localize(dt_mtn)

# dt_east = dt_mtn.astimezone(pytz.timezone("US/Eastern"))

# print(dt_mtn)


dt_mtn = datetime.datetime.now(tz=pytz.timezone("US/Mountain"))
# print(dt_mtn.isoformat())
print(dt_mtn.strftime("%B %d, %Y"))  # July 27, 2016


dt_str = 'July 27, 2016'

dt = datetime.datetime.strptime(dt_str, "%B %d, %Y")
print(dt)

# strftime - Datetime to String
# strptime - String to Datetime
