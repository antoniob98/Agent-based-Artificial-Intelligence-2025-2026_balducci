#armenise
class BananaPartitioningProblem:
    def __init__(self, n):
        self.n = n
        self.initial_state = self.random_state()

    def random_state(self):
        import random
        state = []
        for i in range(self.n):
            state.append(random.randint(0,1))
        return state

    def actions(self,state):
        valid_actions = []
        for i in range(self.n):
            valid_actions.append(i)
        return valid_actions

    def actions_filtered(self,state):
        count_0 = state.count(0)
        count_1 = state.count(1)

        if count_0 < count_1:
            valid_actions = [i for i in range(self.n) if state[i] == 1]
        elif count_0 > count_1:
            valid_actions = [i for i in range(self.n) if state[i] == 0]
        else:
            valid_actions = []
        return valid_actions


    def result(self,state,action):
        new_state = list(state)
        new_state[action] = 1- new_state[action]
        return new_state

    def print_state(self, state):
        for i in range(self.n):
            print (state[i])


    def conflicts(self,state):
        return abs(state.count(0) - state.count(1))

    def evaluate(self,state):
        return -self.conflicts(state)
