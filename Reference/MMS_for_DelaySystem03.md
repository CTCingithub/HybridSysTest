<!--
 * @Author: CTC 2801320287@qq.com
 * @Date: 2024-04-18 16:53:36
 * @LastEditors: CTC 2801320287@qq.com
 * @LastEditTime: 2024-04-20 21:54:38
 * @Description: 
 * 
 * Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
-->
# MMS for Delay Systems Example 03

## 1. Equilibrium and Stability

The equation of the delay system studied is:

$$
\begin{equation}
    \dot{x} = f \left( x_{\tau}, \dot{x} \right),
\end{equation}
$$

where

$$
\begin{equation}
    f (x_{\tau}, \dot{x}) = - \frac{2 k b x_{\tau} + 2 k x_{\tau}^{2} - 6 x_{\tau} \dot{x}}{a - 3 b}.
\end{equation}
$$

With the linearization of Eq. (1), the characteristic equation at trivial equilibrium is expressed as:

$$
\begin{equation}
    \lambda - C - D e^{-\lambda \tau} = 0,
\end{equation}
$$

where

$$
\begin{aligned}
    C &= \left. \frac{\partial f}{\partial x} \right \vert_{x = 0} \\
    &= 0,
\end{aligned} \qquad \qquad
\begin{aligned}
    D &= \left. \frac{\partial f}{\partial x_{\tau}} \right \vert_{x_{\tau} = 0} \\
    &= - \frac{2 k b}{a - 3 b}.
\end{aligned}
$$

Hopf bifurcation occurs if eigenvalues of the eigen equation Eq. (3) are purely imaginary pairs. The author focused on parameter $k$'s influence on stability, and handled it as a bifurcation parameter. Suppose there's only one pair of purely imaginary eigenvalues given by $\pm i \omega$ at $\tau_{c}$ and $\lambda = 0$ is not a root of Eq. (3). Letting $\alpha = \frac{2 b}{a - 3 b}$, and substituting $\lambda = \pm i \omega$ into Eq. (3), we obtain the critical boundary of stability zone in terms of $\tau$ and $k$:

$$
\begin{gather}
    \alpha k \cos{(\omega \tau)} = 0, \\
    \omega - \alpha k \sin{(\omega \tau)} = 0.
\end{gather}
$$

From Eq. (4)(5), the critical boundary is determined by point sets $(\tau^{j}, k)$:

$$
\begin{gather}
    \tau^{j} = \frac{\pi}{2 \omega} + \frac{2 j \pi}{\omega}, \qquad j = 0, 1, 2, \cdots, \\
    \omega = k \alpha.
\end{gather}
$$

Denote the curve combined of point set $(\tau^{j}, k)$ by $S_{j}$. Real part of eigenvalues alter when parameter set $(\tau, k)$ crosses a curve $S_{j}$, and there'll be a switch of stability at stationary state. Define

$$
\begin{gather}
    d_{\tau}^{j} = \left. \frac{\partial \mathrm{Re}(\lambda)}{\partial \tau} \right \vert_{(\tau^{j}, k) \in S_{j}}, \\
    d_{\tau}^{k} = \left. \frac{\partial \mathrm{Re}(\lambda)}{\partial k} \right \vert_{(\tau^{j}, k) \in S_{j}}.
\end{gather}
$$

to indicate the direction of change of the real parts of the eigenvalue on the imaginary axis. Hopf bifurcation may on curve $S_{j}$ if $d_{\tau}^{j} \neq 0$ and $d_{\tau}^{k} \neq 0$, providing that all other eigenvalues of Eq. (3) have nonzero real parts. *The author pointed out that only $j = 0$ corresponds to the case for Hopf bifurcation.*

Choosing $\tau$ to be the unique bifurcation parameter and noticing that $C = 0$, one can obtain from Eq. (3) that

$$
\begin{equation}
    \frac{d \lambda}{d \tau} = - \frac{D \lambda}{e^{\lambda \tau} + D \tau}.
\end{equation}
$$

Noticing that $\lambda = \pm i \omega$. Then, for $\lambda = \pm i \omega$, we have

$$
\begin{aligned}
    \left. \frac{d \lambda}{d \tau} \right \vert_{\lambda = \pm i \omega} &= - \frac{D \lambda}{e^{\lambda \tau} + D \tau} \\
    &= - D \frac{i \omega}{\left( \cos{(\omega \tau)} + D \tau \right) + i \left( \sin{(\omega \tau)} \right)} \\
    &= - \frac{i D \omega}{\left( \cos{(\omega \tau)} + D \tau \right)^{2} + \left( \sin{(\omega \tau)} \right)^{2}} \left( \left( \cos{(\omega \tau)} + D \tau \right) - i \left( \sin{(\omega \tau)} \right) \right) \\
    &= \frac{D \omega}{1 + 2 D \tau \cos{(\omega \tau)} + D^{2} \tau^{2}} \left( - \sin{(\omega \tau)} - i \cos{(\omega \tau)} \right) \\
    &= - \frac{D \omega}{D^{2} \tau^{2} + 1},
\end{aligned}
$$

Provided that $D<0$, it's easy to verify that

$$
\mathrm{Re} \left( \left. \frac{d \lambda}{d \tau} \right \vert_{\lambda = \pm i \omega} \right) = - \frac{D \omega}{D^{2} \tau^{2} + 1} > 0.
$$

Thus, from the the theory of functional differential equations, the author determined that

$$
\begin{gather}
    \tau_{c} = \tau^{0} = \frac{\pi}{2 \omega}, \\
    \omega = k \alpha,
\end{gather}
$$

where $\tau_{c}$ represents the critical time delay for Hopf bifurcation.

## 2. MMS for DDE

This section aims to obtain a **universal conclusion** on MMS for systems with DDE-type dynamics. The DDE Eq. (13) discussed in this section doesn't necessarily refer to Eq. (1).

$$
\begin{equation}
    \dot{z} = c z (t) + d z (t - \tau) + f \left( z(t), \dot{z} (t) \right),
\end{equation}
$$

where $f (\cdot)$ represents a function with **quadratic nonlinearity**. In order to investigate Hopf bifurcation problem, the author perturbed the critcal value of time delay $\tau$ as a bifurcation parameter in Eq. (13):

$$
\begin{equation}
    \tau = \tau_{c} + \varepsilon \tau_{\varepsilon},
\end{equation}
$$

which converts Eq. (13) to

$$
\begin{equation}
    \dot{z} (t) = c z (t) + d z (t - \tau_{c}) + f \left( z(t), \dot{z} (t), z (t - \tau_{c} - \varepsilon \tau_{\varepsilon}), z (t - \tau_{c}), \varepsilon \right),
\end{equation}
$$

where $\varepsilon$ is a small parameter.

The following denotations and differential operators are utilized:

$$
\begin{gathered}
    T_{0} = t, \qquad T_{1} = \varepsilon t, \qquad T_{2} = \varepsilon^{2} t, \qquad \cdots, \\
    D_{0} = \frac{\partial}{T_{0}}, \qquad D_{1} = \frac{\partial}{T_{1}}, \qquad D_{2} = \frac{\partial}{T_{2}}, \qquad \cdots, \\
    \begin{aligned}
        \frac{d}{d t} &= \frac{\partial}{\partial T_{0}} + \varepsilon \frac{\partial}{\partial T_{1}} + \varepsilon^{2} \frac{\partial}{\partial T_{2}} + \cdots \\
        &= D_{0} + \varepsilon D_{1} + \varepsilon^{2} D_{2} + \cdots.
    \end{aligned}
\end{gathered}
$$

Expand the solution of Eq. (13) in powers of $\varepsilon$:

$$
\begin{equation}
    z (t) = \varepsilon Z_{1} (T_{0}, T_{1}, T_{2}, \cdots) + \varepsilon^{2} Z_{2} (T_{0}, T_{1}, T_{2}, \cdots) + \cdots,
\end{equation}
$$

Substituting Eq. (16) in Eq. (13) and expanding $Z_{i}$ at $(T_{0} - \tau_{c}, T_{1}, T_{2}, \cdots)$ in powers of $\varepsilon$ and considering $\varepsilon$'s 1st order, it can be obtained that

$$
\begin{equation}
    D_{0} Z_{1} (T_{0}, T_{1}, T_{2}, \cdots) + \omega Z_{1} (T_{0} - \tau_{c}, T_{1}, T_{2}, \cdots) = 0,
\end{equation}
$$

where $\omega$ is the system's frequency while $\tau$ exactly locates at the bifurcation point. The solution of Eq. (17) has the form

$$
Z_{1} (T_{0}, T_{1}, T_{2}, \cdots) = A_{11} \sin{(\omega T_{0})} + B_{11} \cos{(\omega T_{0})},
$$

where $A_{11} = A_{11} (T_{1}, T_{2}, \cdots)$ and $B_{11} = B_{11} (T_{1}, T_{2}, \cdots)$. Henceforth, the author wrote $A_{11} = A_{11} (T_{1}, T_{2}, \cdots)$ and $B_{11} = B_{11} (T_{1}, T_{2}, \cdots)$ as $A_{11}$ and $B_{11}$ for brevity respectively.

Considering $\varepsilon$'s 2nd order, it can be obtained that

$$
\begin{equation}
    \begin{gathered}
        D_{0} Z_{2} + D_{1} Z_{1} + \cdots = 0 \\
        \begin{gathered}
            \Rightarrow D_{0} Z_{2} (T_{0}, T_{1}, T_{2}, \cdots) + \omega Z_{2} (T_{0} - \tau_{c}, T_{1}, T_{2}, \cdots) + P_{21} \sin{(\omega T_{0})} + Q_{21} \cos{(\omega T_{0})} \\
            + P_{22} \sin{(2 \omega T_{0})} + Q_{22} \cos{(2 \omega T_{0})} + F_{2} = 0, \\
        \end{gathered}
    \end{gathered}
\end{equation}
$$

where $P_{2i} = P_{2i} (D_{1} A_{11}, D_{1} B_{11}, A_{11}, B_{11})$, $Q_{2i} = Q_{2i} (D_{1} A_{11}, D_{1} B_{11}, A_{11}, B_{11})$, and $F_{2} = F_{2} (A_{11}, B_{11})$. Note that $F_{2}$ appears due to the existence of quadratic nonlinearity in $f(\cdot)$.

To eliminate secular terms, coefficients of harmonic terms (namely, $P_{21}$ and $Q_{21}$) should be equal to zero. With further simplification, the following equations can be obtained:

$$
\begin{gathered}
    D_{1} A_{11} = M_{1} (A_{11}, B_{11}), \\
    D_{1} B_{11} = N_{1} (A_{11}, B_{11}).
\end{gathered}
$$

Then, the solution of Eq. (18) is

$$
Z_{2} (T_{0}, T_{1}, T_{2}, \cdots) =  C_{2} + A_{22} \sin{(2 \omega T_{0})} + B_{22} \cos{(2 \omega T_{0})},
$$

where

$$
\begin{gathered}
    A_{22} = A_{22} (A_{11}, B_{11}), \\
    B_{22} = B_{22} (A_{11}, B_{11}), \\
    C_{2} = C_{2} (A_{11}, B_{11}).
\end{gathered}
$$

The above procedure can be performed similarly to higher orders to obtain $D_{i} A_{11}$ and $D_{i} B_{11}$ in expressions of $A$ and $B$. Finally, it can be obtained that

$$
\begin{gather}
    \begin{aligned}
        \frac{d A_{11}}{d t} &= \frac{d}{d t} A_{11} \\
        &= (\varepsilon D_{1} + \varepsilon^{2} D_{2} + \cdots) A_{11} (T_{1}, T_{2}, \cdots) \\
        &= \varepsilon D_{1} A_{11} + \varepsilon^{2} D_{2} A_{11} + \cdots, \\
    \end{aligned} \\
    \begin{aligned}
        \frac{d B_{11}}{d t} &= \frac{d}{d t} B_{11} \\
        &= (\varepsilon D_{1} + \varepsilon^{2} D_{2} + \cdots) B_{11} (T_{1}, T_{2}, \cdots) \\
        &= \varepsilon D_{1} B_{11} + \varepsilon^{2} D_{2} B_{11} + \cdots.
    \end{aligned}
\end{gather}
$$

With the following transformation

$$
\left \{
    \begin{aligned}
        & A_{11} = R(t) \cos{(\varphi (t))}, \\
        & B_{11} = R(t) \sin{(\varphi (t))},
    \end{aligned}
\right.
$$

Eq. (19) and Eq. (20) in polar coordinates can be written as

$$
\begin{gather}
    \dot{R} (t) = r_{1} (\varepsilon, \tau_{\varepsilon}) R(t) + r_{3} (\varepsilon, \tau_{\varepsilon}) R(t)^{3} + r_{5} (\varepsilon, \tau_{\varepsilon}) R(t)^{5} + \cdots, \\
    \dot{\varphi} (t) = f_{0} + f_{2} (\varepsilon, \tau_{\varepsilon}) R(t)^{2} + f_{4} (\varepsilon, \tau_{\varepsilon}) R(t)^{4} + \cdots.
\end{gather}
$$
