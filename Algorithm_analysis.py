from header_import import *

if __name__ == "__main__":
    
    number_episode = 10000

    # Algorithums
#     regular = sarsa_algorithm(episode=number_episode, gamma=1, alpha=0.5, epsilon=0.1, max_time_step=number_episode, action_type="regular", wind_type="regular")
#     regular_time_step, q_value = regular.sarsa()
#     plot = plot_graphs(action_type="regular", wind_type="regular")
#     plot.plot_episode_time_step(regular_time_step, type_graph = "time_step", type_graph_name="Sarsa | 4 action")
#     plot.plot_windy(q_value, type_graph = "time_step", type_graph_name="Sarsa | 4 action") 

#     king = sarsa_algorithm(episode=number_episode, gamma=1, alpha=0.5, epsilon=0.1, max_time_step=number_episode, action_type="king", wind_type="regular")
#     king_time_step, q_value = king.sarsa()
#     plot = plot_graphs(action_type="king", wind_type="regular")
#     plot.plot_episode_time_step(king_time_step, type_graph = "time_step", type_graph_name="Sarsa | 8 action")
#     plot.plot_windy(q_value, type_graph = "time_step", type_graph_name="Sarsa | 8 action") 


#     king_zero = sarsa_algorithm(episode=number_episode, gamma=1, alpha=0.5, epsilon=0.1, max_time_step=number_episode, action_type="king_zero", wind_type="regular")
#     king_zero_time_step, q_value = king_zero.sarsa()
#     plot = plot_graphs(action_type="king_zero", wind_type="regular")
#     plot.plot_episode_time_step(king_zero_time_step, type_graph = "time_step", type_graph_name="Sarsa | 9 action")
#     plot.plot_windy(q_value, type_graph = "time_step", type_graph_name="Sarsa | 9 action")
 

    king = sarsa_algorithm(episode=number_episode, gamma=1, alpha=0.5, epsilon=0.1, max_time_step=number_episode, action_type="king", wind_type="not_regular")
    king_zero_time_step_not_normal, q_value = king.sarsa()
    plot = plot_graphs(action_type="king", wind_type="not_regular")
    plot.plot_episode_time_step(king_zero_time_step_not_normal, type_graph = "time_step", type_graph_name="Sarsa | 8 action | 50 percent")
    plot.plot_windy(q_value, type_graph = "time_step", type_graph_name="Sarsa | 8 action | 50 percent")


#     regular = q_learning_algorithm(episode=number_episode, gamma=1, alpha=1, epsilon=0.1, max_time_step=number_episode, action_type="regular", wind_type="regular")
#     reward_average, max_action = regular.q_learning()
#     plot.plot_episode_time_step(reward_average, type_graph = "reward", type_graph_name="Q_Learning reward | alpha 1")
#     plot.plot_episode_time_step(max_action, type_graph = "action", type_graph_name="Q Learning action | alpha 1")


#     reward_average, max_action = regular.double_q_learning()
#     plot.plot_episode_time_step(reward_average, type_graph = "reward", type_graph_name="Double Q_Learning reward | alpha 1")
#     plot.plot_episode_time_step(max_action, type_graph = "action", type_graph_name="Double Q Learning action | alpha 1")
 

#     regular = q_learning_algorithm(episode=number_episode, gamma=1, alpha=0.8, epsilon=0.1, max_time_step=10000, action_type="regular", wind_type="regular")
#     reward_average, max_action = regular.q_learning()
#     plot.plot_episode_time_step(reward_average, type_graph = "reward", type_graph_name="Q_Learning reward | alpha 0.8")
#     plot.plot_episode_time_step(max_action, type_graph = "action", type_graph_name="Q Learning action | alpha 0.8")


#     reward_average, max_action = regular.double_q_learning()
#     plot.plot_episode_time_step(reward_average, type_graph = "reward", type_graph_name="Double Q_Learning reward | alpha 0.8")
#     plot.plot_episode_time_step(max_action, type_graph = "action", type_graph_name="Double Q Learning action | alpha 0.8")
