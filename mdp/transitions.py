import numpy as np
from mdp.states import State, Action
TRANSITIONS = {

    # ACTION
    (State.ACTION, Action.SIMILAR): {
        State.ACTION: 0.60,
        State.SCI_FI: 0.25,
        State.COMEDY: 0.10,
        State.END: 0.05,
    },

    (State.ACTION, Action.LIGHTER): {
        State.COMEDY: 0.40,
        State.ROMANCE: 0.30,
        State.ACTION: 0.15,
        State.DOCUMENTARY: 0.10,
        State.END: 0.05,
    },

    (State.ACTION, Action.INTENSE): {
        State.HORROR: 0.45,
        State.SCI_FI: 0.30,
        State.ACTION: 0.15,
        State.END: 0.10,
    },

    # COMEDY
    (State.COMEDY, Action.SIMILAR): {
        State.COMEDY: 0.65,
        State.ROMANCE: 0.20,
        State.ACTION: 0.10,
        State.END: 0.05,
    },

    (State.COMEDY, Action.LIGHTER): {
        State.COMEDY: 0.50,
        State.ROMANCE: 0.30,
        State.DOCUMENTARY: 0.15,
        State.END: 0.05,
    },

    (State.COMEDY, Action.INTENSE): {
        State.ACTION: 0.40,
        State.SCI_FI: 0.25,
        State.HORROR: 0.20,
        State.END: 0.15,
    },

    # HORROR
    (State.HORROR, Action.SIMILAR): {
        State.HORROR: 0.70,
        State.SCI_FI: 0.15,
        State.ACTION: 0.10,
        State.END: 0.05,
    },

    (State.HORROR, Action.LIGHTER): {
        State.SCI_FI: 0.35,
        State.ACTION: 0.30,
        State.COMEDY: 0.20,
        State.END: 0.15,
    },

    (State.HORROR, Action.INTENSE): {
        State.HORROR: 0.60,
        State.ACTION: 0.25,
        State.END: 0.15,
    },

    # ROMANCE
    (State.ROMANCE, Action.SIMILAR): {
        State.ROMANCE: 0.65,
        State.COMEDY: 0.25,
        State.END: 0.10,
    },

    (State.ROMANCE, Action.LIGHTER): {
        State.COMEDY: 0.45,
        State.DOCUMENTARY: 0.30,
        State.ROMANCE: 0.15,
        State.END: 0.10,
    },

    (State.ROMANCE, Action.INTENSE): {
        State.ACTION: 0.35,
        State.SCI_FI: 0.30,
        State.HORROR: 0.15,
        State.END: 0.20,
    },

    # DOCUMENTARY
    (State.DOCUMENTARY, Action.SIMILAR): {
        State.DOCUMENTARY: 0.70,
        State.COMEDY: 0.15,
        State.END: 0.15,
    },

    (State.DOCUMENTARY, Action.LIGHTER): {
        State.COMEDY: 0.40,
        State.ROMANCE: 0.30,
        State.DOCUMENTARY: 0.15,
        State.END: 0.15,
    },

    (State.DOCUMENTARY, Action.INTENSE): {
        State.ACTION: 0.35,
        State.SCI_FI: 0.25,
        State.HORROR: 0.20,
        State.END: 0.20,
    },

    # SCI-FI
    (State.SCI_FI, Action.SIMILAR): {
        State.SCI_FI: 0.65,
        State.ACTION: 0.25,
        State.HORROR: 0.05,
        State.END: 0.05,
    },

    (State.SCI_FI, Action.LIGHTER): {
        State.ACTION: 0.35,
        State.COMEDY: 0.30,
        State.DOCUMENTARY: 0.20,
        State.END: 0.15,
    },

    (State.SCI_FI, Action.INTENSE): {
        State.SCI_FI: 0.45,
        State.HORROR: 0.35,
        State.ACTION: 0.10,
        State.END: 0.10,
    },
}

def build_transition_matrix():
    '''
    En:
    Builds the transition probability matrix T[action][state][next_state]
        · T represents the probability of moving from 'state' to 'next_state' when an action is taken.
    Es:
    Construye la matriz de probabilidad de transición T[action][state][next_state]
        · T representa la probabilidad de moverse de 'state' a 'next_state' cuando se toma una acción.
    Ca:
    Construeix la matriu de probabilitat de transició T[action][state][next_state]
        · T representa la probabilitat de moure's de 'state' a 'next_state' quan es pren una acció.
    
    
    
    ==== BORRAR ABANS D'ENTREGAR O ALGO NO SE ====
    Quin problema resol aquesta funció?
        Si estic en un estat S i faig una acció A, a quins estats puc anar i amb quina probabilitat?
        Això es guarda en T, una matriu de transicions.
    
    Que retorna?
        Retorna una estructura buida on més endavant s'ha de posar les probabilitats

    T s'ha de pensar com si fossin 3 capes, exemple:
    T[Action.SIMILAR][State.ACTION][State.COMEDY]
    Significa: probabilitat de passar de ACTION a COMEDY quan faig l'acció SIMILAR
    
    
    [AQUESTA FUNCIÓ NO ESTA ACABADA ENCARA]
    '''
    n_actions = len(Action)
    n_states = len(State)

    T = np.zeros((n_actions, n_states, n_states))
    
    for (state, action), outcomes in TRANSITIONS.items():
        for next_state, prob in outcomes.items():
            T[action][state][next_state] = prob
    
    for action in Action:
        T[action][State.END][State.END] = 1.0

    return T

