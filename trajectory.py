import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

#symbols
a0, a1, a2, a3, t = sp.symbols('a0, a1, a2, a3, t')

#the polynomial function
pos= a0 + a1*t + a2*t**2 + a3*t**3  #positon
vel = sp.diff(pos,t) #velocity, deravative of positon
acc = sp.diff(vel,t)    #acceleration, deravative of velocity

# initial conditions
init_pos = pos.subs(t,0)    #[1, 0, 0, 0]
final_pos = pos.subs(t,2)  #[1, 2, 4, 8]
init_vel = vel.subs(t,0)    #[0, 0, 0, 0]
final_vel = vel.subs(t,2)   #[0, 1, 4, 12]

#TODO PRINT equation to put in report
#print(final_vel)

a = np.array([[1, 0, 0, 0], [1, 2, 4, 8], [0, 1, 0, 0], [0, 1, 4, 12]])
#initial conditions (initial_position, final_position, initial_velocity, final_velocity)
b = np.array([1, 4, 0, 0])
co_of = np.linalg.solve(a, b)   #[ 1.    0.    2.25 -0.75]
t = np.linspace(0, 2, 1000)

#problem with ploting a sympy
#position = pos.subs({a0:co_of[0], a1:co_of[1], a2:co_of[2], a3:co_of[3]})
#position = 1.25*t**3 - 4.75*t**2 + 4.0*t + 1.0
position = 1 + 2.25*t**2 -0.75*t**3
velocity = 2*2.25*t+3*-0.75*t**2
acceleration = 2*2.25+6*-0.75*t
#plot
plt.figure()
plt.plot(t, acceleration)
plt.show()

#References
#https://docs.scipy.org/doc/numpy/reference/generated/numpy.linalg.solve.html
#https://www.youtube.com/watch?v=HSq3JexqZ5k
