def h_and_b(weight, height, age, gender):
    if gender == "f":
        BMR = 655.1 + (9.563 * weight) + (1.850 * height) - (4.676 * age)
   
    elif gender == "m":
        BMR = 66.5 + (13.75 * weight) + (5.003 * height) - (6.755 * age)
    return BMR

def r_and_s(weight, height, age, gender):
    if gender == "f":
        BMR = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
   
    elif gender == "m":
        BMR = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    return BMR


def m_and_s(weight, height, age, gender):
    if gender == "f":
        BMR = (10 * weight) + (6.25 * height) - (5 * age) - 161
   
    elif gender == "m":
        BMR = (10 * weight) + (6.25 * height) - (5 * age) + 5
    return BMR

def convert_pounds_to_kg(pounds):
    kg = pounds/2.2046
    kg1 = round(kg,2)   # 5 function also need to round
    return kg1

def convert_inches_to_cm(inches):
    cm = inches/0.39370
    return cm


def main():
    weight = float(input("Weight in pounds:  "))  
    height = float(input("Height in inches:  "))
    age = int(input("Age:  "))
    gender = input("Gender:  ")
    weight = weight/2.2046
    height = height/0.39370
    print("Your weight in kilograms:  ", round(weight,2))
    print("Your height in centimeters:  ", round(height,2))
    print("Harris and Benedict BMR:  ", round(h_and_b(weight, height, age, gender),2))
    print("Roza and Shizgal BMR:  ", round(r_and_s(weight, height, age, gender),2))
    print("Mifflin and St Jeor BMR:  ", round(m_and_s(weight, height, age, gender),2))

main()

