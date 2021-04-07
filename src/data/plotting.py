import plotly
import plotly.graph_objs as go

import pandas as pd
import numpy as np
import json


def create_plot(feature="bar"):
    """provided random generated plots"""
    if feature == "bar":
        N = 40
        x = np.linspace(0, 1, N)
        y = np.random.randn(N)
        df = pd.DataFrame({'x': x, 'y': y})  # creating a sample dataframe
        data = [
            go.Bar(
                x=df['x'],  # assign x as the dataframe column 'x'
                y=df['y']
            )
        ]
    else:
        N = 1000
        random_x = np.random.randn(N)
        random_y = np.random.randn(N)

        # Create a trace
        data = [go.Scatter(
            x=random_x,
            y=random_y,
            mode='markers'
        )]

    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON
