from datetime import datetime
import iso8601
datetime.strptime('24/Aug/2014:17:57:26 +0200', '%d/%b/%Y:%H:%M:%S %z')

dateStart = "2021-12-09T04:51:58+01:00"
# dateStart = dateStart.replace(':', '')
# dateStart = dateStart.replace('T', '')

print("--------------------------")
theRealDate = iso8601.parse_date(dateStart)
print(theRealDate)
print(type(theRealDate))
print(theRealDate.date())
print(theRealDate.time())
print(theRealDate.hour)
print(theRealDate.timetz())
print(theRealDate.tzinfo)
# print(datetime.strftime(dateStart, '%Y-%m-%d %H:%M:%S'))
# # # print(datetime.strptime(dateStart, '%d/%b/%Y:%H:%M:%S %z'))
# print(datetime.strptime(dateStart, '%Y-%m-%dT%H:%M:%S'))

