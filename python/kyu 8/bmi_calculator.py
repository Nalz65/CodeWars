def bmi(weight, height):
    x = int(weight)/float(height*height)
    print(x)

    if x < 18.5:
        print("Your bmi is underweight")
    elif x >= 18.5 and x < 25.0:
        print("Your bmi is normal")
    elif x >= 25.0 and x < 30:
        print("your bmi is overweight")
    elif x > 30:
        print("You are obese")

bmi(80,1.6)

# Reference
# https://www.sololearn.com/Discuss/2686226/bmi-calculator-python-beginner-project