from local_search import HillClimbing

if __name__ == "__main__":
    from problems.ChessQueens.chessQueens import ChessQueensProblem

    problem = ChessQueensProblem(8)
    search = HillClimbing(problem)
    result = search.search()

    print(result)
    print(problem.evaluate(result))
    print(problem.is_goal(result))
    problem.print_state(result)
