class MonkSudoku:
    def __init__(self):
        self.n = 16
        self.initial_state = self.random_state()

    def random_state(self):
        import random
        state= []
        for i in range(self.n):
            state.append(random.randint(1,4))
        return state

    def actions(self,state):
        valid_actions = []

        for i in range(self.n):
            for j in range(4):
                if state[i] != j+1:
                    valid_actions.append((i, j+1)) #azione = nella casella i scrivi j+1

        return valid_actions

    def result(self,state,action):
        i, j = action
        new_state= list(state)
        new_state[i] = j
        return new_state

    def print_state(self,state):
        for i in range(0, self.n ,4):
            print("----------------------")
            print(f"| {state[i]}  | {state[i+1]}  |  {state[i+2]}  |  {state[i+3]}  |")

    def conflicts(self,state):
        conflicts = 0
        for i in range(0, self.n, 4):
            row = [state[i], state[i+1], state[i+2], state[i+3]]
            for j in range(4):
                for k in range(j+1,4):
                    if row[j] == row[k]:
                        conflicts += 1

        for i in range (0, 4):
            col = [state[i],state[i+4],state[i+8],state[i+12]]
            for j in range(4):
                for k in range(j+1,4):
                    if col[j] == col[k]:
                        conflicts += 1

        blocks= [[0,1,4,5],
                [2,3,6,7],
                [8,9,12,13],
                 [10,11,14,15]]

        for i in range(0, 4):
            square = [state[l] for l in blocks[i]]
            for j in range(4):
                for k in range (j+1,4):
                    if square[j] == square[k]:
                        conflicts += 1

        return conflicts

    def evaluate(self,state):
        return -self.conflicts(state)
