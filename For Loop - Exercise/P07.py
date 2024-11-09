mussala_count = 0
monblan_count = 0
kilimanjaro_count = 0
k2_count = 0
everest_count = 0
people_count = 0
groups_count = int(input())

for x in range(groups_count):
    people_in_group = int(input())
    people_count += people_in_group

    if people_in_group <= 5:
        mussala_count += people_in_group

    elif 6 <= people_in_group <= 12:
        monblan_count += people_in_group

    elif 13 <= people_in_group <= 25:
        kilimanjaro_count += people_in_group

    elif 26 <= people_in_group <= 40:
        k2_count += people_in_group

    elif people_in_group >= 41:
        everest_count += people_in_group

mussala_percentage = f"{((mussala_count / people_count) * 100):.2f}%"
monblan_percentage = f"{((monblan_count / people_count) * 100):.2f}%"
kilimanjaro_percentage = f"{((kilimanjaro_count / people_count) * 100):.2f}%"
k2_percentage = f"{((k2_count / people_count) * 100):.2f}%"
everest_percentage = f"{((everest_count / people_count) * 100):.2f}%"

print(mussala_percentage)
print(monblan_percentage)
print(kilimanjaro_percentage)
print(k2_percentage)
print(everest_percentage)