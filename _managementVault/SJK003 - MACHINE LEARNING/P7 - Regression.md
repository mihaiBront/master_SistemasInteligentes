# 7.1 Concepts
**No classes**, but the target is a value, an approximate  relationship between dependent and independent variables.

- Simple linear regression
- Multiple linear regression 

**2 proposites**:
- Explanatory: regression analysis explains the relationship between response and predictor variables
- Predictive: giva an estimate of the response based on the value of the predictors

![[Pasted image 20241002161106.png]]![[Pasted image 20241002161227.png]]
# 7.2 Types of relationships

- Deterministic *Not interested in that*
- **Statistic** INTERESTING

## 7.2.1 Fundamentals
- Hipothesis (assumptions)
	- Linearity (response variable is a linear combination of parameters and the predictor variable)
	- Normality (variables follow symmetric and Gaussian distribution)
- Preliminarity assessment of strength of the hypothesis:
	- Linear correlation coefficient (*Parson's coef.*)
		![[Pasted image 20241002161619.png]]
		- Si $r = 0$ -> No correlation
		- If $r > 0$ positive relationship
		- If $r < 0$ negative relationship
		And...
		- If $|r| < 0.5$ the correlation is, generally speaking, a weak one
		- If $|r| > 0.8$ the correlation is, generally speaking, a strong one
		![[Pasted image 20241002162118.png]]
>[!note]
>On the bottom row, although there is, obviously some kind of order in the samples, since there is no linear relation, the Parson coef. is 0 (no linear correlation)
		
		![[Pasted image 20241002162314.png]]
		
>[!example] Visual case:
>![[Pasted image 20241002162725.png]]
>- (a) and (b): the points fit perfectly on the straight line, so that we have a linear relationship between the two variables:
>	- (a): with negative slope, which indicates that as X increases, Y becomes smaller and smaller.
>	- (b) with positive slope.
>- (c): it is possible to ensure the existence of a strong relationship between the two variables, but it is not a linear relationship.
>- (d): the points are completely dispersed, so that there is no type of relationship between the variables. 
>- (e) and (f): there is some kind of linear relationship between the two variables: 
>	- (e): a type of linear dependence with a negative slope.
>	- (f): linear relationship with positive slope, but not as strong as the previous case.
>
>![[Pasted image 20241002163015.png]]


# 7.3 Parameter estimation
$$
e_i = y_i - \hat{y}_i = y_i - (b_0 = b_1x_i)
$$

But, how do we get the best fitting line? Well, it will be the one that minimizes differences between observed and predicted data:

$$
L = \sum_{i=1}^n (y_i - (b_0 + b_1x_i))
$$
By aplying derivatives with respect to b0 and b1, and setting them = 0 (maximum or local minima):

![[Pasted image 20241002163858.png]]

# 7.4 Validation (quality of the fit)

![[Pasted image 20241002165850.png]]
![[Pasted image 20241002165902.png]]
![[Pasted image 20241002165915.png]]

**How do we know if the fit adjusts well to observed data?**

- Residual plot: We are looking for the amount of error should be equal above and under the linera regression
	![[Pasted image 20241002170006.png]]
- Coefficient of determination (R-squared):
	![[Pasted image 20241002170410.png]]
	![[Pasted image 20241002170432.png]]
	in a percentual form, it explains what portion of the dependent variable is explainable due to the independent variable: the closer to 1 the better
	![[Pasted image 20241002170236.png]]
- Observed data vs predicted data

**Is the inferred model adequate for the general problem?**

# 7.4 Hypothesis testing