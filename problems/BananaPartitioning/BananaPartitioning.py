import random

#stato esempio: (1,1,0,0): le prime 2 banane assegnate a M1 e le altre ad M2
#azione esempio: (3): dai la banana 3 all'altra scimmia

class BananaPartitioning:

    def __init__(self, n_bananas):
        self.n_bananas = n_bananas
        self.initial_state = self.random_state()

    def random_state(self):
        return tuple(random.randint(0, 1) for _ in range(self.n_bananas))

    def actions(self, state):
        actions = []
        for banana in range(self.n_bananas):
            actions.append(banana)
        return actions

    def result(self, state, action):
        new_state = list(state)
        banana = action
        if state[banana] == 0:
            new_state[banana] = 1
        else:
            new_state[banana] = 0
        return tuple(new_state)

    def get_difference(self, state):
        n_first_monkey = 0
        n_second_monkey = 0
        for banana in range(self.n_bananas):
            if state[banana] == 0:
                n_first_monkey += 1
            else:
                n_second_monkey += 1
        return abs(n_first_monkey - n_second_monkey)

    def evaluate(self, state):
        return - self.get_difference(state)