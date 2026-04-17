import random

class RandomStrategy:
    def select(self, fringe):
        random.shuffle(fringe)
        selected_node = fringe.pop(0)
        return fringe, selected_node
    
class UniformCostStrategy:
    def select(self, fringe):
        fringe.sort(key=lambda node: node.path_cost)
        selected_node = fringe.pop(0)
        return fringe, selected_node
    
class BreadthFirstStrategy:
    def select(self, fringe):
        fringe.sort(key=lambda node: node.depth)
        selected_node = fringe.pop(0)
        return fringe, selected_node
    
class BreadthFirstArmeniseStrategy:
    def select(self, fringe):
        return fringe, fringe.pop(0)
    
class DepthFirstStrategy:
    def select(self, fringe):
        fringe.sort(key=lambda node: node.depth)
        selected_node = fringe.pop()
        return fringe, selected_node
    
class DepthFirstArmeniseStrategy:
    def select(self, fringe):
        return fringe, fringe.pop()

class DepthLimitedStrategy:
    def __init__(self, limit) -> None:
        self.limit = limit
    
    def select(self, fringe):
        new_fringe = [n for n in fringe if n.depth <= self.limit]
        # new_fringe = []
        # for n in fringe:
        #     if n.depth <= self.limit:
        #         new_fringe.append(n)
        return new_fringe, new_fringe.pop()
    
class GreedStrategy:

    def __init__(self, problem) -> None:
        self.problem = problem

    def select(self, fringe):
        fringe.sort(key=lambda node: self.problem.heuristic(node.state))
        return fringe, fringe.pop(0)

class AStarStrategy:

    def __init__(self, problem) -> None:
        self.problem = problem

    def select(self, fringe):
        fringe.sort(key=lambda node: self.problem.heuristic(node.state) + node.path_cost)
        return fringe, fringe.pop(0)

class ExamDepthLimitedStrategy:
    def select(self, fringe):
        fringe = [node for node in fringe if node.depth <= 10]
        selected_node = fringe.pop()
        return fringe, selected_node
    
class ExamAStar:
    def __init__(self, problem):
        self.problem = problem

    def select(self, fringe):
        fringe = sorted(fringe, key= lambda x: x.path_cost + self.problem.heuristic(x.state))
        selected_node = fringe.pop(0)
        return fringe, selected_node