<!--
 * @Author: CTC 2801320287@qq.com
 * @Date: 2024-04-11 20:56:54
 * @LastEditors: CTC 2801320287@qq.com
 * @LastEditTime: 2024-04-13 18:14:36
 * @Description: 
 * 
 * Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
-->
# MMS for Delay Systems Example 1

Consider the equation

$$
\begin{equation}
    \dot{x} (t) = - \alpha x \left( t - \frac{\pi}{2} \right) - \varepsilon \left[ x \left( t - \frac{\pi}{2} \right) + x^{3} (t) \right].
\end{equation}
$$

For the equation above, a Hopf bifurcation occurs at $\varepsilon = 0$ and a stable periodic solution exists for small $\varepsilon > 0$.

For $\varepsilon = 0$, Eq.(1) is linear, the solution is an infinite linear combination of terms of the form $e^{\lambda t}$. Of these $\lambda$s, two are $\pm i$, while all others have negative real parts. Therefor, when after transients die out exponentially fast, we're left with

$$
\begin{equation}
    x (t) = A \sin{(t)} + B \cos{(t)},
\end{equation}
$$

where $A$ and $B$ are constants. In what follows, Eq.(2) is treated as the complementary solution to Eq.(1) with $\varepsilon = 0$. In this way, we will implicitly remove all the exponentially decaying parts of the solution, and an explicit center manifold calculation will be unnecessary.

Define the following time scales

$$
\begin{equation*}
    T_{0} = \varepsilon t, \qquad T_{1} = \varepsilon^{2} t, \qquad T_{2} = \varepsilon^{3} t, \qquad \cdots
\end{equation*}
$$

Define the following operators:

$$
\begin{aligned}
    D = \frac{\partial}{\partial t}, \qquad D_{0} = \frac{\partial}{\partial T_{0}}, \qquad D_{1} = \frac{\partial}{\partial T_{1}}, \qquad D_{2} = \frac{\partial}{\partial T_{2}}, \qquad \cdots \\
    D^{2} = \frac{\partial^{2}}{\partial t^{2}}, \qquad D_{0}^{2} = \frac{\partial^{2}}{\partial T_{0}^{2}}, \qquad D_{1}^{2} = \frac{\partial^{2}}{\partial T_{1}^{2}}, \qquad D_{2}^{2} = \frac{\partial^{2}}{\partial T_{2}^{2}}, \qquad \cdots
\end{aligned}
$$

Then we have

$$
\begin{equation}
    \begin{aligned}
        \frac{\partial}{\partial t} &= \frac{\partial}{\partial t} + \frac{\partial}{\partial T_{0}} \frac{\partial T_{0}}{\partial t} + \frac{\partial}{\partial T_{1}} \frac{\partial T_{1}}{\partial t} + \frac{\partial}{\partial T_{2}} \frac{\partial T_{2}}{\partial t} + \cdots \\
        &= D + \varepsilon D_{0} + \varepsilon^{2} D_{1} + \varepsilon^{3} D_{2} + \cdots,
    \end{aligned}
\end{equation}
$$

and

$$
\begin{equation}
    \begin{aligned}
        \frac{\partial^{2}}{\partial t^{2}} &= \left( D + \varepsilon D_{0} + \varepsilon^{2} D_{1} + \varepsilon^{3} D_{2} + \cdots \right)^{2} \\
        &= D^{2} + \varepsilon \left( 2 D D_{0} \right) + \varepsilon^{2} \left( 2 D D_{1} + D_{0}^{2} \right) + \varepsilon^{3} \left( 2 D D_{2} + 2 D_{0} D_{1} \right) + \cdots.
    \end{aligned}
\end{equation}
$$

The solution to Eq.(1) is assumed to be of the follow form(truncated to 2nd order):

$$
\begin{equation}
    \begin{aligned}
        x (t) &= X (t, T_{0}, T_{1}, T_{2}) \\
        &= X_{0} (t, T_{0}, T_{1}, T_{2}) + \varepsilon X_{1} (t, T_{0}, T_{1}, T_{2}) + \varepsilon^{2} X_{2} (t, T_{0}, T_{1}, T_{2})
    \end{aligned}
\end{equation}
$$

===============================
Temp

$$
\begin{aligned}
    \dot{x} (t) &=&& \left( D + \varepsilon D_{0} + \varepsilon^{2} D_{1} + \varepsilon^{3} D_{2} \right) \left( X_{0} + \varepsilon X_{1} + \varepsilon^{2} X_{2} \right) \\
    &=&& D X_{0} + \varepsilon \left( D X_{1} + D_{0} X_{0} \right) + \varepsilon^{2} \left( D X_{2} + D_{0} X_{1} + D_{1} X_{0} \right) \\
    &&& + \varepsilon^{3} \left( D_{0} X_{2} + D_{1} X_{1} + D_{2} X_{0} \right) + \cdots
\end{aligned}
$$

$$
\begin{aligned}
    x (t - \tau) &= X_{0} \left( t - \tau, T_{0}, T_{1}, T_{2} \right) + \varepsilon X_{1} \left( t - \tau, T_{0}, T_{1}, T_{2} \right) + \varepsilon^{2} X_{2} \left( t - \tau, T_{0}, T_{1}, T_{2} \right) \\
    &= X_{0d} + \varepsilon X_{1d} + \varepsilon^{2} X_{2d}
\end{aligned}
$$

===============================

With Eq.(3)(4)(5), it can be obtained from Eq.(1) that

$$
\begin{equation}
    \begin{aligned}
        \frac{\partial}{\partial t} \left( X_{0} + \varepsilon X_{1} + \varepsilon^{2} X_{2} \right) &=&& - (1 + \varepsilon) \left( X_{0} \left( t - \frac{\pi}{2} \right) + \varepsilon X_{1} \left( t - \frac{\pi}{2} \right) + \varepsilon^{2} X_{2} \left( t - \frac{\pi}{2} \right) \right) \\
        &&& - \varepsilon \left( X_{0} + \varepsilon X_{1} + \varepsilon^{2} X_{2} \right)^{3} \\
        &=&& - X_{0d} + \varepsilon \left( - X_{0}^{3} - X_{0d} - X_{1d} \right) + \varepsilon^{2} \left( - 3 X_{0}^{2} X_{1} - X_{1d} - X_{2d} \right) \\
        &&& + \varepsilon^{3} \left( - 3 X_{0} X_{1}^{2} - 3 X_{0}^{2} X_{2} - X_{2d} \right) + \cdots
    \end{aligned}
\end{equation}
$$

The left-hand side can be rewritten as:

$$
\begin{equation}
    \begin{aligned}
        \frac{\partial}{\partial t} \left( X_{0} + \varepsilon X_{1} + \varepsilon^{2} X_{2} \right) &=&& \left( \frac{\partial}{\partial t} + \varepsilon D_{0} + \varepsilon^{2} D_{1} + \varepsilon^{3} D_{2} \right) \left( X_{0} + \varepsilon X_{1} + \varepsilon^{2} X_{2} \right) \\
        &=&& D X_{0} + \varepsilon \left( D X_{1} + D_{0} X_{0} \right) + \varepsilon^{2} \left( D X_{2} + D_{0} X_{1} + D_{1} X_{0} \right) \\
        &&& + \varepsilon^{3} \left( D_{0} X_{2} + D_{1} X_{1} + D_{2} X_{0} \right) + \cdots
    \end{aligned}
\end{equation}
$$

For $\varepsilon$'s 0th order, we obtain

$$
\begin{equation}
    \begin{aligned}
        D X_{0} &= - X_{0} \left( t - \frac{\pi}{2} \right) \\
        X_{0} (t) &= A \sin{(t)} + B \cos{(t)},
    \end{aligned}
\end{equation}
$$

where $A = A(T_{0}, T_{1}, T_{2})$ and $B = B(T_{0}, T_{1}, T_{2})$ are dependent on time scale $T_{0}$, $T_{1}$, $T_{2}$, $\cdots$.

For $\varepsilon$'s 1st order, we obtain

$$
\begin{equation}
    \begin{aligned}
        D X_{1} + D_{0} X_{0} &= - X_{0}^{3} - X_{0d} - X_{1d} \\
        D X_{1} + X_{1d} &= P_{1} \sin{(t)} + P_{2} \cos{(t)} + P_{3} \sin{(3 t)} + P_{4} \cos{(3 t)},
    \end{aligned}
\end{equation}
$$

where

$$
\begin{equation}
    \left \{ \begin{aligned}
        & P_{1} = - \frac{3}{4} A^{3} - B - \frac{3}{4} A B^{2}, \\
        & P_{2} = A - \frac{3}{4} A^{2} B - \frac{3}{4} B^{3}, \\
        & P_{3} = \frac{1}{4} A^{3} - \frac{3}{4} A B^{2}, \\
        & P_{4} = \frac{3}{4} A^{2} B - \frac{3}{4} B^{3}.
    \end{aligned} \right.
\end{equation}
$$
