from algorithms.value_iteration import run_value_iteration
from algorithms.policy_iteration import run_policy_iteration
from mdp.states import State
from utils.cli import *
from analysis.plots import *
import random



def main():
    print("==========================================")
    print("|                                        |")
    print("| 🎞️ Welcome to the Film Recommender 📽️ |")
    print("|              using MDPs!               |")
    print("|                                        |")
    print("=========================================== \n\n\n")
    while True:
        print("Please, select the best genre recommendation policy according to the following values:\n")
        print("1. Value Iteration\n")
        print("2. Policy Iteration\n")
        print("3. Comparaison between both iterations\n")
        print("Any other key to exit\n")
        choice = input("Enter your choice: ")

        match choice:
            case '1':
                gamma = ask_gamma()
                policy, values = run_value_iteration(gamma)
                print_results("Value Iteration", policy, values)

            case '2':
                gamma = ask_gamma()
                policy, values = run_policy_iteration(gamma)
                print_results("Policy Iteration", policy, values)


            case '3':
                gamma = ask_gamma()

                # Escollim un state aleatori per comparar les dues iteracions
                possible_start_states = [s for s in State if s != State.END]
                state = random.choice(possible_start_states)

                # vi -> Value Iteration
                # pi -> Policy Iteration
                policy_vi, values_vi = run_value_iteration(gamma, state)
                policy_pi, values_pi = run_policy_iteration(gamma, state)

                iteration_comparison(values_vi, values_pi, policy_vi, policy_pi)

            case _:
                print("Exiting program.")
                break


main()


'''
Que esta mostrant el main.py?

EXEMPLE DE RESPOSTA:
================= Value Iteration Results ================

State values:
ACTION -> -38.525
COMEDY -> -43.357
HORROR -> -37.798
ROMANCE -> -51.169
DOCUMENTARY -> -53.876
SCI_FI -> -37.795
END -> -149.757

Optimal policy:
ACTION -> SIMILAR
COMEDY -> SIMILAR
HORROR -> SIMILAR
ROMANCE -> LIGHTER
DOCUMENTARY -> INTENSE
SCI_FI -> SIMILAR
END -> SIMILAR

(gamma 0.9)

===========================================================

Aquestes dades que esta mostrant el main.py és un exemple de resultat de sortida de l'algorisme de Value Iteration.
És una solució matemática del MDP que hem definit amb:
- Estats (ACTION,COMEDY,HORROR,ROMANCE,DOCUMENTARY,SCI_FI,END)
- Accions (SIMILAR,LIGHTER,INTENSE)
- Transicions (probabilitats)
- Recompenses (preferencies)
- Gamma (0.9 en aquest cas, quan més proper a 1 més es valoren les recompenses futures)

* No és una simulació, és una taula de decisions òptimes.

Què significa state values?
Exemple:
Action -> -38.525
Significat:
"Si començo en ACTION i segueixo sempre la política óptima, el valor esperat total de la sessió serà -38.525"
    - No es una probabilitat
    - No es una puntuació bona/dolenta absoluta
    - És un valor relatiu entre estats

Perque tots els valors son negatius (amb gamma 0.9)?
    - La sessió sempre acaba en END
    - END té una recompensa molt negativa (-15 per qualsevol acció)
    - gamma 0.9 fa que les recompenses futures tinguin molt de pes

* Tard o d'hora s'acaba perdent (la gent acaba cansant-se de les recomanacions i marxant)
* L'algorisme medeix quant temps tardes en perdre
* Quan més alt sigui el valor, millor.

Que significa optimal policy?
Exemple:
ROMANCE -> LIGHTER
Significat:
Si l'usuari està veient una pel·lícula de ROMANCE, l'acció que maximitza el valor esperat a llarg termini és recomanar una pel·lícula més LIGHTER (més lleugera).
    - Això no ho decidim nosaltres, ho decideix l'algorisme mirant:
        - Les probabilitats d'anar a END
        - Recompenses
        - Gamma

Interpretació estat per estat amb gamma 0.9:
    - ACTION -> SIMILAR
        - Acció similar manté la sessió viva
        - Menys risc d'anar a END
        - Conservador però segur

    - ROMANCE -> LIGHTER
        - Aqui l'algorisme ha après:
            - Desde ROMANCE, recomanar algo més lleuger redueix la probabilitat d'anar a END més que seguir igual

    - DOCUMENTARY -> INTENSE
        - Aqui l'algorisme diu:
            - Documentary té moltes probabilitats de morir lentament. Per tant, millor arriscar-se a recomanar algo INTENSE que quedar-se estancat i acabar en END.
            - La opció més optima.

    - END -> SIMILAR
        - End és un estat terminal
        - Un cop aquí, només pots quedar-te aquí


Quin paper juga gamma en tot això?
    - gamma en 0.9 significa: prefereixo sobreviure més temps encara que guanyi poc pes cada pas.


    

Que passa amb un gama més baix, per exemple 0.2?
L'algorisme mira només a curt termini, el futur quasi no li importa, i el castig d'anar a END és menys rellevant. Per això els valors de State values ara son positius.

Si tenim:
ACTION -> 1.501
Significa:
"Si començo en ACTION, el que més importa és la recompensa immediata, el futur negatiu quasi no importa."

Seguim tenint Optimal policy amb molts SIMILAR ja que aquesta és una bona recompensa inmediata.


Diferència entre Value Iteration i Policy Iteration
La diferència fundamental en cada iteració és la següent:
    - Value Iteration: Aquesta iteració primer calcula els valors de cada estat i seguidament dedueix la política óptima.
    - Policy Iteration: Calcula directament la política óptima, després calcula els valors de cada estat i a mida que avança va millorant la política fins que no pugui més.

En quant als resultats, veiem que independentment del gamma la diferència dels states és sempre més menor de 1.

State Values Comparison (gamma = 0.1):
--------------------------------------------------
STATE           | VI         | PI         | DIFF
--------------------------------------------------
ACTION          | 1.457      | 1.455      | 0.002
COMEDY          | 1.454      | 1.453      | 0.002
HORROR          | 1.478      | 1.474      | 0.004
ROMANCE         | 1.361      | 1.358      | 0.003
DOCUMENTARY     | 1.170      | 1.166      | 0.004
SCI_FI          | 1.469      | 1.465      | 0.004
END             | -16.650    | -16.667    | 0.017

State Values Comparison (gamma = 0.45):
--------------------------------------------------
STATE           | VI         | PI         | DIFF
--------------------------------------------------
ACTION          | 1.373      | 1.365      | 0.007
COMEDY          | 1.263      | 1.255      | 0.009
HORROR          | 1.234      | 1.226      | 0.007     
ROMANCE         | 0.454      | 0.444      | 0.010
DOCUMENTARY     | -0.263     | -0.274     | 0.011
SCI_FI          | 1.375      | 1.368      | 0.007
END             | -27.252    | -27.273    | 0.021


State Values Comparison (gamma = 0.9):
--------------------------------------------------
STATE           | VI         | PI         | DIFF
--------------------------------------------------
ACTION          | -38.525    | -38.762    | 0.237
COMEDY          | -43.357    | -43.594    | 0.237
HORROR          | -37.798    | -38.035    | 0.237
ROMANCE         | -51.169    | -51.406    | 0.238
DOCUMENTARY     | -53.876    | -54.113    | 0.238
SCI_FI          | -37.795    | -38.031    | 0.237
END             | -149.757   | -150.000   | 0.243

Que les diferències siguin tan lleus en el state és una bona senyal de que en els dos algoritmes el MDP és estable i sempre acaba en una política final semblant.
Hem notat que, tot i la diferència sempre és menor de 1, al presentar un gamma més alt aquesta és fa major, ja que les recompenses futures tenen més pes en el càlcul
dels valors dels estats. En canvi, al presentar un gamma baix, el model prioritza recompenses immediates i els resultats tendeixen a ser semblants.


'''