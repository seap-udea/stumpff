#!/bin/bash
from stumpff import *

#######################################################################
print("Computing stumpff series across two orders of magnitude...")
#######################################################################
errors=[]
delta=1e-14
from numpy import linspace
for t in linspace(-100,100):

    #Analytical values
    c0,c1,c2,c3=series_stumpff_analytic(t)
    
    #Search for the optimum value of N
    k=0
    error=1
    N=0
    while error>delta:
        N+=1
        error=error_series_stumpff(t,k,N)
    delta_c0=abs(series_stumpff(t,k,N)-c0)
    errors+=[delta_c0]
    
    #Search for the optimum value of N
    k=1
    error=1
    N=0
    while error>delta:
        N+=1
        error=error_series_stumpff(t,k,N)
    delta_c1=abs(series_stumpff(t,k,N)-c1)
    errors+=[delta_c1]

    #Search for the optimum value of N
    k=2
    error=1
    N=0
    while error>delta:
        N+=1
        error=error_series_stumpff(t,k,N)
    delta_c2=abs(series_stumpff(t,k,N)-c2)
    errors+=[delta_c2]

    #Search for the optimum value of N
    k=3
    error=1
    N=0
    while error>delta:
        N+=1
        error=error_series_stumpff(t,k,N)
    delta_c3=abs(series_stumpff(t,k,N)-c3)
    errors+=[delta_c3]

print(f"\tMaximum achieved error: {max(errors)}")

#######################################################################
print(f"Timing numerical stumpff series...")
#######################################################################
from timeit import Timer
Nr=1000
t=-10
all_stumpffs=lambda t:[series_stumpff(t,k) for k in range(4)]
time_series=Timer("all_stumpffs(t)",globals=globals()).timeit(Nr)/Nr*1e6
time_trigo=Timer("series_stumpff_analytic(t)",globals=globals()).timeit(Nr)/Nr*1e6
print(f"\tRunning time for series: {time_series:g} usec")
print(f"\tRunning time for trigonometric: {time_trigo:g} usec")
