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
    · It represents a map of the probability of moving from the actual state to a new state when a certain action is taken.

        RETURN
        - T (np.array): Transition probability matrix

    Es:
    Construye la matriz de probabilidad de transición T[action][state][next_state]
    · Representa un mapa de la probabilidad de moverse del estado actual a un nuevo estado cuando se toma una acción determinada.
    
        RETURN
        - T (np.array): Matriz de probabilidad de transición

    Ca:
    Construeix la matriu de probabilitat de transició T[action][state][next_state]
        · Representa un mapa de la probabilitat de moure's de l'estat actual a un nou estat quan es pren una acció determinada.
        
        RETURN
        - T (np.array): Matriu de probabilitat de transició 
    
    
    
    ==== BORRAR ABANS D'ENTREGAR O ALGO NO SE ====
    
    BASICAMENT EL QUE BUSCA FER AQUESTA FUNCIÓ ÉS RETORNAR, A PARTIR DE L'ESTAT ACTUAL I L'ACCIÓ ACTUAL, LA PROBABILITAT DE CADA POSSIBLE FUTUR ESTAT. BASICAMENT CREA UN MAPA (LA MATRIU DE TRANSICIÓ) QUE DESPRÉS FARÀ SERVIR VALUE/POLICY ITERATION 
    PER ESCOLLIR UN CAMÍ.

    [AQUESTA FUNCIÓ NO ESTA ACABADA ENCARA]
    '''
    n_actions = len(Action) # Necessitem el nombre exacte d'accions i estats per poder saber les dimensions de la matriu 
    n_states = len(State) 

    T = np.zeros((n_actions, n_states, n_states)) # Creem la matriu de transició amb zeros, 3 dimensions. Ara mateix per defecte tot es 0, per tant, per defecte no hi ha transició possible entre ningun estat.
    
    for key, value in TRANSITIONS.items(): # TRANSITIONS és el nostre diccionari, on key => estat i acció actual, value => outcomes (possibles futurs estats i les seves probabilitats), 
        state = key[0]
        action = key[1]
        outcomes = value
        for next_state, prob in outcomes.items(): # El que fem es omplenar la matriu de transició amb les probabilitats corresponents trobades al diccionari TRANSITIONS, les que no apareixen al outcome per aquella accio-estat es quedaran a 0.
            T[action][state][next_state] = prob
    
    for action in Action: # END és un estat terminal, per tant, des d'ell només podem seguir a ell mateix amb probabilitat 1 (100%).
        T[action][State.END][State.END] = 1.0

    return T

