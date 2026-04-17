from local_search.hill_climbing import HillClimbing
from problems.bariPlayers.bariPlayers import BariPlayersProblem

if __name__ == "__main__":

    teams = []
    for _ in range(20):
        problem = BariPlayersProblem()
        search = HillClimbing(problem)
        result = search.search()
        teams.append((result, problem.evaluate(result)))
    
    teams = sorted(teams, key=lambda x: float(x[1]))
    for team, value in teams:
        print(f'Value: {value}')
