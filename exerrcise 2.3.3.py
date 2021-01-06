"""If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile),
then 3 miles at tempo (7:12 per mile) and 1 mile at easy pace again,
what time do I get home for breakfast?"""

starting_time ="6.52am"

starting_time_seconds = (6*60 + 52)* 60 # convert starting time to seconds

easy_pace = 8*60 + 15 # in seconds
tempo_pace =  7*60 + 12 # in seconds
total_time = 2* easy_pace + 3* tempo_pace
time_for_breakfast = (starting_time_seconds + total_time) / (60*60)
print(time_for_breakfast)
