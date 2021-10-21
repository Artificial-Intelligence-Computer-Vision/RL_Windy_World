from header_import import *

class plot_graphs(object):
    def __init__(self):
        self.path = "graphs_charts/"



    def plot_episode_time_step(self, type_graph = "reward", type_graph_name = "default"):

        fig = plt.figure()
        axis = fig.add_subplot(111)
        if type_graph == "reward":
            axis.plot(self.reward_average, color='blue')
            plt.axhline(y=0.2, color='red', linestyle='-')
            axis.set_title(type_graph_name+ " Reward vs Time Step")
            axis.set_xlabel("Time Steps")
            axis.set_ylabel("Reward per Step")
        elif type_graph == "action":
            axis.plot(self.max_action, color='blue')
            axis.set_title(type_graph_name + " Maximal Action vs Time Step")
            plt.axhline(y=0.36, color='red', linestyle='-')
            axis.set_xlabel("Time Steps")
            axis.set_ylabel("Maximal Action Value")
        plt.savefig((str(self.path) + type_graph_name + "_" + type_graph + "_policy_graphs.png"), dpi =500)



