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

if __name__ == "__main__":

    pprint(m_g(3, 6))
    print("")
    #pprint(grap_generate( m_g(3,6),20))

