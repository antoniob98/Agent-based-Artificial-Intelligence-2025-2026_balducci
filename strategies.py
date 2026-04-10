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
    
