---
Subject: Machine Learning
Teacher: "@RamónAlbertoMollinedaCárdenas @JoséSalvadorSánchezGarreta"
Topic: 
date: 
tags:
  - SJK003-MachineLearning
---
# 2.0 Notas
- **REFS**:
	- [Evaluation Measures - EvidentlyAI](https://www.evidentlyai.com/classification-metrics/multi-class-metrics#:~:text=Macro-averaging%20calculates%20each%20class%27s,of%20the%20number%20of%20instances.)
	- [Statistics Concepts - Basics](https://datasciencedojo.com/blog/top-statistical-concepts/)

# 2.1 Concepto

- Aplicable en el aprendizaje supervisado

- Se lidia con valores continuos, y se basa en minimizar el error entre la realidad y el valor predicho

## 2.1.1 Modelos de clasificado

- Threshold de probabilidad a una clase (en cuyo caso se devuelve una etiqueta de clase)

- Probabilidad de que el input pertenezca a cierta clase (valor numérico; vector de todas las probs de todas las clases, en realidad)

## 2.1.2 Matriz de confusion

> [!quote] 
> Se puede hacer una matriz de confusion gracias al hecho de que las muestras tienen la información necesaria para ver si la identificación ha sido correcta.

![[Pasted image 20240912181215.png]]

$$\sum(diag) = correct values$$
$$Accuracy = \frac{TP + TN}{\sum all}$$
$$Error = 1 - Accuracy$$

La precision y el error pueden ser engañosos:

>[!example]
>For instance, suppose a data set with 100 instances where 99 belong to class ‘A’ and only 1 belongs to class ‘B’. A model that predicts all instances to class ‘A’ will have an accuracy of 99%, but the accuracy here provides us with little information on how actually the model is performing

>[!example] Ejemplo real
>Deteccion de tumores benignos/malignos -> La mayoría de recursos serán de benignos

>[!example] Ejemplo real
>Detección de manchas de aceite en el océano, la mayoría de imagenes que se tienen como muestra son de oceano sin mancha de aceite.

Son necesarios metodos para evaluar **problemas de clases desbalanceadas** -> Existen técnicas, como:

- **Undersampling**: Reducir el numero de muestras de la clase mayoritaria para que haya las mismas que de la minoritaria
- **Oversampling**: Crear muestras sintéticas de la clase minorita

Metodos alternativos de evaluación:

- **FalsePositive rate** 
$$FP_{rate} = \frac{FP}{FP + TN}$$

- **FalseNegative rate**
$$FN_{rate} = \frac{FN}{FN+TP}$$
- **TruePositive** / recall / sensitivity
$$TP_{rate} = \frac{TP}{FN+TP}$$
- **TrueNegative** /specificity
$$FN_{rate} = \frac{FN}{FN+TP}$$
- **Precision**
$$Precision = \frac{TP}{FP+TP}$$

- **NegativePredictedValue**
$$NPV = \frac{TN}{FN+TN}$$

>[!quote]
>Se suele denominar "positiva" a la clase en la que se está interesado, que tambien suele ser la minoritaria

![[Pasted image 20240912182926.png]]

- **Geometric mean of accuracies**: Llega a su máximo cuando las dos tasas de acierto son máximas
$$G_{mean} = \sqrt{TP_{rate} · TN_{rate}}$$

- **Metrica ponderada** (mean class weighted accuracy):
$$CWA = w · TP_{rate} + (1-w) · TN{rate}$$

- **F-measure**
$$'F-measure' = \frac{(1+\beta) · recall · precision}{\beta^2 ·recall + precision}$$

- **ROC Curve** /macroaverage: [Curva ROC - WIkiPedia](https://es.wikipedia.org/wiki/Curva_ROC), 
$$AUC = \frac{TP_{rate} + TN_{rate}}{2}$$

## 2.1.3 Modelos de regresión

- **RESIDUAL**: Diferencia entre valor real y predicho

- Interesa **EL TAMAÑO de los residuales**, y no un numero de errores

- **DIAGRAMA DE RESIDUOS** 
	![[Pasted image 20240912184224.png]]
	- Interesa la **distancia al 0** -> SD?
	- Interesa que **no esté sesgado**, que haya tantos puntos arriba como abajo del 0
	
>[!hint] Se obtendría una gaussiana si la regresión es válida. El objetivo es centrarla en 0 y reducir su Desviación Etandar

**CONCEPTOS ESTADÍSTICOS IMPORTANTES:**
- Coeficiente de Variación: Sirve para comparar desviaciones estándar de sets con medias distintas
$$ CV(pc) = \frac{SD}{mean} $$
- Sum-squared error:
$$\sum_{i=1}^n (y_i - \hat{y}_i)^2$$

> "^" es el valor predicho

[COMPLETE]

>[!quote]
Sobre las medidas de error, va a tener el mismo efecto **un error grande** que **muchos errores pequeños**. Hay que descartar outliers

![[Pasted image 20240912185722.png]]

Para intentar aliviar el problema de los errores cuadráticos:

- **Relative squared error**

$$RSE = \frac{\sum_{i=1}^n (y_i - \hat{y}_i)}{\sum_{i=1}^n (y_i - \bar{y}_i)}$$

	- Si es mayor que 1: Las predicciones son peores que devolver la media como respuesta siempre
	- Si es menor que 1: Es mejor que devolver la media siempre
	- Si es 0, es perfecto

- **R^2**
$$R^2 = 1-RSE$$
	- Cuanto más se acerque a 1, mejor

[COMPLETE]

> [!question] 
> Puede R^2 ser negativo?
> [StackExchange Response](https://stats.stackexchange.com/questions/12900/when-is-r-squared-negative)

