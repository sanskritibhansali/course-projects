# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 18:06:38 2019

@author: Sanskriti
"""
import math
import numpy as np
import matplotlib.pyplot as plt

m0=459790
mp=151200
m=np.zeros(80)
mu = 3.986e14
Re = 6378000

#t=128
beta=mp/128

mp1=beta*20
g_b=9.7896
g_o=9.81
isp=261*4
s=20
M=np.zeros(128)
t=np.linspace(0,128,128)
theta0=10*np.pi/180
q0=g_o*np.sin(theta0)/V
theta_b = q0*108 + theta0
for i in range(128):
    if i<20:
        M[i]=m0-beta*i
    else:
        M[i]=m0*np.exp(2*(np.sin(theta0)-np.sin(theta0 + q0*i))/(q0*isp))
plt.figure()        
plt.plot(t,M)        
        
    

V=g_o*isp*np.log(m0/(m0-(mp1)))-g_o*s
h=m0*g_o*isp/beta*(((1-(mp1/m0))*np.log(1-(mp1/m0)))+(mp1/m0))-(.5*g_o*s*s)
h_0 = m0*g_o*isp/beta
lambd = (mp1)/m0
h_1 = (((1-lambd)*np.log(1-lambd))+lambd)
h_2 = 0.5*g_o*s*s
H= h_0*h_1-h_2 
print(V)
print(h)
print(H)
print(beta)

theta0=10*np.pi/180
q0=g_o*np.sin(theta0)/V
theta_b = q0*108 + theta0
vel = g_o*np.sin(theta_b)/q0 
m = m0*np.exp(2*(np.sin(theta0)-np.sin(theta_b))/(q0*isp))
h1 = (g_o/(4*q0*q0))*(np.cos(2*theta0)-np.cos(2*theta_b)) + h
x = (g_o/(2*q0*q0))*((theta_b-theta0)-((np.sin(2*theta_b)-np.sin(2*theta0))/2))+0
e = vel*vel/2 - (mu/(Re+h1))
print(vel)
print(h1)  
print(q0)
print(theta_b)  
print('stage one done')
m1=295790
mp_1=187000
theta1=theta_b
isp2=289
q1=g_o*np.sin(theta1)/vel
theta_b1 = q1*166 + theta1
vel1 = g_o*np.sin(theta_b1)/q1 
m = m1*np.exp(2*(np.sin(theta1)-np.sin(theta_b1))/(q1*isp2))
h2 = (g_o/(4*q1*q1))*(np.cos(2*theta1)-np.cos(2*theta_b1)) + h1
x1 = (g_o/(2*q1*q1))*((theta_b1-theta1)-((np.sin(2*theta_b1)-np.sin(2*theta1))/2))+x
e1 = vel1*vel1/2 - (mu/(Re+h2))
print(vel1)
print(h2)    
print(e)
print(e1)


print('stage 2 done')
M1=np.zeros(166)
t1=np.linspace(0,166,166)
for i in range(166):
    M1[i]=m1*np.exp(2*(np.sin(theta1)-np.sin(theta1 + q1*i))/(q1*isp2))
plt.figure()        
plt.plot(t1+128,M1)

theta2=theta_b1 -1

q2=g_o*np.sin(theta2)/vel1
theta_b2 = q2*295 + theta2
vel2 = g_o*np.sin(theta_b2)/q2 
m = m2*np.exp(2*(np.sin(theta2)-np.sin(theta_b2))/(q2*isp3))
h3 = (g_o/(4*q2*q2))*(np.cos(2*theta2)-np.cos(2*theta_b2)) + h2
x2 = (g_o/(2*q2*q2))*((theta_b2-theta2)-((np.sin(2*theta_b2)-np.sin(2*theta2))/2))+x1
e2 = vel2*vel2/2 - (mu/(Re+h3))
print(m)
print(theta_b2)
print(vel2)
print(h3)    
print(e2)

M2=np.zeros(295)
t3=np.linspace(0,295,295)
for i in range(295):
    M2[i]=m2*np.exp(2*(np.sin(theta2)-np.sin(theta2 + q2*i))/(q2*isp3))
plt.figure()        
plt.plot(t3+128+166,M2)


#code for constant velocity profile
#theta1 = theta_b
#theta_final = 2*np.arctan((np.tan(theta1/2))*np.exp(g0*166/vel))
   
#m_final= m1*np.power((np.sin(theta_final)/np.sin(theta1)),(-vel/(g_o*isp)))
   
#h_final = h + ((vel*vel)/g_o)*np.log((np.sin(theta_final))/np.sin(theta1))
   
#x_final = x + vel*vel*(theta_final-theta1)/g_o  
  
#e = vel*vel/2 - mu/(Re + h_final)
#print(theta_final)
#print(h_final)   