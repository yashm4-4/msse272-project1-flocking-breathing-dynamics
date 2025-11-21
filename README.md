# MSSE 272 — Project 1: Flocking & Breathing Dynamics Simulation

This project simulates the 2D motion of many particles interacting with a nonlinear restoring force, producing “flocking” and “breathing” behavior, both being characteristics of collective biological motion.

The system evolves according to Newtonian dynamics and is integrated using a semi-Verlet scheme, demonstrating key ideas in numerical simulation, force modeling, and visual pattern formation.

The resulting motion shows particles contract towards the center and then expanding out again, showcasing an organism-like “breathing” pattern.

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


