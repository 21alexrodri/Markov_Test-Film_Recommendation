import mdptoolbox
from mdp.transitions import build_transition_matrix
from mdp.rewards import build_reward_matrix


def run_value_iteration(gamma: float = 0.9):
    T = build_transition_matrix()
    R = build_reward_matrix()

    vi = mdptoolbox.mdp.ValueIteration(T, R, gamma)
    vi.run()

    return vi.policy, vi.V
