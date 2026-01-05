import matplotlib.pyplot as plt
import numpy as np
from mdp.states import State, Action


# def plot_values_comparison(values_vi, values_pi):
#     states = [state.name for state in State]
#     indices = np.arange(len(states))

#     vi = [values_vi[state.value] for state in State]
#     pi = [values_pi[state.value] for state in State]

#     width = 0.35

#     plt.figure()
#     plt.bar(indices - width / 2, vi, width, label="Value Iteration")
#     plt.bar(indices + width / 2, pi, width, label="Policy Iteration")

#     plt.xticks(indices, states, rotation=45)
#     plt.ylabel("State Value")
#     plt.title("State Value Comparison")
#     plt.legend()
#     plt.tight_layout()
#     plt.show()



def iteration_comparison(values_vi, values_pi, policy_vi, policy_pi):
    states = [state.name for state in State]

    vi = [values_vi[state.value] for state in State]
    pi = [values_pi[state.value] for state in State]

    print("\nState Values Comparison:")
    print("-" * 50)
    print(f"{'STATE':15} | {'VI':10} | {'PI':10} | {'DIFF':10}")
    print("-" * 50)

    for state, vi_val, pi_val in zip(states, vi, pi):
        diff = vi_val - pi_val
        print(f"{state:15} | {vi_val:<10.3f} | {pi_val:<10.3f} | {diff:<10.3f}")

    vi_actions = [Action(policy_vi[state.value]).name for state in State]
    pi_actions = [Action(policy_pi[state.value]).name for state in State]

    print("\nIteration Comparison:")
    print("-" * 40)
    for s, vi, pi in zip(states, vi_actions, pi_actions):
        print(f"{s:15} | VI: {vi:10} | PI: {pi:10}")
