actor_name = str(input())
points = float(input())
jury_count = int(input())

for x in range(jury_count):
    jury_name = str(input())
    jury_points = float(input())

    points += (jury_points * len(jury_name)) / 2
    if points >= 1250.5:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {points:.1f}!")
        break

if points < 1250.5:
    print(f"Sorry, {actor_name} you need {(1250.5 - points):.1f} more!")