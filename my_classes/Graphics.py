import numpy as np
import matplotlib.pyplot as plt

class GrahicCalculations:
    def __init__(self):
        pass

    def compute_linear_regression(self, x, y, y_uncertainty):
        w = 1 / y_uncertainty**2
        delta = sum(w) * np.cdot(w, x**2) - np.cdot(x,w)**2
        slope_t1 = sum(w) * sum(x*y*w)
        slope_t2 = sum(w*y)*sum(w*x)

        self.slope = (slope_t1 - slope_t2) / delta
        self.slope_uncertainty = (np.cdot(w, x**2) / delta)**0.5

        self.origin = (np.cdot(w, x**2) * np.cdot(w,y) - np.cdot(w,x)* sum(x*y*w)) / delta
        self.origin_uncertainty = (sum(w) / delta) ** 0.5
    
    def linear_regression(self, x):
        return self.origin + self.slope * x
    
    

