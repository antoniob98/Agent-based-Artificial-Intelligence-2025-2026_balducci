import random
import math

class SimulatedAnnealing():
    def __init__(self, problem, schedule):
        self.problem = problem
        self.schedule = schedule

    def search(self):
        current = self.problem.initial_state
        for t in range(1, 1000000):  # Arbitrary large number of iterations
            T = self.schedule(t)
            if T < 0.00001:  # Temperature is close to zero, stop the search
                return current
            neighbors = self.problem.actions(current)
            if not neighbors:
                return current
            action = random.choice(neighbors)
            next_state = self.problem.result(current, action)
            # maximization problem: we want to maximize the evaluation function
            delta_e = self.problem.evaluate(next_state) - self.problem.evaluate(current)
            select_probability = math.exp(delta_e / T)
            print(f"Iteration {t}, Temperature: {T:.4f}, Action: {action}, ΔE: {delta_e:.4f}, Select Probability: {select_probability:.4f}")
            if delta_e > 0 or random.random() < select_probability:
                current = next_state
        return current

def exponential_schedule(t, alpha=0.001):
    return 100 * math.exp(-alpha * t)

def linear_schedule(t, alpha=0.001):
    return max(0, 100 - alpha * t)

if __name__ == "__main__":
    from problems.ChessQueens.chessQueens import ChessQueensProblem

    problem = ChessQueensProblem(8)
    search = SimulatedAnnealing(problem, linear_schedule)
    result = search.search()

    print(result)
    print(problem.evaluate(result))
    print(problem.is_goal(result))
    print(problem.conflicts(result))
    problem.print_state(result)
