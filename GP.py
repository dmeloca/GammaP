from typing import List, Tuple
from pprint import pprint

import plotly.graph_objects as go

TYPE = ["Type I", "Type II", "Type III"]
COLORS = ["red", "green", "blue"]

def Trajectory(points:list[list], t:int, fig:go.Figure, classes:list) -> list[list]:
    '''
    Inserts trajectories of type t starting at every point in the list points into the figure fig
    '''
    newPoints = list() #List of points of type t
    for p in points: #Every new trajectory of type t starts at point p
        x = [p[0]]
        y = [p[1]]
        s = [p[2]] #max slope in the trajectories that cross the point (x, y)
        slope = 0
        '''
        Checks if it is possible to draw a new line in the current trajectory
        If the trajectory is of type 2 (III), the slope of every new line
        must be lesser or equal than the slope of the previous lines
        The coordinate y always must be lesser than 20
        '''
        while((t != 2 or slope <= s[-1]) and x[-1] < 9 and y[-1] + slope < 20):
            x.append(x[-1] + 1)
            y.append(y[-1] + slope)
            s.append(max([slope, s[-1]]))
            newPoints.append([x[-1], y[-1], s[-1]])
            #Adds a unit into the correspondent class
            if(x[-1] >= 0 and y[-1] >= 0):
                classes[x[-1] + y[-1]] += 1
            slope += 1
        fig.add_trace(
            go.Scatter(
                x = x,
                y = y,
                name = TYPE[t], 
                legendgroup = TYPE[t],
                marker = dict(color=COLORS[t]),
                text = s,
                showlegend=False,
            )
        )
    return newPoints
    
def graphGenerator(x_0:int, y_0:int) -> go.Figure:
    '''
    Returns the graph of the trajectories of type I, II and III
    and a list where the i-th position stores the number of trajectories
    that cross the points of the class 'i' (points such as the sum of its
    coordinates (x,y) is 'i'. x+y=i)
    '''
    fig = go.Figure()
    classes = [0 for i in range(30)]
    t1 = Trajectory([[x_0, y_0, 0]], 0, fig, classes) #Trajectory Type I
    t2 = Trajectory(t1, 1, fig, classes) #Trajectories Type II
    Trajectory(t2, 2, fig, classes) #Trajectories Type III
    return fig, classes

if __name__ == "__main__":
    fig, classes = graphGenerator(-5, -5)
    fig.show()
    print(classes)