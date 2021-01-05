# 1 hour = 60 minutes
# 1 mile = 1.61 kilometer
"""If you run a 10 kilometer race in 43 minutes 30seconds,
what is your average time per mile ? What is your average speed in miles per hour?"""
# speed = distance/time

#
kilometer_distance = 10

distance_in_mile = kilometer_distance/1.61

time_in_minutes = 43.5 # 60 seconds = 1 minute , so 30 seconds = .5 minnute

time_in_seconds = 43.5 * 60

time_in_hour = time_in_minutes/60

average_time_per_mile_minutes = time_in_minutes/distance_in_mile

average_time_per_mile_seconds = time_in_seconds/distance_in_mile

print(average_time_per_mile_seconds) # in seconds

print(average_time_per_mile_minutes) # in minutes

average_speed = distance_in_mile/time_in_hour

print(average_speed) # in miles per hour

