---
Subject: Machine Learning
Teacher: "@RamónAlbertoMollinedaCárdenas @JoséSalvadorSánchezGarreta"
Topic: 
date: 
tags:
  - SJK003-MachineLearning
---
# 4.0 Notes

- Training sample sets need to be stratified; ideally the sample set should contain the same number of samples for each class.
# 4.1 Intro

**Non-parametric**, **supervised** models can be applied if there exist:
- OBJECTS capable of being described by some formal rep.
- CLASSES that group objects
- Need to AUTOMATE THE CLASSIFICATION

>[!example] Oil spills in the ocean
>![[Pasted image 20240925151220.png]]
>- Objects: Satellite images
>- Formal representation: Vector of features in the image
>	- Pixels
>	- Features
>	- etc.
>- Classes:
>	- Oil Spill
>	- Look-alike
>	- No oil spill

## 4.1.1 Motivation:
This models are classifiers based off of the idea that "the objects inside a class are the most similar". They use similarity (concieved as distance between vectors) measures defined by some model

# 4.2 Types of distance classifiers

## 4.2.1 Minimum Distance Classifier

Classifier that does not take all training data into account, but the designer defines a prototype, a representative that depicts the samples in a single class. This way, an enormous sample set is reduced to a more simpler sample set.

From that reduced data set, the **centroid** is defined by the average of that data set for the class (averaged measures). The most centered sample. This is actually either done:
- By finding a real sample that is the closest to the centroid
- Ellaborating a virtual object, averaging samples, that will represent the centroid

A test object is assigned to the class of the nearest centroid (the minimum distance)

> ![[Pasted image 20240925152122.png]]


**Concepts:**
- <u>Decision boundary</u> Boundary (line on a plain, plain in a 3D space, hyperplanes in higher dimensions) that determines if a sample is assigned a class or another

>[!fail] Flaws
>- Reducing the sample set to define classes implies the loss of information about the classes, making the model less general
>- Loss in detail in decision boundary:
>	![[Pasted image 20240925152223.png]]

## 4.2.2 k Nearest Neighbors (*k-NN*)

All samples available are used for the training.

When trying to classify a new prompt, we go to the sample set and find the $n$ samples that are most similar to that prompt.

![[Pasted image 20240925153818.png]]

How do we assign a class to the new prompt? We take that $n$-sized set of samples and the class will be assigned by majority vote. 

How are **draws** resolved?
- Randomly
- Arbitrarily according to some criteria
	- Assigning a **weight** to each measurement, by distance to the centroid of the class, for example
	- By **priority** (if a class is preferent, like in the example of benign/malign tumors, in case of draw you should always assume the worse)

Said to be a **lazy learner** model since it does not perform any training

Two hyperparameters are needed to be defined:
- **Distance metric**: determine which training data is the closest to a given test point, use that for training
- **The K value**: defines how many neighbors will be checked to guess classification. As can be seen in the image above, the $k$ parameter is critical, and should be found during training by means of optimization

Finding the value of $k$, keep in mind that:
- The error is 0 for $k=1$
- The error is high at low values of $k$ due to variance (*overfitting*), has a **valley** and then goes up again due to bias (*underfitting*).

That precise **valley** is the **sweet spot**

**Concepts**:
- $k$ is the number of samples that are used for finding the class of a sample, later subject to majority decision.

### 4.2.2.1 Classifier with reject option

*If a class doesn't "get enough votes", no decision is made*

This is appliable to any classifier, and in this cased, it is called the *(k-I)-NN* algorithm

The minimum of votes is usually required in the range of $[k/2 < I < k]$

# 4.3 Similarity measures

## 4.3.1 Formulas

**Minkowski** (generic):
$$
d_p(x, y) = (\sum_{i=1}^{d}|y_i - x_i|)^{1/p}
$$

The following ones are the result of the substitution  of p in previous:

**Euclidean** (familiarized with) -> $p = 2$:
$$
d_2(x, y) = \sqrt{\sum_{i=1}^{d}|y_i - x_i|}
$$
**Chebyshev**: -> $p=\infty$:
$$
d_\infty(x, y) = max_{i= 1...d}|y_i - x_i|
$$

**Manhattan**: -> $p = 1$:
$$
d_1(x, y) = \sum_{i=1}^{d}|y_i - x_i|
$$

![[Pasted image 20240925154945.png]]

>[!abstract] Annotation
>- **Chebishev** is the max in strait line over an axis
>- **Manhattan** is independent on the path

- **Cosine similarity**: [COMPLETE]
>[!example] Application of k-NN
>![[Pasted image 20240925160459.png]]
>![[Pasted image 20240925160515.png]]
## 4.3.2 Normalization

Making all atributes the same scale -> Converting the data to a common range (commonly $[0,1]$ or $[-1,1]$) 

- **z-score** (zero-mean) [complete]
- **min-max normalization** [complete]
- **decimal scaling** [complete]

>[!abstract] Summary
>1. Select the number k of neighbors 
>2. Calculate the distance between the training data and the test sample 
>3. Take the k nearest neighbors as per the calculated distance 
>4. Among these k neighbors, count the number of the training data in each class 
>5. Assign the test sample to that category (class) with a majority of neighbors

>[!success] Advantages:
>- **Easy to understand** and implement: given its simplicity, it is one of the first classifiers that a new data scientist will learn 
>- **Adapts easily**: as new training samples are added, the algorithm adjusts to account for any new data since all training data are stored into memory 
>- **Few hyperparameters**: only requires a k value and a distance metric, which is low when compared to other machine learning models

>[!fail] Flaws
>- **Does not scale well**: since k-NN is a lazy algorithm, it uses all the training data at the runtime and hence is slow
>- **Curse of dimensionality**: the k-NN algorithm does not perform well with high-dimensional data
>- **Complexity**: O(n) for each instance to be classified 
>- **Computationally expensive**: it takes up more memory and data storage compared to other classifiers

