import mdptoolbox
from mdp.transitions import build_transition_matrix
from mdp.rewards import build_reward_matrix
from mdp.states import State, Action
import numpy as np
import random



# def run_value_iteration(gamma: float = 0.9):
#     T = build_transition_matrix()
#     R = build_reward_matrix()

#     vi = mdptoolbox.mdp.ValueIteration(T, R, gamma)
#     vi.run()

#     return vi.policy, vi.V

def run_value_iteration(gamma: float = 0.9, state=None, max_steps=10):
    T = build_transition_matrix()
    R = build_reward_matrix()

    vi = mdptoolbox.mdp.ValueIteration(T, R, gamma)
    vi.run()

    policy = vi.policy
    values = vi.V

    # Simulació del recorregut
    print("\nSimulated Path (Value Iteration):")
    # State inicial aleatori
    if state is None:
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
