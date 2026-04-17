from problems.forestProblem.forest_problem import ForestProblem
from path_search.search import Search
from path_search.strategies import ExamDepthLimitedStrategy, ExamAStar, RandomStrategy

problem = ForestProblem()

strategy = ExamDepthLimitedStrategy()
search = Search(problem=problem, strategy=strategy)
result = search.run()

if result is None:
    print('No solution found')
else:    
    print(f'Solution found with path cost {result.path_cost}')

    path = []
    for _ in range(result.depth):
        path.append(result.action)
        result = result.parent
    path = path[::-1]
    print(path)

    state = problem.initial_state
    print(f'Initial state: {state}')
    for action in path[:2]:
        state = problem.result(state, action)
        print(state)

    print(f'Third state: {state}')


strategy = ExamAStar(problem=problem)
search = Search(problem=problem, strategy=strategy)
result = search.run()
if result is None:
    print('No solution found')
else:    
    print(f'Solution found with path cost {result.path_cost}')

    path = []
    for _ in range(result.depth):
        path.append(result.action)
        result = result.parent
    path = path[::-1]
    print(path)

    state = problem.initial_state
    print(f'Initial state: {state}')
    for action in path[:2]:
        state = problem.result(state, action)
        print(state)

    print(f'Third state: {state}')