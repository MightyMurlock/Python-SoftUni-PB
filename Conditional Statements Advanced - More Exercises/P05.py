#season = Summer, Winter
#location = Alaska, Morocco
#accomodation = Hotel, Hut, Camp

budget = float(input())
season = str(input())

if budget <= 1000:
     accomodation = "Camp"

     match season:
         case "Summer":
             location = "Alaska"
             price = (65 / 100) * budget
         case "Winter":
             location = "Morocco"
             price = (45 / 100) * budget

elif budget > 1000 and budget <= 3000:
    accomodation = "Hut"

    match season:
        case "Summer":
            location = "Alaska"
            price = (80 / 100) * budget
        case "Winter":
            location = "Morocco"
            price = (60 / 100) * budget

else:
    accomodation = "Hotel"

    match season:
        case "Summer":
            location = "Alaska"
        case "Winter":
            location = "Morocco"
    price = (90 / 100) * budget

print(f"{location} - {accomodation} - {price:.2f}")