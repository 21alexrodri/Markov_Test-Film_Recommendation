import matplotlib.pyplot as plt
import numpy as np
from mdp.states import State, Action

'''
En:
    Function to compare and plot the results of Value Iteration and Policy Iteration algorithms.

Es:
    Función para comparar y representar gráficamente los resultados de los algoritmos de Value Iteration y Policy Iteration.

Ca:
    Funció per comparar i representar gràficament els resultats dels algorismes de Value Iteration i Policy Iteration.

'''
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
