"""
BMI CategorizerGoal: Calculate $BMI = weight/(height^2) and classify (
Underweight < 18.5, 
Normal 18.5-24.9, 
Overweight 25-29.9, 
Obese 30+).
Input             Output
70 (kg), 1.75 (m) Normal
100 (kg), 1.70 (m) Obese
"""
weight, height = map(float, input("Enter the Weight and Height ").split())
bmi = weight/(height**2)
if bmi < 18.5:
    print("Underweight")
elif bmi<25:
    print("Normal")
elif bmi<30:
    print("Overweight")
else:
    print("Obese")