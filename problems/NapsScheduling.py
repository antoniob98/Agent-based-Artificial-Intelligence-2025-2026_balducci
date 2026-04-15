naps = ["Nap1", "Nap2", "Nap3", "Nap4"]

conflicts = {
    ("Nap1", "Nap2"),
    ("Nap1", "Nap3"),
    ("Nap2", "Nap4"),
}

num_trees = 2

import random

class NapsScheduling:
    def __init__(self):
        self.num_trees = num_trees
        self.conflicts = conflicts
        self.naps = naps
        self.initial_state = self.random_state()

    def random_state(self):
        return {nap: random.randint(1, self.num_trees) for nap in self.naps}

    def actions(self, state):
        actions = []
        for nap in self.naps:
            tree1 = state[nap]
            for tree2 in range(1, self.num_trees + 1):
                if tree1 != tree2:
                    actions.append((nap, tree2))
        return actions

    def decode_action(self, action):
        nap = action[0]
        tree = action[1]
        return nap, tree

    def result(self, state, action):
        nap, tree = self.decode_action(action)
        state[nap] = tree
        return state

    def get_conflicts(self, state):
        n_conflicts = 0
        for (nap1, nap2) in self.conflicts:
            if state[nap1] == state[nap2]:
                n_conflicts += 1
        return n_conflicts

    def evaluate(self, state):
        penalty = 0
        for tree in range(1, self.num_trees + 1):
            if tree not in state.values():
                penalty += 10
        return - self.get_conflicts(state) - penalty



