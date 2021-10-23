from header_import import *

if __name__ == "__main__":
    
    # Algorithums
    regular = sarsa_algorithm(episode=10000, gamma=1, alpha=0.5, epsilon=0.1, max_time_step=10000, action_type="regular", wind_type="regular")
    regular_time_step = regular.sarsa()
    regular.plot_episode_time_step(type_graph = "time_step", type_graph_name="Sarsa | 4 action")

    king = sarsa_algorithm(episode=10000, gamma=1, alpha=0.5, epsilon=0.1, max_time_step=10000, action_type="king", wind_type="regular")
    king_time_step = king.sarsa()
    king.plot_episode_time_step(type_graph = "time_step", type_graph_name="Sarsa | 8 action")

    king_zero = sarsa_algorithm(episode=10000, gamma=1, alpha=0.5, epsilon=0.1, max_time_step=10000, action_type="king_zero", wind_type="regular")
    king_zero_time_step = king_zero.sarsa()
    king_zero.plot_episode_time_step(type_graph = "time_step", type_graph_name="Sarsa | 9 action")


    king = sarsa_algorithm(episode=10000, gamma=1, alpha=0.5, epsilon=0.1, max_time_step=10000, action_type="king", wind_type="not_regular")
    king_zero_time_step_not_normal = king.sarsa()
    king.plot_episode_time_step(type_graph = "time_step", type_graph_name="Sarsa | 8 action | 50 percent")


    number_episode = 10000
    regular = q_learning_algorithm(episode=number_episode, gamma=1, alpha=1, epsilon=0.1, max_time_step=10000, action_type="regular", wind_type="regular")
    regular.q_learning()
    regular.plot_episode_time_step(type_graph = "reward", type_graph_name="Q_Learning reward | alpha 1")
    regular.plot_episode_time_step(type_graph = "action", type_graph_name="Q Learning action | alpha 1")
    regular.double_q_learning()
    regular.plot_episode_time_step(type_graph = "reward", type_graph_name="Double Q_Learning reward | alpha 1")
    regular.plot_episode_time_step(type_graph = "action", type_graph_name="Double Q Learning action | alpha 1")
 
    regular = q_learning_algorithm(episode=number_episode, gamma=1, alpha=0.8, epsilon=0.1, max_time_step=10000, action_type="regular", wind_type="regular")
    regular.q_learning()
    regular.plot_episode_time_step(type_graph = "reward", type_graph_name="Q_Learning reward | alpha 0.8")
    regular.plot_episode_time_step(type_graph = "action", type_graph_name="Q Learning action | alpha 0.8")
    regular.double_q_learning()
    regular.plot_episode_time_step(type_graph = "reward", type_graph_name="Double Q_Learning reward | alpha 0.8")
    regular.plot_episode_time_step(type_graph = "action", type_graph_name="Double Q Learning action | alpha 0.8")
