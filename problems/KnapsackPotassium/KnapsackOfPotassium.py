import random

bananas = [{"weight": 2, "potassium": 3},
           {"weight": 2, "potassium": 3},
           {"weight": 3, "potassium": 4},
           {"weight": 3, "potassium": 4},
           {"weight": 4, "potassium": 5},
           {"weight": 5, "potassium": 8}]
#stato è tupla con 1 se c'è la banana, 0 altrimenti
#azione è il numero della banana che devo togliere o mettere. quindi da ogni stato ho sempre lo stesso set di azioni possibili
class KnapsackOfPotassium:

    def __init__(self, capacity):
        self.bananas = bananas
        self.capacity = capacity
        self.initial_state = self.random_state()

    def random_state(self):
        return tuple(random.randint(0,1) for _ in range(len(self.bananas)))

    def actions(self, state):
        actions = []
        for banana in range(len(self.bananas)):
            actions.append(banana)
        return actions

    def result(self, state, action):
        new_state = list(state)
        banana = action
        if state[banana] == 1:
            new_state[banana] = 0 # se c'è la tolgo
        else:
            new_state[banana] = 1 # altrimenti la metto
        return new_state

    def actual_weight(self, state):
        total_weight = 0
        for banana in range(len(self.bananas)):
            if state[banana] == 1:
                total_weight += self.bananas[banana]["weight"]
        diff = self.capacity - total_weight  # negativo se sto superando la capacità
        return total_weight, diff

    def actual_potassium(self, state):
        potassium = 0
        for banana in range(len(self.bananas)):
            if state[banana] == 1:
                potassium += self.bananas[banana]["potassium"]
        return potassium

    def evaluate(self, state):
        total_weight, diff = self.actual_weight(state)
        potassium = self.actual_potassium(state)
        if diff < 0: # penalizzo il valore se sto superando la capacità
            return potassium - 100 * abs(diff)
        else:
            return potassium

