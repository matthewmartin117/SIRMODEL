import numpy as np
import numpy.linalg as npl
import math
import matplotlib.pyplot as plt
from scipy.integrate import odeint
def calculate_sir_model(S, I, R, a, b, t_final, number_of_steps):
      # Implement SIR model calculations
      # Return values or plot
      #Use Pseudocode from Calculus in Context, Chapter 2 page 69 to plot the 3 functions S, I and R. Use a (.00001)and b (14) as varibles instead of numbers
  #Use a fixed plot window with y as the total height and fix the number of days you want to explore.
  # Set parameters
  a = 0.00001  # Infection rate
  b = 14  # Recovery rate
  death_rate = 0.1  # 10% of recovered cases lead to death

  # Initial conditions
  t_initial = 0
  t_final = 30  # Time in days
  t = t_initial
  S = 45400
  I = 2100
  R = 2500
  D = 0  # Initial deaths
  number_of_steps = 30
  delta_t = (t_final - t_initial) / number_of_steps

  # Total population for fixed plot window
  total_population = S + I + R

  # Lists to store the values for plotting
  t_values = [t]
  S_values = [S]
  I_values = [I]
  R_values = [R]
  D_values = [D]

  # Simulation loop
  for k in range(1, number_of_steps + 1):
      # Calculate rate of change
      S_prime = -a * S * I
      I_prime = a * S * I - I / b
      R_prime = (1 - death_rate) * I / b
      D_prime = death_rate * I / b

      # Calculate the changes
      delta_S = S_prime * delta_t
      delta_I = I_prime * delta_t
      delta_R = R_prime * delta_t
      delta_D = D_prime * delta_t

      # Update the variables
      t = t + delta_t
      S = S + delta_S
      I = I + delta_I
      R = R + delta_R
      D = D + delta_D

      # Store the values
      t_values.append(t)
      S_values.append(S)
      I_values.append(I)
      R_values.append(R)
      D_values.append(D)

  # Plotting the results
  plt.plot(t_values, S_values, label="Susceptible")
  plt.plot(t_values, I_values, label="Infected")
  plt.plot(t_values, R_values, label="Recovered")
  plt.plot(t_values, D_values, label="Deaths")

  # Setting a fixed y-axis for better comparison
  plt.ylim(0, total_population)

  # Add labels and title
  plt.xlabel('Time (days)')
  plt.ylabel('Population')
  plt.title('SIRD Model Simulation')


  plt.legend()

  # Show the plot
  plt.show()