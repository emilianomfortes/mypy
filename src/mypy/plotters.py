import matplotlib.pyplot as plt
import pandas as pd

def plot1d(data: (list or pd.DataFrame), ):
    
    if isinstance(data, pd.DataFrame):
        print("pd Plot")
    elif isinstance(data, list):
        if len(list) == 1:
            print("Only y data")
        elif len(list) == 2:
            print("X and Y data")
        else:
            raise ValueError(f"data input is a list of a len different than 1 or 2.")
    else:
        raise ValueError(f"data is neither a pd.DataFrame or a list of np.arrays...")