DISCOUNT1 = 50 / 100
DISCOUNT2 = 15 / 100
DISCOUNT3 = 5 / 100

season = str(input()) #Winter, Spring, Summer
group_type = str(input()) #boys, girls, mixed
student_count = int(input())
nights_count = int(input())

#price per night
match season:
    case "Winter":
        match group_type:
            case "boys" | "girls":
                price_per_night = 9.60

                if group_type == "boys":
                    sport = "Judo"
                elif group_type == "girls":
                    sport = "Gymnastics"

            case "mixed":
                price_per_night = 10

                sport = "Ski"

    case "Spring":
        match group_type:
            case "boys" | "girls":
                price_per_night = 7.20

                if group_type == "boys":
                    sport = "Tennis"
                elif group_type == "girls":
                    sport = "Athletics"

            case "mixed":
                price_per_night = 9.50

                sport = "Cycling"

    case "Summer":
        match group_type:
            case "boys" | "girls":
                price_per_night = 15

                if group_type == "boys":
                    sport = "Football"
                elif group_type == "girls":
                    sport = "Volleyball"

            case "mixed":
                price_per_night = 20

                sport = "Swimming"

total = (nights_count * price_per_night) * student_count
if student_count >= 50:
    total -= total * DISCOUNT1
elif student_count >= 20 and student_count < 50:
    total -= total * DISCOUNT2
elif student_count >= 10 and student_count < 20:
    total -= total * DISCOUNT3

print(f"{sport} {total:.2f} lv.")