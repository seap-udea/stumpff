#!/bin/bash
from stumpff import *

#######################################################################
print("Computing stumpff series across two orders of magnitude...")
#######################################################################
#Range to explore
from numpy import log10,logspace,linspace,hstack
trange1=logspace(-5,0,10)
trange2=linspace(0,100,200)

errors=[]
for t in hstack((-trange2,-trange1,trange1,trange2)):
    #Analytical values
    c0,c1,c2,c3=ck_analytic(t)
    errors+=[abs(ck(t,0)-c0),abs(ck(t,1)-c1),
             abs(ck(t,2)-c2),abs(ck(t,3)-c3)]
print(f"\tMaximum achieved error: {max(errors):.1e}")

#######################################################################
print(f"Timing numerical stumpff series...")
#######################################################################
from timeit import Timer
Nr=1000
t=1
all_stumpffs=lambda t:[ck(t,k) for k in range(4)]
time_series=Timer("all_stumpffs(t)",globals=globals()).timeit(Nr)/Nr*1e6
time_trigo=Timer("ck_analytic(t)",globals=globals()).timeit(Nr)/Nr*1e6
print(f"\tRunning time for series: {time_series:g} usec")
print(f"\tRunning time for trigonometric: {time_trigo:g} usec")
