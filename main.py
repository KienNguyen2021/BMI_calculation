weight = float(input ("enter your weights in kg : "))
height = float(input ("enter your height in meter : "))

bmi = float (weight / (height ** 2)) // 2 power 2
bmi_integer = int(bmi)
print ("your BMI is : " + str(bmi_integer))
