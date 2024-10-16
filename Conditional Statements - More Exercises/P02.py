#play norm annualy = 30 000 minutes

#workday = 63 minutes/day
#day_off = 127 minutes/day

#year = 365 days

DAYS_YEAR = 365
PLAYTIME_NORM = 30000
WORKDAY_PLAYTIME = 63
DAY_OFF_PLAYTIME = 127

days_off = int(input())

workdays = DAYS_YEAR - days_off
workdays_playtime = workdays * WORKDAY_PLAYTIME
days_off_playtime = days_off * DAY_OFF_PLAYTIME

playtime_annualy = workdays_playtime + days_off_playtime

if playtime_annualy > PLAYTIME_NORM:
    time_difference = playtime_annualy - PLAYTIME_NORM
    print("Tom will run away")
    print(f"{time_difference // 60} hours and {time_difference % 60} minutes more for play")
else:
    time_difference = PLAYTIME_NORM - playtime_annualy
    print("Tom sleeps well")
    print(f"{time_difference // 60} hours and {time_difference % 60} minutes less for play")