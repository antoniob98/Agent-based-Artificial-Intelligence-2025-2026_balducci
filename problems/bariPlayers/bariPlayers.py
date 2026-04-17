import random
from problems.bariPlayers.players import players


players_names = list(players.keys())

PENALTY = 100

class BariPlayersProblem:
    def __init__(self):
        self.initial_state = self.random_state()

    def random_state(self):
        import random
        random_state = []
        for _ in range(11):
            random_state.append(random.choice(players_names))
        return tuple(random_state)

    # def actions_(self, state):
    #     # action: remove player1 insert player 2
    #     actions = []
    #     players_in_state = list(state)
    #     for _ in range(20):
    #         # player to remove
    #         p1 = random.choice(players_in_state)
    #         # player to insert
    #         done = False
    #         while not done:
    #             p2 = random.choice(players_names)
    #             if p2 not in players_in_state:
    #                 done = True
    #         actions.append((p1, p2))
    #     return actions

    def actions(self, state):
        # action: remove player1 insert player 2
        actions = []
        players_in_state = list(state)
        players_values = self.team_value(state)
        players_prob = {p: players[p]['valore'] / players_values for p in state}
        
        while len(actions) != 20:
            # player to remove
            prob = random.random()
            for p in players_in_state:
                if players_prob[p] < prob:
                    p1 = p
                    break
                else:                    
                    p1 = random.choice(players_in_state)
            # player to insert
            done = False
            while not done:
                p2 = random.choice(players_names)
                if p2 not in players_in_state:
                    done = True
            actions.append((p1, p2))
        return actions


    def result(self, state, action):
        state = list(state)
        p1, p2 = action
        state.remove(p1)
        state.append(p2)
        return tuple(state)

    def count_role(self, state, role):
        count = 0
        for p in state:
            if players[p]['ruolo'] == role:
                count += 1
        return count
    
    def team_value(self, state):
        value = 0
        for p in state:
            value += players[p]['valore']
        return value

    def evaluate(self, state):
        value = 0
        for p in state:
            value += players[p]['valore']
        
        if self.count_role(state, 'Portiere') == 0:
            value -= PENALTY
        if self.count_role(state, 'Difensore') < 3:
            value -= PENALTY
        if self.count_role(state, 'Centrocampista') < 2:
            value -= PENALTY
        if self.count_role(state, 'Attaccante') == 0:
            value -= PENALTY

        return value
