import numpy as np
from mdp.states import State, Action
# EN: On a real business case this would be done with a study, and using for example business intelligence patterns it could be analyzed the real case of rewards, but for this project, as requested, we will make a simple and fictitious version.
# ES: Esto en un caso real de empresa se haría con un estudio, y con uso de por ejemplo business intelligence se podrían sacar patrones para analizar el caso real de recompensas, pero para este proyecto, tal y como se ha pedido, haremos una versión simple y ficticia.
# CA: Això en un cas real d'empresa es faria amb un estudi, i amb ús de per exemple business intelligence es podrien treure patrons per analitzar el cas real de rewards, però per aquest projecte, tal i com s'ens ha demanat, farem una versió simple i fictícia.
REWARDS = {
    # ACTION
    State.ACTION: {
        Action.SIMILAR: 1.4,
        Action.LIGHTER: 1.2,
        Action.INTENSE: 1.3,
    },

    # COMEDY
    State.COMEDY: {
        Action.SIMILAR: 1.4,
        Action.LIGHTER: 1.3,
        Action.INTENSE: 0.6,
    },

    # HORROR
    State.HORROR: {
        Action.SIMILAR: 1.3,
        Action.LIGHTER: 1.6,
        Action.INTENSE: 1.1,
    },

    # ROMANCE
    State.ROMANCE: {
        Action.SIMILAR: 1.4,
        Action.LIGHTER: 1.3,
        Action.INTENSE: 0.4,
    },

    # DOCUMENTARY
    State.DOCUMENTARY: {
        Action.SIMILAR: 1.3,
        Action.LIGHTER: 1.3,
        Action.INTENSE: 0.5,
    },

    # SCI_FI
    State.SCI_FI: {
        Action.SIMILAR: 1.4,
        Action.LIGHTER: 1.2,
        Action.INTENSE: 1.5,
    },

    # END (terminal)
    State.END: {
        Action.SIMILAR: -15.0,
        Action.LIGHTER: -15.0,
        Action.INTENSE: -15.0,
    },
}


def build_reward_matrix() -> np.ndarray:
    '''
    En:
    Builds the reward matrix R[state][action]
    · It represents the reward obtained by taking a certain action in a given state.

        RETURN
        - R (np.array): Reward matrix

    Es:
    Construye la matriz de recompensas R[state][action]
    · Representa la recompensa obtenida al tomar una determinada acción en un estado dado.
    
        RETURN
        - R (np.array): Matriz de recompensas

    Ca:
    Construeix la matriu de recompenses R[state][action]
        · Representa la recompensa obtinguda en prendre una determinada acció en un estat donat.
        
        RETURN
        - R (np.array): Matriu de recompenses
    '''
    n_states = len(State)
    n_actions = len(Action)

    R = np.zeros((n_states, n_actions))

    for state, actions in REWARDS.items():
        for action, reward in actions.items():
            R[state][action] = reward

    return R