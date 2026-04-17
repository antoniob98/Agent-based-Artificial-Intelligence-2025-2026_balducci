#armenise
class FeatureSelection:
    def __init__(self):
        self.penalty = 2
        self.feat_names = ["Color", "Size", "Ripness", "Texture", "Sweetness"]
        self.features = [5, 3, 8, 2 ,6] # [color, size, ripeness, texture, sweetness]
        self.initial_state = self.random_state()

    def random_state(self):
        import random
        state = []
        for i in range(len(self.features)):
            state.append(random.randint(0,1))
        return state

    def actions(self,state):
        valid_actions = []
        for i in range(len(self.features)):
            valid_actions.append(i)
        return valid_actions

    def result(self,state, action):
        new_state = list(state)
        new_state[action]= 1 - new_state[action]
        return new_state

    def print_state(self,state):
        print("Sono state selezionate le seguenti feature:")
        for i in range(len(self.features)):
            if state[i] == 1:
                print(f"{self.feat_names[i]} : {self.features[i]}")

    def conflicts(self,state):
        total_relevance = 0
        count = 0
        for i in range(len(state)):
            if state[i]==1:
                total_relevance += self.features[i]
                count += 1
        total_penalty= self.penalty * count
        return total_relevance - total_penalty

    def evaluate(self,state):
        return self.conflicts(state)

