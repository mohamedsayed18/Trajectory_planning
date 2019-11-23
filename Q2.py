#question 2
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

#number of conditions = 7
a0, a1, a2, a3, a4, a5, a6, a7, t = sp.symbols('a0, a1, a2, a3, a4, a5, a6, a7, t')#symbols

#polynomial position profile.
pos = a0 + a1*t + a2*t**2 + a3*t**3  #positon
vel = pos.diff(t)  #velocity
#a1 + 2*a2*t + 3*a3*t**2 + 4*a4*t**3 + 5*a5*t**4 + 6*a6*t**5
acc = vel.diff(t)  #acceleration
#2*a2 + 6*a3*t + 12*a4*t**2 + 20*a5*t**3 + 30*a6*t**4

#init_pos = pos.subs(t,0)    #[1, 0, 0, 0]
mid_pos = pos.subs(t,2)     #
final_pos = pos.subs(t,4)  #
#init_vel = vel.subs(t,0)    #
final_vel = vel.subs(t,4)   #
#init_acc = acc.subs(t,0)    #[]
final_acc = acc.subs(t,4)   #
#print(final_vel)
'''
#print(init_pos)
print(mid_pos)
print(final_pos)
#print(init_vel)
print(final_vel)
#print(init_acc)
print(final_acc)
'''
#spline_1
c = np.array([[1,0,0,0],
[1,2,4,8],
[0,1,0,0],
[0,0,2,0]])
d = np.array([1,2,0,0])
coof1 = np.linalg.solve(c, d)

#spline_2
a = np.array([[1,2,4,8],
[1,4,16,64],
[0,1,8,48],
[0,0,2,24]])
b = np.array([2,0,0,0])
coof2 = np.linalg.solve(a, b)
print(coof2)
#[ 1.00000000e+00 -7.10542736e-15  2.88281250e+00 -3.27929687e+00
#  1.53222656e+00 -3.26660156e-01  2.56347656e-02]
#splines_1 [ 1.     0.    -0.     0.125] ,
#splines_2 [ 16.   -12.     3.    -0.25]

t = np.linspace(0, 2, 1000)
position_1 = coof1[0] + coof1[1]*t + coof1[2]*t**2 + coof1[3]*t**3
velocity_1 = coof1[1] + 2*coof1[2]*t + 3*coof1[3]*t**2
acceleration_1 = 2*coof1[2] + 6*coof1[3]*t

t2 = np.linspace(2, 4, 1000)
position_2 = coof2[0] + coof2[1]*t2 + coof2[2]*t2**2 + coof2[3]*t2**3
velocity_2 = coof2[1] + 2*coof2[2]*t2 + 3*coof2[3]*t2**2
acceleration_2 = 2*coof2[2] + 6*coof2[3]*t2

#plot
plt.figure()
plt.plot(t, acceleration_1)
plt.plot(t2, acceleration_2)
plt.show()
