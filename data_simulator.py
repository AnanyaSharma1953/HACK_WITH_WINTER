import numpy as np

def generate_data(n=200):
    temperature = np.random.normal(50, 3, n)
    vibration = np.random.normal(10, 1, n)
    power = np.random.normal(200, 10, n)

    # Inject anomalies at the end
    temperature[-10:] += 15
    vibration[-10:] += 5

    return np.column_stack((temperature, vibration, power))
