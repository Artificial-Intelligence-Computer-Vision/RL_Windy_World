from header_import import *

class sarsa_algorithm(Windy_World):
    def __init__(self, episode, gamma, alpha, epsilon, max_time_step, action_type, wind_type):
        super().__init__(action_type, wind_type)
        
        self.alpha = alpha
        self.epsilon = epsilon
        self.gamma = gamma
        self.epsilon = epsilon
        self.number_episode = episode
        self.action_type = action_type
        self.max_time_step = max_time_step
        self.q_value = defaultdict(float)
        
        self.time_step = []
        
        
    def argmax_rand(self, max_act):
        return np.random.choice(np.flatnonzero(max_act == np.max(max_act)))
    
    def policy(self, state):
        if np.random.rand() > self.epsilon:
            return self.argmax_rand([self.q_value[state, a] for a in self.action_space])
        else:
            return np.random.choice(self.action_space)
    
    def sarsa(self):
        
        for i in range(self.number_episode):
            state = self.reset()
            action = self.policy(state)
            
            while True:
                done, reward, next_state = self.step(action)
                next_action = self.policy(next_state)
                self.q_value[state, action] = self.q_value[state, action] + self.alpha * (reward + self.gamma * self.q_value[next_state, next_action] - self.q_value[state, action])
                state, action = next_state, next_action
                self.time_step.append(i)
                if len(self.time_step) >= self.max_time_step:
                    return self.time_step
                    
                if done:
                    break
                    
        return self.time_step
                    
    
    def plot_episode_time_step(self):
        
        fig = plt.figure()
        axis = fig.add_subplot(111)
        axis.plot(self.time_step, color='blue')
        axis.set_title(self.action_type +" Episode vs Time Step")
        axis.set_xlabel("Time Steps")
        axis.set_ylabel("Episodes")
        plt.show()


        
