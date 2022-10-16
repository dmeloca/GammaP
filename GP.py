from typing import List
from pprint import pprint

import plotly.express as px
import pandas as pd
import plotly.graph_objects as go


def TG_I(root:int ,counter: int) -> list[int]:
    '''
    Genera las trayectorias de tipo uno
    '''
    x = [0, 1, 2, 3, 4, 5] #width
    y = list()
    slopes = list()

    if counter >0: #blank spaces
         for i in range(0, counter): y.append(None); slopes.append(None)
    #initiation
    slopes.append(0)
    y.append(root) 

    for slope in range(0, len(x)-len(y)): y.append(slope+y[slope+counter]); slopes.append(slope) #points in y

    if counter == 0: #graphing
        fig = go.Figure()
        fig.add_trace(go.Scatter(
        x=x,
        y=y,
        name = 'Type I', 
        legendgroup='Type I',
        marker=dict(color='red'),))
        return y,fig

    #fig.show()

    return y

def TG_II(TI:list[int], fig) :
    '''
    Genera las trayectorias de tipo dos
    '''
    x = [0, 1, 2, 3, 4, 5] #width

    for i in range(1,len(TI)):
        y = TG_I(TI[i],i )
        c = True #legend
        if i > 1: c = False 

        fig.add_trace(go.Scatter(
        x=x,
        y=y,
        name = 'Type II', 
        legendgroup='Type II',
        marker=dict(color='blue'),
        showlegend= c,))
        
def TG_III():
    pass



    #fig.show()


def m_g(c: int, r: int)-> List[list]:
    '''
    nxn matrix generator
    '''
    matrix = [[0 for col in range(c)] for row in range(r)]



    return matrix

def testplots():
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
    y, fig= TG_I(0,0)
    
    TG_II( y, fig)


