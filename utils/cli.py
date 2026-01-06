from mdp.states import State, Action
import random
import numpy as np

'''
En:
    Common function to ask the user for the gamma value in both Value Iteration and Policy Iteration.

Es:
    Función común para pedir al usuario el valor de gamma tanto en Value Iteration como en Policy Iteration.

Ca:
    Funció comuna per demanar el valor de gamma a l'usuari tant en Value Iteration com en Policy Iteration.

'''
def ask_gamma(default=0.9):
    print("Select a gamma value (from 0.1 to 0.9, default 0.9): ")
    print("Gamma value determines the importance of future rewards.")
    gamma_input = input("Enter gamma value (or press Enter for default 0.9): ")

    try:
        gamma = float(gamma_input) if gamma_input else default
        if not 0 < gamma < 1:
            raise ValueError
        return gamma
    except ValueError:
        print("Invalid gamma value. Using default gamma =", default)
        return default

'''
En:
    Function to print the results of the iterations.

Es:
    Función para mostrar los resultados de las iteraciones.

Ca:
    Funció per mostrar els resultats de les iteracions.

'''
def print_results(title, policy, values):
    print(f"================= {title} Results ================\n")
    print("State values:")
    for state in State:
        print(state.name, "->", round(values[state.value], 3))

    print("\nOptimal policy:")
    for state in State:
        print(state.name, "->", Action(policy[state.value]).name)

    print("===================================================")


'''
En:
    Function to simulate the path of states according to the obtained policy.

Es:
    Función para simular el recorrido de estados según la política obtenida.

Ca:
    Funció per simular el recorregut d'estats segons la política obtinguda.

'''
def show_path(iteration, T, policy, state=None, max_steps=10):
    print(f"\nSimulated Path ({iteration}):")
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

    