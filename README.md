# MSSE 272 — Project 1: Many-Particle Simulation

This project simulates the 2D motion of many particles subject to a nonlinear restoring force using Newtonian dynamics.  
It demonstrates numerical integration, scientific visualization, and modern modular Python design aligned with real scientific-computing workflows.

---

## Simulation GIF

<p align="center">
  <img src="results/simulation.gif" width="450">
</p>

---

## Physical Model

Particle motion evolves according to Newton’s second law.


**Position update (semi-Verlet):**  
$x(t+\Delta t) = x(t) + v_x(t)\,\Delta t + \tfrac{1}{2}a_x(t)\Delta t^2$  
$y(t+\Delta t) = y(t) + v_y(t)\,\Delta t + \tfrac{1}{2}a_y(t)\Delta t^2$  

**Velocity update:**  
$v_x(t+\Delta t) = v_x(t) + a_x(t)\Delta t$  
$v_y(t+\Delta t) = v_y(t) + a_y(t)\Delta t$  

where $\Delta t$ is the time step.

**Nonlinear restoring force:**  
$F_x = -c x^2 \text{sign}(x)$  
$F_y = -c y^2 \text{sign}(y)$



Randomized particle masses introduce heterogeneous acceleration responses, producing diverse trajectories and characteristic collapse dynamics.

---


