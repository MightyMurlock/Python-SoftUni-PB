from math import floor

POINTS_W = 2000
POINTS_F = 1200
POINTS_SF = 720

average_points = 0
win_count = 0

tournament_count = int(input())
points = int(input())

for x in range(tournament_count):
    rank = str(input())

    match rank:
        case "W":
            points += POINTS_W
            average_points += POINTS_W
            win_count += 1
        case "F":
            points += POINTS_F
            average_points += POINTS_F
        case "SF":
            points += POINTS_SF
            average_points += POINTS_SF

average_points /= tournament_count
win_rate = (win_count / tournament_count) * 100

print(f"Final points: {points}")
print(f"Average points: {floor(average_points)}")
print(f"{win_rate:.2f}%")
