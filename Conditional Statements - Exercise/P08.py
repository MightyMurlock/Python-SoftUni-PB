from math import ceil

LUNCH_TIME_PERCENTAGE = 12.5 / 100
REST_TIME_PERCENTAGE = 25 / 100

series_name = str(input())
episode_duration = int(input())
break_duration = int(input())

lunch_time = break_duration * LUNCH_TIME_PERCENTAGE
rest_time = break_duration * REST_TIME_PERCENTAGE

break_time_left = break_duration - lunch_time - rest_time

if break_time_left >= episode_duration:
    print(f"You have enough time to watch {series_name} and left with {ceil(break_time_left - episode_duration)} minutes free time.")
else:
    print(f"You don't have enough time to watch {series_name}, you need {ceil(episode_duration - break_time_left)} more minutes.")