from algorithms.value_iteration import run_value_iteration
from algorithms.policy_iteration import run_policy_iteration
from mdp.states import State, Action
from utils.functions import *
from analysis.plots import *



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
                # print("Select a gamma value (from 0.1 to 0.9, default 0.9): ")
                # print("Gamma value determines the importance of future rewards. A higher gamma (close to 1) values future rewards more, while a lower gamma (close to 0) focuses on immediate rewards.")
                # gamma_input = input("Enter gamma value (or press Enter for default 0.9): ")
                # try:
                #     gamma = float(gamma_input) if gamma_input else 0.9
                #     if not 0 < gamma < 1:
                #         raise ValueError
                # except ValueError:
                #     print("Invalid gamma value. Using default gamma = 0.9")
                #     gamma = 0.9
                
                # policy, values = run_value_iteration(gamma)
                # print("================= Value Iteration Results ================\n")
                # print("State values:")
                # for state in State:
                #     print(state.name, "->", round(values[state], 3))

                # print("\nOptimal policy:")
                # for state in State:
                #     print(state.name, "->", Action(policy[state]).name)
                
                # print("===========================================================")

                gamma = ask_gamma()
                policy, values = run_value_iteration(gamma)
                print_results("Value Iteration", policy, values)

            case '2':
                gamma = ask_gamma()
                policy, values = run_policy_iteration(gamma)
                print_results("Policy Iteration", policy, values)


            case '3':
                gamma = ask_gamma()
                # vi -> Value Iteration
                # pi -> Policy Iteration
                policy_vi, values_vi = run_value_iteration(gamma)
                policy_pi, values_pi = run_policy_iteration(gamma)

                plot_values_comparison(values_vi, values_pi)
                table_policy_comparison(policy_vi, policy_pi)

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

'''