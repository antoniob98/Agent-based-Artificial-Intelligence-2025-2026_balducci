import random

OBSTACLE = "obstacle"
FREE = "free"

FREE_PROBABILITY = 0.9

# state is a tuple (x, y) representing the robot's position on the grid
# action is a string representing the move direction: "up", "down", "left", "right"


class Grid:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.possible_actions = ["up", "down", "left", "right"]

    def environment_construction(self, initial_state, goal_state):
        is_x, is_y = initial_state
        gs_x, gs_y = goal_state

        self.grid = {}

        for row in range(self.rows):
            for column in range(self.columns):
                if random.random() < FREE_PROBABILITY:
                    self.grid[row, column] = FREE
                else:
                    self.grid[row, column] = OBSTACLE
        # Ensure initial and goal states are free
        self.grid[(is_x, is_y)] = FREE
        self.grid[(gs_x, gs_y)] = FREE


        # Print environment
        for row in range(self.rows):
            for column in range(self.columns):
                print(f"{self.grid[row, column]:<10}", end="")
            print()

        return self


class RobotNavigationProblem:
    def __init__(self, initial_state, goal_state, rows, columns):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.map = Grid(rows, columns).environment_construction(initial_state, goal_state)

    def actions(self, state):
        possible_actions = []

        for action in self.map.possible_actions:
            # Compute next position
            new_x, new_y = self.result(state, action)

            # Check boundaries and obstacles
            if (
                0 <= new_x < self.map.rows
                and 0 <= new_y < self.map.columns
                and self.map.grid[(new_x, new_y)] == FREE
            ):
                possible_actions.append(action)

        return possible_actions

    def result(self, state, action):
        x, y = state

        moves = {
            "up": (-1, 0),
            "down": (1, 0),
            "left": (0, -1),
            "right": (0, 1),
        }

        dx, dy = moves[action]
        new_x = x + dx
        new_y = y + dy

        return (new_x, new_y)

    def action_cost(self, state, action):
        return 1

    def is_goal(self, state):
        return state == self.goal_state


    def mahattan_distance(self, state):
        x, y = state
        gs_x, gs_y = self.goal_state
        return abs(x - gs_x) + abs(y - gs_y)
    
    def euclidean_distance(self, state):
        x, y = state
        gs_x, gs_y = self.goal_state
        return ((x - gs_x) ** 2 + (y - gs_y) ** 2) ** 0.5