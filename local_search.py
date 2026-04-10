class HillClimbing():

    def __init__(self, problem):
        self.problem = problem
    
    def get_neighbors(self, state):
        return [self.problem.result(state, action) for action in self.problem.actions(state)]

    def search(self):
        
        state = self.problem.initial_state

        # Hill Climbing
        while True:
            neighbors = self.get_neighbors(state)
            if not neighbors:
                break
            
            best_neighbor = max(neighbors, key=lambda x: self.problem.evaluate(x))
            if self.problem.evaluate(best_neighbor) <= self.problem.evaluate(state):
                break
            
            state = best_neighbor

        return state

