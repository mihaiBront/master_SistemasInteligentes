---
Subject: Computer Vision
Teacher: "@FilibertoPlaBañón"
Topic: Filtering in Spatial Domain
date: 2024-09-23
tags:
  - SJK002-ComputerVIsion
---
# 3.0 Notas


# 3.1 Conceptos:

Why is it needed?

- Denoising: retrieve original data
	- Spatial filtering
	- Frequency filtering ([[P4 - Image Filtering in Frequency Domain]])

# 3.2 Linear filters

Linear transformation of an image (polynomic)

## 3.2.1 Convolution 
#exam

From a said function $f(x)$ and another one $g(x)$, the convolution is the result of the product of the intersection and then derivation of both function:
$$
Conv = (f*g)(x) = \int_{-\infty}^{+\infty}f(\alpha)·g(x-\alpha)
$$
Graphical example:
![[Pasted image 20240923152755.png]]
In a discrete case:
$$
\sum_{-\infty}^{+\infty}f(\alpha)·g(x-\alpha)
$$
But image plains are defined as a 2D matrix:

$$
\sum_{i}\sum_{j}K(i,j)I(x-i, y-j)
$$
Where:
- **K** is the kernel (smaller than the image by nature). Has an origin, which is usually its  center point
- **I** is the image itself

In natural lenguage, we could say that it is reduced to:
- Multiplication of a kernel by te region of the image centered on a center
- Summatory of all values in resulting matrix

>[!example]
>Image convolution with a kernel:
>![[Pasted image 20240923153402.png]]
>The kernel is placed centered on a speciffic pixel, the operations in this example are:
>![[Pasted image 20240923153436.png]]
>The value of computing the convolution of that kernel on the image on a certain pixel is the last image.

>[!note] What happens in corners and borders?
>Usually, the pixels that fall outside the image are interpolated before convoluted

>[!note] Kernels are usually required to be of odd sizes
>Kernels are usually odd-sized (`3x3`, `5x5`, `5x7`...), that is because, with an even sized kernel, there is no exact center defined. You CAN use an even-sized kernel but the result of the convolution would be ever so slightly displaced (the bigger the kernell, the lesser the desplacement)

## 3.2.2 Median filter (ideal low-pass filter)

The kernel (a $3x3$ example) would be:
$$
K = 
\begin{bmatrix}  
1 & 1 & 1\\  
1 & 1 & 1\\
1 & 1 & 1
\end{bmatrix}
$$
The result of that filtering is like averaging all pixels inside the kernel

![[Pasted image 20240923154641.png]]

## 3.2.3 Gaussian filtering (low-pass filter)
#lab

Linear filters with weighs defined by a gaussian function on a kernel of size (Kx, Ky); ***windowSize***, and a ***sigma*** (variance)

The result of processing a gaussian on that kernel, is an oval/round gaussian on the plain.

$$
g[x, y] = e^{\frac{x^2+y^2}{2\sigma^2}}
$$

Can be obtained by a gaussian matrix, which contains only the values of a diagonal if it represents a circle or an oval aligned with the x/y axis:

$$
K_{gauss}(x, y) = \begin{bmatrix}
\sigma_x & 0\\
0 & \sigma_y
\end{bmatrix}
$$

Or has elements in the other places if it i is not:

$$
K_{gauss}(x, y) = \begin{bmatrix}
\sigma_x & a\\
b & \sigma_y
\end{bmatrix}
$$

>[!abstract] Appreciation
>Looking at the formula for defining the Gaussian function, it can be easily realised that:
>- For the center point of the kernel, the value will always be 1 ($e^0$)
>- The further away from the center, the weight will always descend
>- The lower the sigma, the faster the weight will descend

A Gaussian matrix has:
- Axial symmetry
- Single lobe (one maximum): which is important for the frequency domain, much more simpler in the frequency realm (the *Fourier Transform* of a Gaussian is a Gaussian)
- Low-Pass properties
- Its intensity is controlled by $\sigma$

## 3.3 Median filter (non-linear)

How does it work?
1. Select all values that fall inside the kernel
2. Sort and find the middle point
3. Take that middle point and assign it to the pixel selected by the kernel

Properties
- Non-linear
- Works very good with very noisy images
- Preserves edges with good quality

>[!example] Comparations
>![[Pasted image 20240923161827.png]]
>![[Pasted image 20240923161329.png]]
>![[Pasted image 20240923161349.png]]

>[!quote] Advancements
>**Anisotropic**: Not equal in all direction -> Preserves well the *second order discontinuities*
>**First order disctontinuities**: *Borders*
>**Second order discontinuities**: *Corners* are considered second order discontinuities, and as you can see, median does not preserve them well

