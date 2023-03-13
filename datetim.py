import datetime

# Converting epoch time into DateTime using Python
epoch_time = 4587963258
date_time = datetime.datetime.fromtimestamp(epoch_time)
print(date_time)

# Converting DateTime into epoch time using Python
epoch_time = datetime.datetime(2023,8,9).timestamp()

# using datetime.fromtimestamp() function to convert epoch time into datetime object  
mytimestamp = datetime.datetime.fromtimestamp( epoch_time )  
  
# using strftime() function to convert  
datetime_str = mytimestamp.strftime( "%Y - %m - %d  %H : %M : %S")  

print(datetime_str)