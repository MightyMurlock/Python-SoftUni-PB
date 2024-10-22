exam_hour = int(input())
exam_minute = int(input())
arrive_hour = int(input())
arrive_minute = int(input())

total_exam_minutes = (exam_hour * 60) + exam_minute
total_arrive_minutes = (arrive_hour * 60) + arrive_minute

if total_arrive_minutes > total_exam_minutes:
    print("Late")
    time = "late"
    final_time = total_arrive_minutes - total_exam_minutes
elif total_arrive_minutes == total_exam_minutes or (total_arrive_minutes >= (total_exam_minutes - 30) and total_arrive_minutes <= (total_exam_minutes - 30)):
    print("On time")
    time = "early"
    final_time = total_exam_minutes - total_arrive_minutes
elif total_arrive_minutes < (total_exam_minutes - 30):
    print("Early")
    time = "early"
    final_time = total_exam_minutes - total_arrive_minutes

if total_arrive_minutes != total_exam_minutes:
    final_hour = final_time // 60
    final_minute = final_time % 60
    match time:
        case "late":
            if arrive_hour == exam_hour:
                print(f"{final_minute:02d} minutes after the start")
            else:
                print(f"{final_hour}:{final_minute:02d} hours after the start")
        case "early":
            if arrive_hour == exam_hour or :
                print(f"{final_minute:02d} minutes before the start")
            else:
                print(f"{final_hour}:{final_minute:02d} hours before the start")




