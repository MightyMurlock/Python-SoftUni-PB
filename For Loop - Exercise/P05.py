FACEBOOK_FINE = 150
INSTAGRAM_FINE = 100
REDDIT_FINE = 50

tab_count = int(input())
salary = int(input())

for x in range(tab_count):
    tab_name = str(input())
    match tab_name:
        case "Facebook":
            salary -= FACEBOOK_FINE
        case "Instagram":
            salary -= INSTAGRAM_FINE
        case "Reddit":
            salary -= REDDIT_FINE

    if salary <= 0:
        print("You have lost your salary.")
        break

if salary > 0:
    print(salary)