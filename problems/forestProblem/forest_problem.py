
class ForestProblem:

    def __init__(self, initial_state=None, goal_state=None):

        # I need to define the initial state
        self.initial_state = (4, 0, 0)
        self.goal_state = (0, 4, 1)

    def actions(self, state):
        # I can move only monkeys with a torch
        actions = []
        torch_position = state[2]
        available_monkeys = state[torch_position]
        # move one monkey
        if available_monkeys > 0:
            actions.append([1, torch_position])
        # move two monkeys
        if available_monkeys > 1:
            actions.append([2, torch_position])
        return actions

    def result(self, state, action):
        monkeys = action[0]
        torch_position = action[1]
        new_state = list(state)
        # move monkeys from left to right
        if torch_position == 0:
            new_state[0] -= monkeys
            new_state[1] += monkeys
            new_state[2] = 1
        elif torch_position == 1:
            new_state[1] -= monkeys
            new_state[0] += monkeys
            new_state[2] = 0
        else:
            raise ValueError('Wrong torch value')
        if new_state[0] < 0 or new_state[0] > 4:
            raise ValueError(f'Wrong state: {new_state}')
        if new_state[1] < 0 or new_state[1] > 4:
            raise ValueError(f'Wrong state: {new_state}')
        return tuple(new_state)


    def action_cost(self, state, action):
        return 1
    
    def is_goal(self, state):
        return state == self.goal_state
    
    def heuristic(self, state):
        return round(state[0]/2)
