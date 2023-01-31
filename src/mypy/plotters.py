import matplotlib.pyplot as plt
import pandas as pd

def plot1d(data: (list or pd.DataFrame), x=None, y=None, figsize=(6,5), savefig=None, show=False):
    
    fig, ax = plt.subplots(figsize=figsize)
    
    if isinstance(data, pd.DataFrame):
        print("pd Plot")
        if (x is not None) and (y is not None):
            data.plot(x=x, y=y, ax=ax)
        else:
            raise ValueError("Tring to plot a pd.DataFrame without x and y col labels.")
    elif isinstance(data, list):
        if len(list) == 1:
            print("Only y data")
        elif len(list) == 2:
            print("X and Y data")
        else:
            raise ValueError(f"data input is a list of a len different than 1 or 2.")
    else:
        raise ValueError(f"data is neither a pd.DataFrame or a list of np.arrays...")
    
    if savefig is not None:
        fig.savefig(savefig)
    if show:
        plt.show()

    return fig, ax