from mdp.transitions import build_transition_matrix
from mdp.states import State, Action

T = build_transition_matrix()

print(T[Action.INTENSE][State.ACTION])
print(T[Action.INTENSE][State.ACTION].sum())