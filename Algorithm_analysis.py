from header_import import *

if __name__ == "__main__":
    
    # Algorithums
    regular = sarsa_algorithm(episode=10000, gamma=1, alpha=0.5, epsilon=0.1, max_time_step=10000, action_type="regular", wind_type="regular")
    regular_time_step = regular.sarsa()
    regular.plot_episode_time_step()

    king = sarsa_algorithm(episode=10000, gamma=1, alpha=0.5, epsilon=0.1, max_time_step=10000, action_type="king", wind_type="regular")
    king_time_step = king.sarsa()
    king.plot_episode_time_step()

    king_zero = sarsa_algorithm(episode=10000, gamma=1, alpha=0.5, epsilon=0.1, max_time_step=10000, action_type="king_zero", wind_type="regular")
    king_zero_time_step = king_zero.sarsa()
    king_zero.plot_episode_time_step()

    king = sarsa_algorithm(episode=10000, gamma=1, alpha=0.5, epsilon=0.1, max_time_step=10000, action_type="king", wind_type="not_regular")
    king_zero_time_step_not_normal = king.sarsa()
    king.plot_episode_time_step()
