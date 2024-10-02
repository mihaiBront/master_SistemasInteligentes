---
Subject: Computer Vision
Teacher: "@FilibertoPlaBañón"
Topic: 
date: 
tags:
  - SJK002-ComputerVIsion
---
# 5.0 Notes


# 5.1 What is an edge?

![[Pasted image 20240930151324.png]]

An edge is a significant change in image intensity, and it is useful for identifying object features and its limits.

Types:

![[Pasted image 20240930151509.png]]
# 5.2 Steps in edge detection

## 5.2.1 Filtering for changes enhancement

Finding the perfect filter for both **reducing the noise** and **enhance discontinuities**

**Edge detectors**: algorithms in charge of those two steps

![[Pasted image 20240930151932.png]]

## 5.2.2 Detecting and locating pixels

Deciding whether it is a pixel or not (avoiding or interpolating edges)

## 5.2.3 Subpixel precision estimation (optional)

Refining curves that define edges

![[Pasted image 20240930152247.png]]

# 5.3 Edge detectors based on image gradient

![[Pasted image 20240930152318.png]]
What effect does the gradient have over a function? -> It detects changes in a wave

## 5.3.1 2D Gradient

$$
\nabla f(x, y) = \frac{\partial f}{\partial x} \vec{i} +\frac{\partial f}{\partial y} \vec{j} 
$$

![[Pasted image 20240930153339.png]]
### Variants of the gradient

- **Gradients depending on its magnitude**:
$$
m(x, y) = \sqrt{f^2_x + f^2_y}
$$
	Following gradients adre only done along the x axis, so it only detects edges in x
	- First one is taking the module, on its full range (from -1 to 1, resampled to [0:255])
	- Second one (BL) is the absolute value of that; since we care about edges, we don't care if they're positive or negative
	- Third (BR) is the 255-complement of the third
	![[Pasted image 20240930153441.png]]
	
- **Gradients combining directions:**
	We can obtain both axes if we sum both derivatives absolute values
	![[Pasted image 20240930153759.png]]
	
- **Angle of the gradient**: 
$$
\phi(x, y) = arctan(\frac{f_y}{f_x})
$$
	In human language, it provides the normal of an edge (perpendicular to the tangent), and it can be understood as the "*the direction of maximum variation for the function in a point*"
	
	If we represent a function along a line defined by the rotation at one point (and passing through that point) we will se a maximum.
	
- **Magnitude sum vs Module**:
	
	![[Pasted image 20240930154357.png]]

The gradient method is very susceptible to noise in contours, their contours are not usually defined and smooth, so image might have to be treated before edge detection

>[!success] #exam Relacionar las expresiones matematicas con tipos de filtros así como con el efecto que tienen sobre las imagenes

>[!success] #exam Razonar y entender las explicaciones de los métodos para solucionar el problema del descentrado de la imagen a raíz del descentrado de los filtros

>[!abstract] Discrete derivatives:
>Remembering derivatives:
>$$
>f'(x) = lim_{h->0}\frac{f(x+h) - f(x)}{h}
>$$
>In a discrete set:
>- The derivative on the right
>$$
>f'(x) = \frac{f(i+1) - f(i)}{samplingPeriod}
>$$.
>- Or, why not, the derivative on the left
>$$
>f'(x) = \frac{f(i) - f(i-1)}{samplingPeriod}
>$$
>Which would take the same value for a continuous function, but not necessarily in a discrete space


- **The simplest gradient**:
$$
\begin{equation}
	\begin{cases}
		\begin{bmatrix}
		-1 & 1
		\end{bmatrix}\\
		\begin{bmatrix}
		-1\\1
		\end{bmatrix}
	\end{cases}
\end{equation}
$$
	This will detect the variations to the RIGHT and towards the BOTTOM
- **Centered variant:**
$$
\begin{equation}
	\begin{cases}
		\begin{bmatrix}
		-1 & 0 & 1
		\end{bmatrix}\\
		\begin{bmatrix}
		-1\\0\\1
		\end{bmatrix}
	\end{cases}
\end{equation}
$$
- **Prewitt operator**: combines a gradient with an average filter:
$$
\begin{equation}
	\begin{cases}
		\begin{bmatrix}
		-1 & 0 & 1 \\ -1 & 0 & 1 \\ -1 & 0 & 1 
		\end{bmatrix}\\
		\begin{bmatrix}
		-1 & -1 & -1 \\ 0 & 0 & 0 \\ 1 & 1 & 1
		\end{bmatrix}
	\end{cases}
\end{equation}
$$
- **Sobel operator**: combines a gradient with an average filter, but weighting the center by the double:
$$
\begin{equation}
	\begin{cases}
		\begin{bmatrix}
		-1 & 0 & 1 \\ -2 & 0 & 2 \\ -1 & 0 & 1 
		\end{bmatrix}\\
		\begin{bmatrix}
		-1 & -2 & -1 \\ 0 & 0 & 0 \\ 1 & 2 & 1
		\end{bmatrix}
	\end{cases}
\end{equation}
$$
- **Isotropic operator**: combines a gradient with an average filter, but weighing the center $\sqrt{2}$ more
$$
\begin{equation}
	\begin{cases}
		\begin{bmatrix}
		-1 & 0 & 1 \\ -\sqrt{2} & 0 & \sqrt{2} \\ -1 & 0 & 1 
		\end{bmatrix}\\
		\begin{bmatrix}
		-1 & -\sqrt{2} & -1 \\ 0 & 0 & 0 \\ 1 & \sqrt{2} & 1
		\end{bmatrix}
	\end{cases}
\end{equation}
$$
- **Gaussian + gradient**: since they both have the *associative property*, instead of applying both, we can apply the derivative to the gaussian kernel, then applying it to the image:
	
	- *In 1D* : 
	![[Pasted image 20240930160840.png]]
	- *In 2D* : (in the next example, the derivative is performed along the x axis)
	![[Pasted image 20240930160907.png]]

>[!abstract]
>In 2D, the variance ($\sigma$) is a matrix:
>$$
>covarianceMatrix = 
>\begin{bmatrix}
>	\sigma_x & \sigma_{xy}\\
>	\sigma_{yx} & \sigma_{x}
>\end{bmatrix}
>$$
>In the case, above, the variance is the same for x and for y, and doesn't have any value on the variance matrix other diagonal

- **Robert's** and **Kirsch's masks** for edge detection in distinct directions:
![[Pasted image 20240930162119.png]]

>[!abstract] Meaning of the derivative
>![[Pasted image 20240930162300.png]]
>Local maximums are potential edge points (2nd Derivative = 0, point where sign changes)

## 5.3.3 Edge detectors based on gradient
#### Binarize
![[Pasted image 20240930162639.png]]![[Pasted image 20240930162648.png]]
![[Pasted image 20240930170221.png]]

- **CANNY** edge detection -> Optimal when the noise on the image has a gaussian distribution (*shot noise for instance*; also thermal noise)
	![[Pasted image 20240930170749.png]]
	
	1. **Smoothing + Enhancement**: Gradient of a gaussian function
	2. **Detection: significant local maxima**
		- **Non-Maximal suppression** -> Keeping local maxima; depends on the magnitude and the direction of the gradient; detecting gradient maxima in the gradient direction
		- **Hysteresis threshold** -> 2 thresholds in combination ($T_1 < T_2$);
			1. For each pixel, finding the *gradient direction*
			2. Along the line defined by the gradient direction, check if *THAT specific pixel is a local maximum*, if so, keep (also keeps the magnitude)
			3. Finally, applying a *threshold for defining WHAT IS THE MINIMUM VALUE TO BE CONSIDERED AS THRESHOLD* (here is where we use both thresholds, explained later)
			What do the two threshold mean then?
			- Gradient magnitude $>T2$ -> Pixel <b style="color: green; font-weight:600">IS AN EDGE</b>
			- Gradient magnitude $<T1$ -> Pixel is <b style="color: red; font-weight:600">NOT AN EDGE</b>
			- $<T1$ Gradient magnitude $>T2$ -> Pixel <b style="color: darkgoldenrod; font-weight:600">IS AN EDGE</b> but only if it connects to a $>T2$  edge
			![[Pasted image 20240930171710.png]]
			How is *"connection"* determined?

## 5.3.2 Laplacian operator

![[Pasted image 20240930172916.png]]
In the center of one edge, there is:
- A change of sign
- A value where $\nabla^2 f(x) == 0$

It has a big problem; that being being especially sensitive to noise, much more than using the *gradient* (first derivative). Therefore, finding smoothing methods that would prevent that is imperative.

- **Laplacian of a gaussian**:
	![[Pasted image 20240930173733.png]]
	![[Pasted image 20240930173741.png]]
	![[Pasted image 20240930173833.png]]
	**APPLICATIONS**
	- Enhancing the contrast in borders; 2nd derivative added to the image increases the contrast in borders; being $\alpha$ the constant by which we want to increase contrast in borders
		![[Pasted image 20240930175006.png]]
		![[Pasted image 20240930175137.png]]

How to evaluate how aggressive is an edge? The bigger the slope when passing by y=0; the better; it also allows for sub-pixel interpolation.

$\sigma$ controls the amount of smoothing
- σ large -> 
	- robust edges, but shifted
	- More lost edges / Found edges are robust
	- Less precision (edge shift) / Nearby edges can be merged
- σ small -> 
	- better localization
	- More sensitive to noise / More false edges
	- More precision to locate edges

