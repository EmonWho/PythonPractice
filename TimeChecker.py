#This is a way to find the current time
import datetime
now = datetime.datetime.now()
print ("Current date and time : ",end="")
print (now.strftime("%Y-%m-%d %H:%M:%S"))


#And this is another way to find
import datetime

current_time = datetime.datetime.now()

print("Time now at greenwich meridian is : " , end="")
print(current_time)