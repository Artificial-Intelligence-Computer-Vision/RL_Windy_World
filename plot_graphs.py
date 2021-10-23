from header_import import *

class plot_graphs():
    def __init__(self):
        self.path = "graphs_charts/"

        self.chart_path = self.path + "charts/"
        self.enviroment = self.path + "enviroment/"



    def action_path(self, q_value):
        x, y = self.start
        path = [self.start]
        for _ in range(100):
            best_action = np.argmax([q_value[(x,y), a] for a in self.action_space])
            x, y = self.transition(x, y, best_action)
            path.append((x,y))
            if x == self.goal[0] and y == self.goal[1]:
                break
                
        return path



    def plot_windy(self, q_value):
        
        action_path = self.action_path(q_value)
        fig = plt.figure()
        axis = fig.add_subplot(111)
        axis.set_xlim(-0.5, 9.5)
        axis.set_ylim(-0.5, 6.5)
        axis.set_yticks([])
        axis.set_xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        axis.set_xticklabels([0, 0, 0, 1, 1, 1, 2, 2, 1, 0])
        axis.text(0, 3, 'S', fontsize=18, horizontalalignment='center', verticalalignment='center')
        axis.text(7, 3, 'G', fontsize=18, horizontalalignment='center', verticalalignment='center')
    
        for x in range(10):
            for y in range(7):
                axis.add_patch(patches.Rectangle([x-0.5, y-0.5], 1, 1, fill=False))
            
                params = {'head_width':0.2, 'head_length':0.2, 'color':'gray', 'alpha':.2}
                if self.action_type == "regular":
                    action = np.argmax([q_value[(x,y), a] for a in self.action_space])
                    if action == 0:
                        axis.arrow(x, y, -0.1, 0, **params)
                    elif action == 1:
                        axis.arrow(x, y, 0, -0.1, **params)
                    elif action == 2:
                        axis.arrow(x, y,  0.1, 0, **params)
                    elif action == 3:
                        axis.arrow(x, y, 0,  0.1, **params)
                        
                elif self.action_type == "king":
                    action = np.argmax([q_value[(x,y), a] for a in self.action_space])
                    if action == 0:
                        axis.arrow(x, y, -0.1, 0, **params)
                    elif action == 1:
                        axis.arrow(x, y, 0, -0.1, **params)
                    elif action == 2:
                        axis.arrow(x, y,  0.1, 0, **params)
                    elif action == 3:
                        axis.arrow(x, y, 0,  0.1, **params)
                    elif action ==4:
                        axis.arrow(x, y, -0.1, -0.1, **params)
                    elif action == 5:
                        axis.arrow(x, y, -0.1, 0.1, **params)
                    elif action == 6:
                        axis.arrow(x, y,  0.1, -0.1, **params)
                    elif action == 7:
                        axis.arrow(x, y, 0.1,  0.1, **params)
                        
                elif self.action_type == "king_zero":
                    action = np.argmax([q_value[(x,y), a] for a in self.action_space])
                    if action == 0:
                        axis.arrow(x, y, -0.1, 0, **params)
                    elif action == 1:
                        axis.arrow(x, y, 0, -0.1, **params)
                    elif action == 2:
                        axis.arrow(x, y,  0.1, 0, **params)
                    elif action == 3:
                        axis.arrow(x, y, 0,  0.1, **params)
                    elif action ==4:
                        axis.arrow(x, y, -0.1, -0.1, **params)
                    elif action == 5:
                        axis.arrow(x, y, -0.1, 0.1, **params)
                    elif action == 6:
                        axis.arrow(x, y,  0.1, -0.1, **params)
                    elif action == 7:
                        axis.arrow(x, y, 0.1,  0.1, **params)
                    elif action == 8:
                        axis.arrow(x, y, 0,  0, **params)
                        
                        
        for i in range(len(action_path)-1):
            x, y = action_path[i]
            next_x, next_y = action_path[i+1]
            axis.plot([x, next_x], [y, next_y], color='blue', alpha=1.0)

        plt.savefig((str(self.enviroment) + type_graph_name + "_" + type_graph + "_paths.png"), dpi =500)



    def plot_episode_time_step(self, data,  type_graph = "reward", type_graph_name = "default"):

        fig = plt.figure()
        axis = fig.add_subplot(111)
        if type_graph == "reward":
            axis.plot(data, color='blue')
            plt.axhline(y=0.2, color='red', linestyle='-')
            axis.set_title(type_graph_name+ " Reward vs Time Step")
            axis.set_xlabel("Time Steps")
            axis.set_ylabel("Reward per Step")
        elif type_graph == "action":
            axis.plot(data, color='blue')
            axis.set_title(type_graph_name + " Maximal Action vs Time Step")
            plt.axhline(y=0.36, color='red', linestyle='-')
            axis.set_xlabel("Time Steps")
            axis.set_ylabel("Maximal Action Value")
        elif type_graph == "time_step":
            axis.plot(data, color='blue')
            axis.set_title(type_graph_name +" Episode vs Time Step")
            axis.set_xlabel("Time Steps")
            axis.set_ylabel("Episodes")
        plt.savefig((str(self.chart_path) + type_graph_name + "_" + type_graph + "_.png"), dpi =500)



        



