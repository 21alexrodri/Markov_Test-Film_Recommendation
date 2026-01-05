import mdptoolbox
from mdp.transitions import build_transition_matrix
from mdp.rewards import build_reward_matrix
from mdp.states import State, Action
import numpy as np
import random



# def run_policy_iteration(gamma: float = 0.9):
#     T = build_transition_matrix()
#     R = build_reward_matrix()

#     pi = mdptoolbox.mdp.PolicyIteration(T, R, gamma)
#     pi.run()

#     return pi.policy, pi.V

def run_policy_iteration(gamma: float = 0.9, max_steps=10):
    T = build_transition_matrix()
    R = build_reward_matrix()

    pi = mdptoolbox.mdp.PolicyIteration(T, R, gamma)
    pi.run()

    policy = pi.policy
    values = pi.V

    # Simulació del recorregut
    print("\nSimulated Path (Policy Iteration):")
    # State inicial aleatori
    possible_start_states = [s for s in State if s != State.END]
    state = random.choice(possible_start_states)
    print("Initial State chosen:", state.name)

    path = [state.name]
    for _ in range(max_steps - 1):
        # Si el state és END, sempre sortirà END, per lo que sortim del bucle
        if state == State.END:
            break

        action = policy[state.value]
        probs = T[action][state.value]
        next_state_index = np.random.choice(len(State), p=probs)
        state = list(State)[next_state_index]

        path.append(state.name)

    # Assegurem que l'ultim state sigui END
    if path[-1] != State.END.name:
        path.append(State.END.name)
    print(" -> ".join(path))

    return policy, values