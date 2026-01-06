import mdptoolbox
from mdp.transitions import build_transition_matrix
from mdp.rewards import build_reward_matrix
from utils.cli import show_path

'''
En:
    Module implementing the Policy Iteration algorithm for a Markov Decision Process (MDP).

Es:
    Módulo que implementa el algoritmo de Policy Iteration para un Proceso de Decisión de Markov (MDP).

Ca:
    Mòdul que implementa l'algorisme de Policy Iteration per a un Procés de Decisió de Markov (MDP).

'''
def run_policy_iteration(gamma: float = 0.9, state=None, max_steps=10):
    T = build_transition_matrix()
    R = build_reward_matrix()

    pi = mdptoolbox.mdp.PolicyIteration(T, R, gamma)
    pi.run()

    policy = pi.policy
    values = pi.V

    # Simulació del recorregut
    show_path("Policy Iteration", T, policy, state, max_steps)
    
    return policy, values