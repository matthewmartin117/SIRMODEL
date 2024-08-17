import numpy as np
import io
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.use('Agg')

def calculate_sir_model(S, I, R, days):

    T  = days #number of days
    a= .05         # % new infection each day
    aS= 1 - a      # % remain suseptible
    rnI= .04       # recover no immunity
    rI= .1         # recover with immunity
    rD= .01        # die from disease


    A = np.matrix([[aS,rnI,0,0],[rnI+rD,(1-(rnI +rI + rD)) ,0,0],[0,rI,1,0],[0,rD,0,1]]) #dynamics matrix
    x1 = np.array([S,I,R,0]) #initial state: everyone healthy
    stateTraj = np.hstack([np.vstack(x1),np.zeros((4,T-1))]) #initialize trajectory with 0s
    for t in range(T-1):
        stateTraj[:,t+1] = np.matmul(A,stateTraj[:,t])

    for i in range(len(stateTraj)):
        plt.plot(range(T),stateTraj[i])




    # Add labels and title
    plt.xlabel('Time (days)')
    plt.ylabel('Population')
    plt.title('SIRD Model Simulation')
    plt.legend(["Susceptible","Infected","Recovered","Deceased"])

    # Save the plot to a BytesIO object
    img_io = io.BytesIO()
    plt.savefig(img_io, format='png')
    img_io.seek(0)
    plt.close()  # Close the figure to avoid resource leaks

    return img_io



