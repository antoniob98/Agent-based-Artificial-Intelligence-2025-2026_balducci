import random


OSTACOLO = "ostacolo"
LIBERO = "libero"

class Griglia:
    def __init__(self, righe, colonne):
        self.righe = righe
        self.colonne = colonne

    def ambientConstruction(self, initial_state, goal_state):
        initial_x = initial_state.x
        initial_y = initial_state.y
        goal_x = goal_state.x
        goal_y = goal_state.y
        self.griglia = {}
        for riga in range(self.righe):
            for colonna in range(self.colonne):
                self.griglia[riga, colonna] = LIBERO if (random.random() > 0.1 or (riga == goal_x and colonna == goal_y) or (riga == initial_x and colonna == initial_y) ) else OSTACOLO
        #Print ambiente
        for riga in range(self.righe):
            for colonna in range(self.colonne):
                print(f"{self.griglia[riga, colonna]:<10}", end="")
            print()
        return self
    
    
class Position:
    def __init__(self, x, y, parent, action_cost=0):
        self.x = x
        self.y = y
        self.parent = parent
        self.action_cost = action_cost

    def path(self):
        path = []
        current = self
        while current is not None:
            path.append((current.x, current.y))
            current = current.parent
        return path
    


class RobotNavigationProblem:
    def __init__(self, initial_state, goal_state, righe, colonne):
        self.initial_state = initial_state
        self.goal_state = goal_state

        self.map = Griglia(righe, colonne).ambientConstruction(initial_state, goal_state)

    def actions(self, state):
        x = state.x
        y = state.y
        possible_actions = []

        moves = [
            ("up",-1, 0),
            ("down",1, 0),
            ("left",0, -1),
            ("right",0, 1)
        ]

        for action_name, dx, dy in moves:
            # new_x = x + dx
            # new_y = y + dy
            new_x, new_y = self.result(state, action_name)

            if (0 <= new_x < self.map.righe and 
                0 <= new_y < self.map.colonne and 
                self.map.griglia[(new_x, new_y)] == LIBERO):
                possible_actions.append(action_name)
        return possible_actions

    def result(self, state, action):
        x = state.x
        y = state.y

        moves = {
            "up": (-1, 0),
            "down": (1, 0),
            "left": (0, -1),
            "right": (0, 1)
        }
        
        dx, dy = moves[action]
        new_x = x + dx
        new_y = y + dy
        
        return Position
        return (new_x, new_y)
    
    def action_cost(self, state, action):
        return 1
    
    def is_goal(self, state):
        return state == self.goal_state