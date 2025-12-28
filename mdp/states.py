from enum import IntEnum

class State(IntEnum):
    '''
    En:
    Enum representing different movie genres and an end state.

    Es:
    Enum que representa diferentes géneros de películas y un estado final.

    Ca:
    Enum que representa diferents gèneres de pel·lícules i un estat final.
    '''
    ACTION = 0
    COMEDY = 1
    HORROR = 2
    ROMANCE = 3
    DOCUMENTARY = 4
    SCI_FI = 5
    END = 6


class Action(IntEnum):
    '''
    En:
    Enum representing types of recommendation actions.
    Es:
    Enum que representa tipos de acciones de recomendación.
    Ca:
    Enum que representa tipus d'accions de recomanació.
    '''
    SIMILAR = 0
    LIGHTER = 1
    INTENSE = 2
