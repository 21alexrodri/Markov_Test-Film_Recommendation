from mdp.states import State, Action


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

def print_results(title, policy, values):
    print(f"================= {title} Results ================\n")
    print("State values:")
    for state in State:
        print(state.name, "->", round(values[state.value], 3))

    print("\nOptimal policy:")
    for state in State:
        print(state.name, "->", Action(policy[state.value]).name)

    print("===================================================")
    