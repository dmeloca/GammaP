from pprint import pprint
import plotly.graph_objects as go

TYPE = ["Type I", "Type II", "Type III"]
COLORS = ["red", "green", "blue"]

def trajectory(points:list[list], t:int, fig:go.Figure, classes:list) -> list[list]:
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
            if(x[-1] + y[-1] >= 0 and x[-1] + y[-1] <= 28):
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
    
def graphGenerator(x_0:int, y_0:int, fig:go.Figure) -> list[int]:
    '''
    Returns the graph of the trajectories of type I, II and III
    and a list where the i-th position stores the number of trajectories
    that cross the points of the class 'i' (points such as the sum of its
    coordinates (x,y) is 'i'. x+y=i)
    '''
    classes = [0 for i in range(29)]
    t1 = trajectory([[x_0, y_0, 0]], 0, fig, classes) #Trajectory Type I
    t2 = trajectory(t1, 1, fig, classes) #Trajectories Type II
    trajectory(t2, 2, fig, classes) #Trajectories Type III
    return classes

def alphabets(x_0:int, y_0:int, permutation:str) -> tuple[go.Figure, list[list]]:
    '''
    Returns the figure and the matrix of permuted alphabets
    '''
    fig = go.Figure()
    p = [ord(i)-48 for i in permutation]
    #fig.update_yaxes(scaleanchor = 'x', scaleratio = 1) #Same scale for x and y axes
    #fig.update_yaxes(automargin= "height"  )
    fig.update_yaxes(autotypenumbers="strict")
    #matrix with 10 columns of alphabets with a shift
    alphabets = [[chr(((i+j) % 26) + 97) for i in range(20)] for j in range(10)]
    #permutation of the columns of the previous matrix
    k = [alphabets[p[i]] for i in range(10)]
    #number of trajectories thar cross points of each class
    classes = graphGenerator(x_0, y_0, fig)
    #adds the number of trajectories to every position in the matrix
    for i in range(10):
        for j in range(20):
            k[i][j] = chr((ord(k[i][j]) - 97 + classes[i+j]) % 26 + 97)
    #draws a column at every iteration
    for c in range(10):
        fig.add_trace(
            go.Scatter(
                x = [c]*20,
                y = list(range(20)),
                mode = "markers+text",
                text = k[c],
                textposition = "middle center",
                marker = dict(color='white'),
                showlegend = False,
            )
        )
    return fig, k

from string import ascii_lowercase

# char to int
char2int = {x: idx for idx, x in enumerate(ascii_lowercase)}
# int to char
int2char = {idx: x for idx, x in enumerate(ascii_lowercase)}

def encrypt_gammaP(plain_text:str, k:list[list]) -> str:
    plain_text = plain_text.replace(" ", "").lower()
    return "".join([int2char[(char2int[i] + k) % 26] for i in plain_text]).upper()

def decrypt_gammaP(cipher_text:str, k:list[list]) -> str:
    cipher_text = cipher_text.replace(" ", "").lower()
    return "".join([int2char[(char2int[i] - k) % 26] for i in cipher_text])


if __name__ == "__main__":
    fig, k = alphabets(-5, -1, '0235814697')
    fig.show()
    print(k)