---
Subject: Big Data Analytics
Teacher: "@RafaelBerlangaLlavori @RafaelBerlangaLlavori"
Topic: 
date: 2024-10-02
tags:
  - "#SJK006-BigDataAnalytics"
---
# 6.1 Context
![[Pasted image 20241002181235.png]]

Permits analysing any type of indicator or measure, such as:
- Anomaly detection
- Breakage detection
- Stock prediction
- Sales prediction
- Demand
- ...

In a datachain:
![[Pasted image 20241002181354.png]]

Axis:
![[Pasted image 20241002181420.png]]

- X AXIS:
	- Time series
	- Data is sampled in equidistant intervals, to ease the data analysis
- Y AXIS: Value of the variable

> [!note]
> Although, usually, and for the examples in this section, the plots are uni-variant, it can be multi-variant

# 6.2 Components of the time series

- Trend: "*tendencia* " -> Linear regression
- Cyclical Patterns -> 
- Seasonal Patterns -> Seasonal sales, for example, like Christmas
- Irregularities -> Might be interest points
- Noise

Types of the series depending on its characteristics

- Stationary vs NonStationary: Depending on weather the average is constant or not (respectively)
- Multiplicative vs Additive: Depending on weather the standard deviation is NOT CONSTANT or CONSTANT respectively
- Stochastic vs Deterministic (deterministic if there is a function that can exactly represent the progression; stochastic if not)

![[Pasted image 20241002182107.png]]
## How to Normalize a Series:

1. Interpolate missing values
2. Remove trend (slope)
3. Remove seasonality (de-seasonalize) -> Senoidales?

Types of smoothing:
- Basic smoothing:
	- Rolling mean (moving average)
	- Exponential smoothing (helps smoothing the multiplicative character)
- Logarithmic transform
- Differentiation (difference with the shifted series)

>[!abstract]
> ![[Pasted image 20241002183503.png]]
>![[Pasted image 20241002183517.png]]

# 6.3 Predictions

