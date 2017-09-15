from datetime import  datetime
from datetime import timedelta
from datetime import timezone

#主要熟悉python内置的datetime 库
now = datetime.now()
print(now)
print(type(now))

d = datetime(2019, 5, 30, 20, 20, 20) #创建一个datetime的类
print(d)
print(d.timestamp()) #单位是秒不是毫秒

fromtimestamp = datetime.fromtimestamp(d.timestamp()) #通过实践戳来构建一个时间 会自动根据所在的时区构建和本时区相符合的时间
print(fromtimestamp)
print(fromtimestamp.utcfromtimestamp(d.timestamp())) #通过时间戳来构建一个UTC +0:00 时间 即时间统一时间


#str 转化成时间
strptime = datetime.strptime('2010-6-12 12:20:30', '%Y-%m-%d %H:%M:%S')
print(strptime)


#把一个时间转化成为字符串
strftime = now.strftime("%a")
print(strftime)


#对时间的加减操作
datetime_now = datetime.now()
print(datetime_now - timedelta(hours=10)) #利用timedelta类可以很方便的实现对时间的加减操作
print(datetime_now + timedelta(days= 4,hours=1)) #利用timedelta类可以很方便的实现对时间的加减操作



#将本地时间转化为UTC时间

tz_utc_8 = timezone(timedelta(hours=8))

time = datetime(2017,9,8,20,20,20)
time.replace(tzinfo=tz_utc_8)
print(time)


