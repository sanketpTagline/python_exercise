from datetime import datetime as dt 
import portion as p 

starting_time_string = input("Enter Start Date (YYYY-MM-DD HH:MM AM/PM) : ")
ending_time_string = input("Enter Ending Date (YYYY-MM-DD HH:MM AM/PM) : ")
 
start_time = dt.strptime(starting_time_string, '%Y-%m-%d %I:%M %p')
ending_time = dt.strptime(ending_time_string, '%Y-%m-%d %I:%M %p')

print("starting timr ",start_time)
print("Ending time ",ending_time)

def calculateDiff(startDate, endDate):
    night_time  = p.closed(0,6)
    
    day_time = p.closed(startDate.replace(hour = night_time.upper,minute = 0),endDate.replace(hour = night_time.lower,minute = 0)) 
    print("day interval",day_time)
    night_time = p.closed(startDate.replace(hour = night_time.lower,minute = 0),endDate.replace(hour = night_time.upper,minute = 0))
    print("night interval",night_time)
        
    time_differnce = (ending_time -start_time).total_seconds()/3600
    
    if (startDate.hour >= 0 and startDate.hour <= 6):
        time_differnce += (6 - startDate.hour)
         
    if (endDate.hour >= 0 and endDate.hour <= 6):
        time_differnce += (endDate.hour)
      
    if day_time.overlaps(night_time):
        intersection_time = day_time & night_time
        overlaphour = (intersection_time.upper - intersection_time.lower).total_seconds()/3600
        time_differnce -= overlaphour 
    return time_differnce 
  
result= calculateDiff(start_time,ending_time)
print(result) 