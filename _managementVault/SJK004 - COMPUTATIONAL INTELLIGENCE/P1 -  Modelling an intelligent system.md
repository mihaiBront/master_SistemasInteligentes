---
Subject: Computational Intelligence
Teacher: "@LuisAmableGarcíaFernández"
Topic: 
date: 
tags:
  - SJK004-ComputationalIntelligence
---
# 1 Agents
*"An **INTELLIGENT** agent is an entity capable of performing autonomous, flexible actions in an environment."*

**Flexible** implies:
- Reactive: Holds continuous interactions w/the environment. Reacts to the simules in its medium
- Pro-Active: Oportunistic interpretation of the changes in the dynamics of the medium
- Social: Interacts, and solicitates information other agents in the environment

# 2. Environment
*"Physical or virtual  medium, common to all agents"*

| **Environment characteristics** +                                                                                      | **Environment characteristics** -                                      |
| ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| Accessible: Agents have vision of the whole entirity of the environment                                                | Not - Accessible: View of environment is limited                       |
| Deterministic: Results of actions can be predicted                                                                     | Non-Deterninistic: Actions don't always translate into a same reaction |
| Episodic: It works in blocks, between which, the conditions of how the last episode ended does not affect the next one | Non-Episodic                                                           |
| Static                                                                                                                 | Dynamic                                                                |
| Discrete                                                                                                               | Continuous                                                             |

# 3. How can intelligence be approached?

Can appear:
1. As a consequence of statistical model, fed with an enormous pre-processed data (**machine learning**)
2. Emerging as a massive interaction of simple rules (**neural networks**)
3. Conventional programming -> **Intentional systems** (BDI Logic is freq. used)
4. Combinations of previously mentioned

## 3.1 Machine learning:

"*Computer programs that learn from experience*".

Used in ambits like:
- Prediction from complex data historics

### Supervised learning: -> [[P0 - Introducción a la asignatura]]

- Set of learning data that is already tagged algorithm gets image + class
- Evaluation, not passing class to algorithm, but we know what class the images are

### Unsupervised learning -> Classificator, learns to group

### Semi supervised
### Active learning

### **REINFORCED LEARNING**

# 4. Reinforcement learning

![[Pasted image 20240919160132.png]]
- Política: función que, dado el estado actual, determina qué acción hacer
- Función de valor: función que puntúa todos los otros estados posibles en función del estado actual.
- Acción
- Modelo
- Estado: Valores de las variables del entorno en un momento dado

## 4.1 Tipos de estados

![[Pasted image 20240919160434.png]]

## 4.2 Acciones:
Actions: Can be 
- Discrete (choose one among the N available actions )
- Continuous (an array of scalar values, e.g.)

## 4.3 Politics
Policy: A projection from the set of states to the set of actions. This projection can be: 
- Deterministic. 
- Stochastic.

## 4.4 Value function

Value functions: Two types 
- $V\pi(s)$, the value that can be obtained accumulating the potential reward obtained from state s following policy ℼ 
- $Q\pi(s,a)$, the value that can be obtained accumulating the potential reward obtained from state s, performing action a, and then, following policy ℼ

>[!quote] Explanation
> - V: Sumatorio de de recompensas desde el punto actuar al punto de máximo valor alcanzable
> - Q(s, a) Valor acumulado des del estado S, haciendo la accion A y a partir de ahí seguir la política

![[Pasted image 20240919161349.png]]

- Time: $t$
- $S_t \in S$ (set of states)
- $A_t \in A$ (set of actions)
- $R_t \in R$ (set of real numbers)

## 4.3 Calculations:

RETURN:
![[Pasted image 20240926151700.png]]

>[!abstract] Limit cases
>- If $\gamma$ = $0$: Only the immediatly following state is important
>- If $\gamma$ = $1$: All following states are equally weighted
>- If $\gamma$ is closer to $0$: More proximal cases are much more weighted than further away ones
>- If $\gamma$ is closer to $0$: The state weight decreases slower with distance


# 5. Decision making
## 5.1 Markov Decision Process (MDP)

- Sistemas sin memoria ("*no me importa que he hecho hasta ahora, solo lo que me queda por hacer hasta llegar al objetivo*") -> El sistema solo depende del estado actual

>[!example] Example
>Robots don't care of how they reached a point, only what they have to do from there on

- Tupla de 4 elementos: 
$$
probability = <S, A, T, R>
$$
-  $S$: Status
- $A$: Action
- $R$: Transition Probabilities

> [!example] Recycling bot
> - States [low, high] battery
> - Actions:
> 	- A(low) = {search, wait, recharge}
> 	- A(high) = {search, wait}
> - Rewards: 
> 	- `1` for each can collected, 
> 	- `0` if no can collected, 
> 	- `-3` if stopped for recharge
> 
> ![[Pasted image 20240919163151.png]]
>![[Pasted image 20240919165004.png]]

[Markov DP Solving (pg.24 :LiArrowBigRight:)](obsidian://open?vault=_managementVault&file=_res%2F_assets%2FSJK004%2FUnit%201_%20Modelling%20an%20Intelligent%20agent_1.pdf)
>[!example]
>Imagin the following case:
>
>Space of following states: (pairs $N,rew$)
>
>|  |  | |
>| ---- | ---- | ----- |
>| 4(0) | 5(0) | 6(1)  |
>| 3(0) | IMP  | 7(-1) |
>| 2(0) | 1(0) | 0(0)  |
>
>Set of movements:
>A = {:LiArrowBigUp:, :LiArrowBigRight:, :LiArrowBigLeft:, :LiArrowBigDown:}
>
>We will have of max transitions of 8(cells) x 8 x 4 (movements)
>
>1. Supongamos que el coste para el agente al ejecutar una accion es $-10$. Si $\gamma$ es $0$ y ek agente está en el estado 0, qué acción debe tomar?
>
>*Con $\gamma$ = $0$, como solo le importa el siguiente comportamiento, el set de recompensas ordenados igual que A:*
>	*$R = {-11, -10, -10, -10}$*
>	
>*Con $\gamma = .5$*, tenemos dos opciones de camino valido:
>	$Aa = {U, U} -> R = (-11+ \frac{-9}{2}) = -15.5$
>	$Ab = {L, L, U, U, R, R} -> R = -19.66$

## 5.2 Solution methods
![[Pasted image 20240926155008.png]]
![[Pasted image 20240926154942.png]]
![[Pasted image 20240926154951.png]]

# 6 Environment discovery (real life)

