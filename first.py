def age_group(age):
    if age<0:
        return "Invalid Age"
    elif age>0 and age<13:
        return "Child"
    elif age>=13 and age<19:
        return "Teenager"
    elif age>=20 and age<60:
        return "Adult"
    elif age>=60 and age<100:
        return "Senior"


# print(age_group(25))


def ticket_price(age,day):
    if day=="wed":
        if age < 18:
            return 8 - (8 * 0.02)
        else:
            return 12 - (12 * 0.02)
    else:
        if age < 18:
            return 8
        else:
            return 12


# print(ticket_price(22,"wed"))

def grade_calculator(score):
    if(score<100 and score>=90):
        return "A"
    elif(score<90 and score>=80):
        return "B"
    elif (score<80 and score>=70):
        return "C"
    else:
        return "F"

# print(grade_calculator(84))

def fruit_ripeness(color):
    match color:
        case "green":
           return "Unripe"
        case "yellow":
           return "Ripe"
        case "brown":
           return "Overripe"
    # if (color=="green"):
    #     return "Unripe"
    # elif (color=="yellow"):
    #     return "Ripe"
    # elif (color=="Brown"):
    #     return "Overripe"

# print(fruit_ripeness("green"))


def weather_activity_suggestion(weather):
    if weather.lower() == "sunny":
        return "Go for a walk"
    elif weather.lower() == "rainy":
        return "Read a book"
    elif weather.lower() == "snowy":
        return "Build a snowman"

# print(weather_activity_suggestion("RAiny"))


def transportation_selection(distance):
    if distance <= 3:
        return "Walk"
    elif distance > 3 and distance < 16:
        return "Bike"
    else:
        return "Car"

# print('transportation_selection',transportation_selection(13))


def password_strength(password=""):
    if len(password)<=6:
        return "Weak"
    elif len(password)>6 and len(password)<=10:
        return "Medium"
    else:
        return "Strong"

# print(password_strength("Helasdfafsdalo"))

