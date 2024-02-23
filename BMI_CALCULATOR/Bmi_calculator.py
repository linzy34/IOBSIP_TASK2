def calculate_bmi(weight, height):
    return weight / (height ** 2)

def bmi_categorize(bmi):
    if bmi < 18.5:
        return "You are underweight"
    elif 18.5 <= bmi < 25:
        return " You are normal"
    elif 25 <= bmi < 30:
        return "You are overweight"
    else:
        return "You are obese"

def main():
    print("Welcome to the Body Mass Index Calculator..")
    weight = float(input("Enter your weight in kilogram:"))
    height = float(input("Enter your height in metre:"))

    bmi = calculate_bmi(weight,height)
    category = bmi_categorize(bmi)

    print(f"Your bmi is : {bmi:.2f}")
    print(f"Your are classified as : {category}")
main()
