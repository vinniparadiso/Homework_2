#Vincenza Paradiso Homework 2
#Problem 1
def print_name(name):
    print("The name is", name)
print_name("Vinni")
print_name("Paradiso")

#Problem 2
def ninety(a,b,c):
    d= 90*4-(a+b+c)
    return d
print(ninety(27,32,48))

#Problem 3
def miles_per_hour(miles, hours, minutes, seconds):
    a=miles
    b=hours
    c=minutes/60
    d=seconds/3600
    speed=a/(b+c+d)
    return speed
print(miles_per_hour(20,2,21,16))

#Problem 4
def name(x):
    if x=="Chris":
        print("Hello Chris!")
    else:
        print("Goodbye!", x)
name("Vinni")
name("Chris")

#Problem 5
def convert_temperature(temp,units):
    if units=="celsius":
        new_temp=temp*(9/5+32)
        return new_temp
    elif units=="farenheit":
        new_temp_2=(temp-32)*5/9
        return new_temp_2
print(convert_temperature(27,"celsius"))
print(convert_temperature(27,"farenheit"))

#Problem 6
def calculate_grade(score):
    if score>=90:
        print("You have an A.")
    if 80<=score<90:
        print("You have a B.")
    if 70<=score<80:
        print("You have a C.")
    if 60<=score<70:
        print("You have a D.")
    if score<60:
        print("You have a F.")
print(calculate_grade(99))
print(calculate_grade(27))
print(calculate_grade(86))