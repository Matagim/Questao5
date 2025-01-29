from Core import uniform_cost_search, report, PourProblem, breadth_first_search, GreenPourProblem, iterative_deepening_search, astar_search
import plot as plot

if __name__ == '__main__':
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
    problem = [p1]
    problem1 = [g1]
    report([uniform_cost_search, breadth_first_search, astar_search, iterative_deepening_search], problem)
    plot.reporti([uniform_cost_search, breadth_first_search,astar_search, iterative_deepening_search], problem)
    plot.reporti([uniform_cost_search, breadth_first_search,astar_search, iterative_deepening_search], problem1)
