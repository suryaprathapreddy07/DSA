from dataclasses import dataclass
from datetime import date, datetime
import re
from time import time_ns
logs=[['122.106.125.155__HOME__[21/06/2005:23:48:33]_"GET_/bannerad/ad.html"'],['122.106.125.155__HOME__[21/06/2012:23:48:33]_"GET_/bannerad/ad.html"']]
# timeframe=logs[0].split('__')[-1].split('_')[0]
# print(timeframe)
# dateList = re.findall(r'(\d+/\d+/\d+)',timeframe)[0].split('/')
# print(matches)

def solve(N,logs,startDate,startTime,endDate,endTime):
    count=0
    startDateList=re.findall(r'(\d+/\d+/\d+)',startDate)[0].split('/')
    startTimeList=startTime.split(':')
    endDateList=re.findall(r'(\d+/\d+/\d+)',endDate)[0].split('/')
    endTimeList=endTime.split(':')
    startDate=datetime(int(startDateList[-1]),int(startDateList[1]),int(startDateList[0]),int(startTimeList[0]),int(startTimeList[1]),int(startTimeList[-1]))
    endDate=datetime(int(endDateList[-1]),int(endDateList[1]),int(endDateList[0]),int(endTimeList[0]),int(endTimeList[1]),int(endTimeList[-1]))
    for i in logs:
        timeframe=i[0].split('__')[-1].split('_')[0]
        # print(timeframe)
        dateList = re.findall(r'(\d+/\d+/\d+)',timeframe)[0].split('/')
        logDate=datetime(int(dateList[-1]),int(dateList[1]),int(dateList[0]))
        if(startDate<logDate<endDate):
            count+=1
    return count

print(solve(2,logs,'28/8/2001','04:28:47','09/09/2009','20:29:00'))





