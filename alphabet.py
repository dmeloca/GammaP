import plotly.graph_objects as go

def alphabet_plane(text:list[str]):

    fig = go.Figure()
    fig.add_trace(go.Scatter(

    x=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9,   #0, x axis 0-9
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9,  #1
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9], #9
        

    y = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,     #0, y axis 0-9
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1,  
            2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 
            3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 
            4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 
            5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
            6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 
            7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 
            8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 
            9, 9, 9, 9, 9, 9, 9, 9, 9, 9],#9
    
    mode="markers+text",
    text= text,
    textposition="bottom center"))
    fig.show()


def permutation_columns(p: str, matrix: list[str]) -> list[str]:
    """
    Column permutation, enter a permutation of the form "1235.. " and the matrix to be permuted
    """
    m_c= list(matrix) #copy
    selector = len(p) #jump to the other element in the column so that x iterates over it
    for i in range(len(p)): #choose the column
        for x in range(len(p)): #iterate through the elements of the column
            m_c[int(p[i])+selector*x]= matrix[int(p[(i+1)%len(p)])+selector*x] #change
    return m_c        

"""
int(p[i]) := elige la columna
se

m_c[int(p[i])+column*x]= matrix[int(p[(i+1)%len(p)])+column*x]


['a','b','c',
'b', 'c','d',
'c','d','e']

['b', 'c', 'a', 
'c', 'd', 'b', 
'd', 'e', 'c']
"""
        





if __name__ == "__main__":
    
    """
    #small case
    p = "012"
    text=['a','b','c',
            'b', 'c','d',
            'c','d','e']
    """
    

    
    text=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',  #0
        'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',  #1
        'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',  
        'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',  
        'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',  
        'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',  
        'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',  
        'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',  
        'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',  
        'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's']#9 
    
    p="0246813579"

    text = permutation_columns(p,text)
    #print(text)
    alphabet_plane(text)

