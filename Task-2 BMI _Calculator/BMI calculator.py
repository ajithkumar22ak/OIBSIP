def calculate_bmi(weight, height):
    """
    This function calculates BMI using weight (kg)
    and height (meters)
    """
    return weight / (height * height)
print("✨BMI CALCULATOR📱")
try:
    weight = float(input("Dude Enter your weight in kilograms: "))
    height_cm = float(input("Dude Enter your height in centimeters: "))
    height = height_cm / 100
    if weight <= 0 or height <= 0:
        print("Please enter valid positive numbers.")
    else:
        bmi = calculate_bmi(weight, height)
        print("\nYour BMI is:", round(bmi, 2))

        if bmi < 18.5:
            print("Category:Dude your weight is Underweight😁")
        elif bmi < 25:
            print("Category:Dude your weight is  Normal weight(fitt Dude😎)")
        elif bmi < 30:
            print("Category:Dude your weight is  Overweight🤣")
        else:
            print("Category:Dude your weight is  Obese😂😂")
except ValueError:
    print("Invalid input😫Please enter numbers only.")
