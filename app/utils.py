import numpy as np
import io
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.use('Agg')

def calculate_sir_model(S, I, R, a, b, t_final, number_of_steps):
    # Parameters
    death_rate = 0.1  # 10% of recovered cases lead to death
    D = 0  # Initial deaths

    # Time parameters
    t_initial = 0
    delta_t = (t_final - t_initial) / number_of_steps
    t = t_initial

    # Total population for fixed plot window
    total_population = S + I + R

    # Lists to store the values for plotting
    t_values = [t]
    S_values = [S]
    I_values = [I]
    R_values = [R]
    D_values = [D]

    # Simulation loop
    for _ in range(number_of_steps):
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
        t += delta_t
        S += delta_S
        I += delta_I
        R += delta_R
        D += delta_D

        # Store the values
        t_values.append(t)
        S_values.append(S)
        I_values.append(I)
        R_values.append(R)
        D_values.append(D)

    # Plotting the results
    plt.figure()
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

    # Save the plot to a BytesIO object
    img_io = io.BytesIO()
    plt.savefig(img_io, format='png')
    img_io.seek(0)
    plt.close()  # Close the figure to avoid resource leaks

    return img_io

# Example usage
img_io = calculate_sir_model(45400, 2100, 2500, 0.01786, 14, 30, 30)

# The img_io object can now be used to return the image in a web application or save it to a file.
