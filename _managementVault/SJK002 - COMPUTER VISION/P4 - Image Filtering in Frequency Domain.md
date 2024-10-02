---
Subject: Computer Vision
Teacher: "@FilibertoPlaBañón"
Topic: Filtering in Frequency Domain
date: 2024-09-23
tags:
  - SJK002-ComputerVIsion
---
# 4.0 Notes
- Review excel I made in "Ampliació de teoria de circuits"
- [Wikipedia - Convolution Theorem](https://en.wikipedia.org/wiki/Convolution_theorem)
- [Convolution Theorem - An Overview (source)](https://www.sciencedirect.com/topics/engineering/convolution-theorem)

# 4.1 Intro

2D Fourier transformation
$$
I(x,y) = I(u, v)
$$
Translates a matrix into two frequencies, one for each direction
Can be used, for example, for edge detection

# 4.2 Fourier transformation
## 4.2.1 Refresh

Decomposition of a function into an infinite sum of sinusoidal functions.

![[Pasted image 20240923164734.png]]
$$
f(x) = \frac{a_0}{2} + \sum_{n=1}^{\infty} a_ncos(nx) + \sum_{n=1}^{\infty}b_ncos(nx)
$$
Where:
- $a_0$ is the base offset over the $y$ axis
- $a_n, b_n$ are the weights of that component

$a_n, b_n$ are calculated as:
$$
a_n = \frac{1}{\pi}\int_{-\pi}^{+\pi}f(x)cos(nx)dx
$$
$$
n=0,1,2,3...
$$

$$
a_n = \frac{1}{\pi}\int_{-\pi}^{+\pi}f(x)sin(nx)dx
$$
$$
n=1,2,3,4...
$$
And the cosine and sine functions can be expressed as complex numbers like:
$$
cos(\phi) = \frac{e^{i\phi}+e^{-i\phi}}{2i}
$$
$$
cos(\phi) = \frac{e^{i\phi}-e^{-i\phi}}{2i}
$$

## 4.2.2 Discrete transformed applied to images

What happens in 2D and on an Image plain:
- An image is a "limited region" for this function, so the longest period (lowest frequency) available for each axis, is the width or height of the image.
- An image is a discrete space, so the highest frequency available 

So, the expression of the Fourier transform for a discrete system and a limited region function is:
$$
F[k,j] = \sum_{m=0}^{M-1}\sum_{n=0}^{N-1}f[n,m]e^{-2\pi i (kn/N+jm/M)}
$$
>[!abstract] Annotation
>The result of a "senoidal" wave in 2D looks like an egg package

## 4.2.3 Modulation

- Magnitude (amplitude) for each harmonic
- Phase

## 4.2.4 The transform and its properties

![[Pasted image 20240923171033.png]]
Both transformations are lossless

Actually, the resulting DFT Magnitud image, would not be exactly like that, but instead, it is divided in quadrants and reordered to obtain the "Optic DFT:
![[Pasted image 20240923171740.png]]

- From the DFT Magnitude representation, we can observe that the lowest frequencies (closest to the center of the axes), are predominant. This is typical of a, so to say, "natural" image.

- The DFT Phase representation is almost always used to reconstruct the image.

>[!example] Artificial example
>![[Pasted image 20240923171826.png]]
>![[Pasted image 20240923171836.png]]
>![[Pasted image 20240923171853.png]]
>*Logaritmic scale just to appreciate the changes better*
>![[Pasted image 20240923172043.png]]

## 4.2.5 DFT/FFT

- In 1D signals for N samples
	- DFT: Holds for any N value $O(N^2)$
	- FFT: Only holds for N values that are power 2 $O(Nlog(N))$ (Zero padding)

- In 2D:
	- The transform is separable; can be calculated over one whole axis and then once for the other axis
	- Transform first in one dimension and then in the other dimension
	- That is because the function is symmetric

# 4.3 Convolution theorem, the relationship between the spatial and frequential realm
#exam

*How does a convolution translates to the frequency realm?*

If we convolute an image with a kernel: $f*g=h$, it translates into a frequency-by-frequency product of $F * G = H$. In other words, the result of the convolution's Fourier transform multiplied by the image's Fourier transform.

Then, to recover the "original image but filtered", we also have to multiply the phase (actually, we multiply the complex polar form).

![[Pasted image 20240923173642.png]]

>[!example] Examples with different filters 
>- Mean vs. Gaussian
>![[Pasted image 20240923174438.png]]
>- Low-Pass filter: You lose detail due to the loss of HIGH FREQ. = BORDERS
>![[Pasted image 20240923174828.png]]
>- High-Pass filter: You select the borders, lose plain textures -> GET BORDERS (notice how the major part of an image's information is in the low frequencies)
>![[Pasted image 20240923175123.png]]
>- Periodical noise in a diagonal direction (low pass filter on the two dots at higher freqs.)
>![[Pasted image 20240923174844.png]]
>- Filtering the newspaper's text frequency to see the ball a bit clearer, sort of a *bokeh* effect
>![[Pasted image 20240923175311.png]]



