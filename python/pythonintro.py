# Intro to Python: Types

# LHS(Left hand side): variable
# Assignment operator(=): assigns the value on the RHS to the 
# variable on the the LHS
# RHS(Right Hand Side): value
# Statement: is a general term for a single instruction
#            that uses or manipulates a value

# Age is an integer, because it holds whole number

age = 20
print(age)

# Float(floating point number)
PI = 3.14159
print(PI)



# Boolean: True/False value
isRaining = False

# String: combination of alphanumeric values
name = 'Dre'
team = "Atlanta United's team"
months = '''
January, Febraury,
March, April
'''
print(name)
print(months)

# List: a sequence values
scores = [13.42, 54.5643, 53.542, 32.6343] 

# Dictionary: a sequence of labeled values
nbateams = ({"Atlanta": "Hawks", "Houston": "Rockets", "Orlando": "Magic"})


#----------------------------------------------------------------------------

# Special Characters
# \b: backspace
# \t: horizontal tab
# \v: vertical tab
# \n: newline
# \r: carriage return 

weather = 'rainy\tsunny\ncloudy\vhail\rhurricane\b'
print(weather)

#-------------------------------------------------------------

# interpolation operator: takes values that are stored in variables an d places in a string
# username = input('Type in your username: ')
# password = input('Type in your password: ')
print('Welcome %s' % age)
print('Pi: %.3f' % PI)

#------------------------------------------------------------

result = 4/2
print('Result: ', result)
positiveNum = abs(-32)
print(positiveNum)
exponents = pow(2, 2)
rounding = round(PI)
print(exponents, rounding)

#-----------------------------------------------
# Control Flow

currentTemp = 20
freezingTemp = 32

if currentTemp <= freezingTemp:
    print('its freezing')
elif currentTemp == freezingTemp:
    print('its at freezing')
else:
    print('not condition covers this value')


# Multiple conditions
isSunny = False

# if both cases are not met then the block of code is not run
if currentTemp < freezingTemp and isRaining == True:
    print('its freezing and rainy')
elif currentTemp > freezingTemp or isRaining == False:
    print('its a nice day')
else:
    print('its an uncomfortable day')


if isSunny != True:
    print('its cloudy')

#--------------------------------------

#Lists
georgiaResidents = ['Dez', 'Matt', 'Dre']

# The first index of a list(array) is 0
print(georgiaResidents[2])


# interates through the array for each element in the array
for name in georgiaResidents:
    if name == 'Dre':
        print('Instructor')
    elif name == 'Dez':
        print('TA')
    else:
        print('Student')

# interates  up to 5 times
for number in range(5):
    print(number)

#city = 'Atlanta'
#print(city[10])

georgiaResidents.pop()
#print(georgiaResidents[2])

# While Loop: we must set the exit condition. If exit condition is not met then we run into an infinite loop
i = 1
while i < 10:
    print(i)
# -----------------------------------------------------------------------------------------------------------------
