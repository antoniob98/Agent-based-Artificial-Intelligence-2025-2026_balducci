class SchedulingNaps:
    def __init__(self,n_trees):
        self.n_trees = n_trees
        self.naps = ["Nap1","Nap2","Nap3","Nap4","Nap5"]
        self.incompatibilities =[("Nap1","Nap2"),("Nap1","Nap3"),("Nap2","Nap4"),("Nap4","Nap5")]
        self.initial_state = self.random_state()
        #state = [0, 0, 1, 2, 2]
    def random_state(self):
        import random
        state = []
        for i in range(len(self.naps)):
            state.append(random.randint(0,(self.n_trees - 1)))
        return state

    def actions(self,state):
        valid_actions = []
        #indice_nap, tree = action

        for i in range(len(self.naps)):
            for j in range(self.n_trees):
                if j != state[i]:
                    valid_actions.append((i, j))
        return valid_actions

    def result(self,state,action):
        new_state= list(state)
        i,j = action
        new_state[i] = j
        return new_state

    def print_state(self,state):
        for i in range(len(state)):
            print(f"{self.naps[i]} on Tree {state[i]}")

    def conflicts(self,state):
        conflicts = 0
        for i in range(len(self.incompatibilities)):
            a, b = self.incompatibilities[i]
            index_a = self.naps.index(a)
            index_b = self.naps.index(b)
            if state[index_a] == state[index_b]:
                conflicts += 1
        return conflicts

    def evaluate(self,state):
        return -self.conflicts(state)