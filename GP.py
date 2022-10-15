from typing import List
from pprint import pprint

def grap_generate( plane:List[list],limit: int ) -> List[list] :
    '''
    Graph generated from trajectories I, II, III.
    Takes into account the number of dates that go to each point
    '''

    row: int = len(plane) -1
    column: int = 1    
    slope: int = 0
    #type I trajectory
    while column <= limit:
        if row < 0 or column > len(plane)-1: 
            break 

        plane[row][column] = 1

        slope += 1
        row -= slope
        column += 1

    #type II trajectory 
    row: int = len(plane) -1
    column: int = 1    
    slope: int = 0
    while column <= limit:
        if row < 0 or column > len(plane)-1: 
            break 

        plane[row][column] = 1

        slope += 1
        row -= slope
        column += 1




    return plane


def m_g(c: int, r: int)-> List[list]:
    '''
    nxn matrix generator
    '''
    matrix = [[0 for col in range(c)] for row in range(r)]



    return matrix

import plotly.express as px
import pandas as pd

import plotly.graph_objects as go

x = [0,1, 2, 3, 4, 5]

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=x,
    y=[0, 0, 1, 3 ],
    name = 'Type I', 
    legendgroup='Type I',
    marker=dict(color='red'),
))


fig.add_trace(go.Scatter(
    x=x,
    y=[None, 0, 0, 1, 3],
    name = 'Type II', 
    legendgroup='Type II',
    marker=dict(color='blue'),
))

fig.add_trace(go.Scatter(
    x=x,
    y=[None, None, 1, 1, 2],
    name = 'Type II', 
    legendgroup='Type II',
    marker=dict(color='blue'),
    showlegend=False,
))


fig.add_trace(go.Scatter(
    x =x,
    y =[None, None, None, 3, 3],
    name = 'Type II', 
    legendgroup='Type II',
    marker=dict(color='blue'),
    showlegend=False,
))

fig.add_trace(go.Scatter(
    x =x,
    y =[None, None, 0, 0],
    name = 'Type III', 
    legendgroup='Type III',
    marker=dict(color='green'),
))

fig.add_trace(go.Scatter(
    x =x,
    y =[None, None, None, 1, 1, 2],
    name = 'Type III', 
    legendgroup='Type III',
    marker=dict(color='green'),
    showlegend=False,
))

fig.add_trace(go.Scatter(
    x =x,
    y =[None, None, None, None, 2, 2],
    name = 'Type III', 
    legendgroup='Type III',
    marker=dict(color='green'),
    showlegend=False,
))


fig.show()



if __name__ == "__main__":
    pass

    #pprint(m_g(3, 6))
    #print("")
    #pprint(grap_generate( m_g(3,6),20))

