import numpy as np
import pandas as pd

class class_missingValue:
    X = []
    y = []
    a = []
    b = []
    name = ''

    def __init__(self, data, pick=None):
        self.X = data.X
        self.y = data.y
        self.a = np.isnan(data.X)
        self.name = pick
        self.pick()
        #self.b = np.isnan(data.y)

    def pick(self):
        if self.name == "max":
            self.max()
        elif self.name == "median":
            self.median()

    def max(self):
        print('Mengatasi Missing Value Dengan Max')
        self.X[self.a] = np.nanmax(self.X)
        #self.y[self.a] = np.nanmax(self.y)

    def median(self):
        print('Mengatasi Missing Value Dengan Median')
        self.X[self.a] = np.nanmedian(self.X)

