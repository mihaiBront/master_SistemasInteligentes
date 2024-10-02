---
Subject: Machine Learning
Teacher: "@RamónAlbertoMollinedaCárdenas @JoséSalvadorSánchezGarreta"
Topic: 
date: 
tags:
  - SJK003-MachineLearning
---

<object data="../_res/SJK003/01-introduction.pdf" type="application/pdf">
	<div>No online PDF viewer installed</div>
</object>

# 0. Links
- [Varianza y sesgo](https://aprendeia.com/bias-y-varianza-en-machine-learning/) 

# 1. Concepts

A computer system is said to learn from some experience E with respect to some task T and performance measure P, if its performance at task T, as measured by P, improves with experience E
## 1.1 Experience

Set of examples for a certain task (observations, samples...). An example is made of a number of features (**quantitative**/measurables; discrete values or **qualitative**)

Examples of features:
- People's faces would be examples. More than one picture for the same face would also be examples. Features would be the encoding of the pixels of an image, which would be discrete values -> **quantitative**
	
- With that person example:
	- We can establish classes/categories in function of the person. All images from one person would have the same class (for examples)
	- They are described by an N number of features, which form a **vector of attributes**
![[Pasted image 20240911155158.png]]
- 2 types:
	- **SUPERVISED**: Each sample's class is known, tries to predict from `p(y,x)` when exposed to new info.
		![[Pasted image 20240911155548.png]]
	- **NON-SUPERVISED** (clustering "*agrupamientos*"): Samples are not associated with class labels. Start is making groups like "these are similar -> call it class A ..."
		![[Pasted image 20240911155602.png]]
		Knowing, for example, how many classes there are helps with the problem
	- [MIDGROUND] **Semi-supervised**: Easy and fast to get unlabeled samples, labeled examples are hard to get. Using a small set of labeled samples and a larger one of unlabeled ones. 
		Use unsupervised techniques to predict labels and then feed them to a supervised alg.
		![[Pasted image 20240911160112.png]]

## 1.2 Task

- 2 tipos segun la funcion
	- **clasificación**
	- **regresión** -> Predecir un solo valorico numerico
- segun el modelo
	- **parametrico**: asume la forma de una ecuacion matematica, sabe mas o menos como va a ser la distribución:
		- poor performance if the assumptions are not met 
		- less training data are required 
		- computationally faster
		- Some algorithms: naïve Bayes, linear regression, logistic regression, linear SVM, neural networks, etc.
	- **no-parametrica**: no asume nada:
		- more accurate predictions since they offer a better fit to data 
		- easier since they do not need to make any assumption 
		- risk of overfitting 
		- Some algorithms: decision tree, k nearest neighbours, non-linear SVM, Gaussian processes, etc
- **Performance** is a god measure for comparing models
	- for classification:
		$$accuracy = \frac{n_{correct}}{n_{total}}$$
		$$error_rate = 1- accuracy$$
	- for regression:
		![[Pasted image 20240911162721.png]]

## 1.3 Fases del entrenamiento:

**APRENDIZAJE**:

- Set de pruebas
- Objetivo = minimizar el error al clasificar esas muestras

**EVALUACIÓN**

- Set de pruebas diferente
- Usar el modelo entrenado para analizar el set de evaluacion.
- Objetivo = obtener un un nivel de error parecido al del entrenamiento

> [!note]
> No usar samples del set de aprendizaje en la evaluación

La **generalizacion** 

Asumciones:
- the training examples are independent of the test examples 
- the training and test sets are identically distributed 
- i.e., the same (unknown, implicit) distribution function generated both training and test examples 
- if we could set the parameters in advance, 𝑡𝑟𝑎𝑖𝑛𝑖𝑛𝑔 𝑒𝑟𝑟𝑜𝑟 ≅ 𝑡𝑒𝑠𝑡 𝑒𝑟𝑟𝑜𝑟
- however, the parameters are optimized from the training set and therefore, 𝑒𝑥𝑝𝑒𝑐𝑡𝑒𝑑 𝑡𝑟𝑎𝑖𝑛𝑖𝑛𝑔 𝑒𝑟𝑟𝑜𝑟 ≤ 𝑒𝑥𝑝𝑒𝑐𝑡𝑒𝑑 𝑡𝑒𝑠𝑡 𝑒𝑟𝑟𝑜𝑟

> [!note]
> El error de entrenamiento siempre va a ser menor, o como mucho igual que el error de aprendizaje

## 1.4 Over and underfitting

- **OVERFITTING**: Modelo demasiado complejo, se ciñe demasiado al set de entrenamiento, no es capaz de obtener conclusiones de datos nuevos. Sesgo bajo y varianza alta 

- **UNDERFITTING**: Modelo muy simple, no logra un error lo suficientemente bajo. Varianza muy pequeña y sesgo grande

## 1.5 Capacidad del modelo

Es la capacidad del modelo que otorga para controlar la probabilidad de caer en under u overfitting

![[Pasted image 20240911164300.png]]

>[!tip]
>Objetivo: hacer modelos en el sweet spot donde se minimicen ambos errores
