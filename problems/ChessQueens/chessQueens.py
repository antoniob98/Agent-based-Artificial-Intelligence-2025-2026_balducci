# State representation: a tuple of length n, where the i-th element represents the column position of the queen in the i-th row.
# Example: For n=4, the state (1, 3, 0, 2) means that the queen in the first row is in column 1, the queen in the second row is in column 3, the queen in the third row is in column 0, and the queen in the fourth row is in column 2.

class ChessQueensProblem:
    def __init__(self, n):
        self.n = n
        self.initial_state = self.random_state()

    def random_state(self):
        import random
        return tuple(random.randint(0, self.n - 1) for _ in range(self.n))

    def actions(self, state):
        actions = []
        for col in range(self.n):
            row = state[col]
            free_rows = [r for r in range(self.n) if r != row]
            actions.extend([(col, r) for r in free_rows])
        return actions

    def result(self, state, action):
        col, row = action
        new_state = list(state)
        new_state[col] = row
        return tuple(new_state)

    def is_goal(self, state):
        return self.conflicts(state) == 0
    
    def print_state(self, state):
        for row in range(self.n):
            line = ""
            for col in range(self.n):
                if state[col] == row:
                    line += "Q "
                else:
                    line += ". "
            print(line)
        print()

    def conflicts(self, state):
        conflicts = 0
        for col in range(self.n):
            row = state[col]
            for col2 in range(col + 1, self.n):
                row2 = state[col2]
                if row == row2 or abs(row2 - row) == abs(col2 - col):
                    conflicts += 1
        return conflicts
    
    def evaluate(self, state):
        return -self.conflicts(state)

if __name__ == "__main__":
    chess_queens_problem = ChessQueensProblem(8)
    print("Initial state:")
    chess_queens_problem.print_state(chess_queens_problem.initial_state)
    print("Number of conflicts:", chess_queens_problem.conflicts(chess_queens_problem.initial_state))
    chess_queens_problem.is_goal(chess_queens_problem.initial_state)