#armenise: i vincoli impediscono completamente la possibilità di superare la capacità max sempre
class KnapsackOfPotassium:
    def __init__(self,capacity):
        self.capacity = capacity
        self.bananas = [(2,3),(2,3),(3,4),(3,4),(4,5),(5,8)]
        self.initial_state = self.random_state()

    def random_state(self):
        import random
        state = []
        count = 0
        for i in range(len(self.bananas)):
            if count + self.bananas[i][0] <= self.capacity:
                state.append(random.randint(0,1))
                if state[i] == 1:
                    count = count + self.bananas[i][0]
            else:
                state.append(0)
        return state

    def actions(self, state):
        valid_actions = []
        state_count = 0
        for i in range(len(state)):
            if state[i] == 1:
                state_count += self.bananas[i][0]

        for i in range(len(state)):
            if state[i] == 0:
                if state_count + self.bananas[i][0] <= self.capacity:
                    valid_actions.append(i)
            elif state[i] == 1:
                valid_actions.append(i)
        return valid_actions

    def result(self,state, action):
        new_state = list(state)
        new_state[action] = 1 - state[action]
        return new_state

    def print_state(self,state):
        for i in range(len(state)):
            print(state[i])

    def conflicts(self,state):
        total_potassium = 0
        for i in range(len(self.bananas)):
            total_potassium += self.bananas[i][1]

        state_potassium = 0
        for i in range(len(state)):
            if state[i] == 1:
                state_potassium += self.bananas[i][1]

        return total_potassium - state_potassium

    def evaluate(self,state):
        return -self.conflicts(state)

