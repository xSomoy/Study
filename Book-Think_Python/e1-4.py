total_time = (43*60) + 30 # in seconds
total_mile = 10/1.61

avg_time_per_mile = total_time / total_mile 
avg_speed_in_miles_hour = total_mile / (total_time / (60*60))

print('Average Time Per Mile (In Seconds): ' + "{:.2f}".format(avg_time_per_mile)) # in seconds
print('Average Miles Per Hour : ' + '{:.2f}'.format(avg_speed_in_miles_hour))




