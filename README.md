# Markov_Test-Film_Recommendation


## 📘 Description

#### -- English --
This project models a movie recommendation system as a Markov Decision Process (MDP).
At each step, the system observes the genre the user is currently watching and decides which type of movie to recommend next.

Each recommendation action can lead to different outcomes with certain probabilities, such as the user switching genre, staying in the same genre, or ending the session.

#### -- Castellano --

Este proyecto modela un sistema de recomendación de películas como un Proceso de Decisión de Markov (MDP).
En cada paso, el sistema observa el género que el usuario está viendo y decide qué tipo de película recomendar.

Cada acción de recomendación puede producir distintos resultados con ciertas probabilidades, como cambiar de género, continuar igual o cerrar la sesión.

#### -- Català --

Aquest projecte modela un sistema de recomanació de pel·lícules com un Procés de Decisió de Markov (MDP).
A cada pas, el sistema observa el gènere que l’usuari està veient i decideix quin tipus de pel·lícula recomanar.

Cada acció de recomanació pot tenir diferents resultats amb probabilitats associades, com canviar de gènere, continuar igual o acabar la sessió.

## 🪛 Objective

#### -- English --

To find an optimal recommendation policy that maximizes user engagement and minimizes session abandonment.

#### -- Castellano --

Encontrar una política óptima de recomendación que maximice la retención del usuario y minimice el abandono de la sesión.

#### -- Català --

Trobar una política òptima de recomanació que maximitzi la permanència de l’usuari i minimitzi l’abandonament de la sessió.

## 🔎 States

#### -- English --

- S0 – User watching Action
- S1 – User watching Comedy
- S2 – User watching Horror
- S3 – User watching Romance
- S4 – Session ended (terminal state)

#### -- Castellano --
- S0 – Usuario viendo Acción
- S1 – Usuario viendo Comedia
- S2 – Usuario viendo Terror
- S3 – Usuario viendo Romance
- S4 – Sesión terminada (estado terminal)

#### -- Català --
- S0 – Usuari veient Acció
- S1 – Usuari veient Comèdia
- S2 – Usuari veient Terror
- S3 – Usuari veient Romàntic
- S4 – Sessió acabada (estat terminal)

## 🎬 Actions

#### -- English --
- A0 – Recommend similar content
- A1 – Recommend lighter content
- A2 – Recommend more intense content

#### -- Castellano --
- A0 – Recomendar contenido similar
- A1 – Recomendar contenido más ligero
- A2 – Recomendar contenido más intenso

#### -- Català --
- A0 – Recomanar contingut similar
- A1 – Recomanar contingut més lleuger
- A2 – Recomanar contingut més intens

## 📊 Transition

#### -- English --
For each state and action, multiple next states are possible with different probabilities.
The next state depends only on the current state and the selected action, fulfilling the Markov property.

The terminal state (S4) is absorbing.

#### -- Castellano --
Desde cada estado y acción se puede pasar a varios estados posibles con probabilidades distintas.
El siguiente estado depende solo del estado actual y la acción elegida, cumpliendo la propiedad de Markov.

El estado terminal (S4) es absorbente.

#### -- Català --
Des de cada estat i acció es pot passar a diversos estats possibles amb diferents probabilitats.
El següent estat depèn només de l’estat actual i l’acció triada, complint la propietat de Markov.

L’estat terminal (S4) és absorbent.

## ⭐ Rewards (example)

#### -- English --

- The user continues watching: positive reward
- The genre is changed successfully: positive reward
- End of the session: negative reward

**Wyh this reward structure?**

The objetive is to maximize the user engagement and permanence in the platform, so we reward actions that lead to continued watching or successful genre changes, while penalizing session endings.

#### -- Castellano --

- El usuario continúa viendo: recompensa positiva
- El género se cambia con éxito: recompensa positiva
- Fin de la sesión: recompensa negativa

**¿Por qué esta estructura de recompensas?**
El objetivo es maximizar la retención del usuario en la plataforma, por lo que se recompensan las acciones que llevan a continuar viendo o a cambios de género exitosos, mientras que se penalizan los cierres de sesión.

#### -- Català --

- L’usuari continua veient: recompensa positiva
- El gènere es canvia amb èxit: recompensa positiva
- Fi de la sessió: recompensa negativa

**Per què aquesta estructura de recompenses?**
L’objectiu és maximitzar la permanència de l’usuari a la plataforma, per això es recompensen les accions que porten a continuar veient o a canvis de gènere exitosos, mentre que es penalitzen els tancaments de sessió.

