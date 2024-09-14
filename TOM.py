import math

RPM = float(input("Enter the RPM : "))
crank = float(input("Enter the Crank in m : "))
connection_Rod = float(input("Enter the connecting rod in m : "))
Mass_reciprocatingParts = float(input("Enter the Mass reciprocating Parts in kg : "))
#Crank_angle = float(input("Enter the value"))
Gas_pressure =float(input("Enter the Gas pressure in N/m^2: "))
Diameter =  float(input("Enter the Diameter in m : "))
mim = int(input("Enter the minimum angle : "))
max = int(input("Enter the maximum angle : "))

FPS = []
angle=[]
for Crank_angle in range(mim,max+10,10):
    angle.append(Crank_angle)
    W = (2*math.pi*RPM/60)

    N = crank/connection_Rod

    Area = (math.pi/4)*Diameter

    FL = Area*Gas_pressure

    cos = math.cos(math.radians(Crank_angle))
    #cos_inverse= math.acos(cos)
    #cos_inverse_value= math.degrees(cos_inverse)

    cos2 = math.cos(math.radians(Crank_angle*2))
    #cos_inverse2= math.acos(cos)
    #cos_inverse_value2= math.degrees(cos_inverse)

    cosBy2 = (cos+cos2)/N
        
    sin= math.sin(math.radians(Crank_angle))
    radians_value = math.asin(sin)
    degrees_value = math.degrees(radians_value)

    FI = Mass_reciprocatingParts*crank*(W**2)*cosBy2

    FP = FL-FI+Mass_reciprocatingParts
    formatted_value = format(FP, '.2f')

    FPS.append(formatted_value)

print(FPS)

import numpy as np
import matplotlib
matplotlib.use('TkAgg')  # Or another backend, depending on your setup
import matplotlib.pyplot as plt
x=angle
y=FPS
plt.figure(figsize=(12,12))
plt.plot(x,y, label='net force', color='blue')
plt.title('Net Force As Per Angle')
plt.xlabel('Angle of Crank')
plt.ylabel('Net Force on the piston')
plt.legend()
plt.grid(True)
plt.show()

