from Core import uniform_cost_search, report, PourProblem, breadth_first_search, GreenPourProblem, iterative_deepening_search, astar_search, RouteProblem, Map, EightPuzzle
from Core import breadth_first_bfs, depth_limited_search, greedy_bfs
import plot as plot

if __name__ == '__main__':
    romania = Map(
    {('O', 'Z'):  71, ('O', 'S'): 151, ('A', 'Z'): 75, ('A', 'S'): 140, ('A', 'T'): 118, 
     ('L', 'T'): 111, ('L', 'M'):  70, ('D', 'M'): 75, ('C', 'D'): 120, ('C', 'R'): 146, 
     ('C', 'P'): 138, ('R', 'S'):  80, ('F', 'S'): 99, ('B', 'F'): 211, ('B', 'P'): 101, 
     ('B', 'G'):  90, ('B', 'U'):  85, ('H', 'U'): 98, ('E', 'H'):  86, ('U', 'V'): 142, 
     ('I', 'V'):  92, ('I', 'N'):  87, ('P', 'R'): 97},
    {'A': ( 76, 497), 'B': (400, 327), 'C': (246, 285), 'D': (160, 296), 'E': (558, 294), 
     'F': (285, 460), 'G': (368, 257), 'H': (548, 355), 'I': (488, 535), 'L': (162, 379),
     'M': (160, 343), 'N': (407, 561), 'O': (117, 580), 'P': (311, 372), 'R': (227, 412),
     'S': (187, 463), 'T': ( 83, 414), 'U': (471, 363), 'V': (535, 473), 'Z': (92, 539)})


    r0 = RouteProblem('A', 'A', map=romania)
    r1 = RouteProblem('A', 'B', map=romania)
    r2 = RouteProblem('N', 'L', map=romania)
    r3 = RouteProblem('E', 'T', map=romania)
    r4 = RouteProblem('O', 'M', map=romania)


    p1 = PourProblem((1, 1, 1), 13, sizes=(2, 16, 32))
    p2 = PourProblem((0, 0, 0), 21, sizes=(8, 11, 31))
    p3 = PourProblem((0, 0),     8, sizes=(7,9))
    p4 = PourProblem((0, 0, 0), 21, sizes=(8, 11, 31))
    p5 = PourProblem((0, 0),     4, sizes=(3, 5))

    g1 = GreenPourProblem((1, 1, 1), 13, sizes=(2, 16, 32))
    g2 = GreenPourProblem((0, 0, 0), 21, sizes=(8, 11, 31))
    g3 = GreenPourProblem((0, 0),     8, sizes=(7,9))
    g4 = GreenPourProblem((0, 0, 0), 21, sizes=(8, 11, 31))
    g5 = GreenPourProblem((0, 0),     4, sizes=(3, 5))

    e1 = EightPuzzle((1, 4, 2, 0, 7, 5, 3, 6, 8))
    e2 = EightPuzzle((1, 2, 3, 4, 5, 6, 7, 8, 0))
    e3 = EightPuzzle((4, 0, 2, 5, 1, 3, 7, 8, 6))
    e4 = EightPuzzle((7, 2, 4, 5, 0, 6, 8, 3, 1))
    e5 = EightPuzzle((8, 6, 7, 2, 5, 4, 3, 0, 1))

    problem = [p1,p2,p3,p4,g1,g2,g3,g4,r0,r1,r2,r3,r4,e1]
    


    
    plot.reporti([uniform_cost_search, breadth_first_search,astar_search, iterative_deepening_search, breadth_first_bfs, depth_limited_search, greedy_bfs], problem)
    
