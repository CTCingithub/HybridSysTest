<!--
 * @Author: CTC 2801320287@qq.com
 * @Date: 2024-04-11 20:56:54
 * @LastEditors: CTC 2801320287@qq.com
 * @LastEditTime: 2024-04-25 22:12:07
 * @Description: 
 * 
 * Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
-->
# MMS for Delay Systems Example 1

Define the following time scales

$$
\begin{equation*}
    T_{0} = \varepsilon t, \qquad T_{1} = \varepsilon^{2} t, \qquad T_{2} = \varepsilon^{3} t, \qquad \cdots
\end{equation*}
$$

The following denotations and differential operators are utilized:

$$
\begin{gathered}
    T_{0} = t, \qquad T_{1} = \varepsilon t, \qquad T_{2} = \varepsilon^{2} t, \qquad \cdots, \\
    D_{0} = \frac{\partial}{T_{0}}, \qquad D_{1} = \frac{\partial}{T_{1}}, \qquad D_{2} = \frac{\partial}{T_{2}}, \qquad \cdots, \\
    \begin{aligned}
        \frac{d}{d t} &= \frac{\partial}{\partial T_{0}} + \varepsilon \frac{\partial}{\partial T_{1}} + \varepsilon^{2} \frac{\partial}{\partial T_{2}} + \cdots \\
        &= D_{0} + \varepsilon D_{1} + \varepsilon^{2} D_{2} + \cdots,
    \end{aligned} \\
    \begin{aligned}
        \frac{d^{2}}{d t^{2}} &= \left( D_{0} + \varepsilon D_{1} + \varepsilon^{2} D_{2} + \cdots \right)^{2} \\
        &= D_{0}^{2} + \varepsilon \left( 2 D_{0} D_{1} \right) + \varepsilon^{2} \left( 2 D_{0} D_{2} + D_{1}^{2} \right) + \cdots.
    \end{aligned}
\end{gathered}
$$

Expand solution $x$ as

$$
x = X_0 (T_0, T_1, T_2, \cdots) + \varepsilon X_1 (T_0, T_1, T_2, \cdots) + \varepsilon^2 X_2 (T_0, T_1, T_2, \cdots) + \cdots.
$$

Then we have

$$
\begin{gathered}
    \frac{d x}{d t} = D_0 X_0 + \varepsilon \left( D_0 X_1 + D_1 X_0 \right) + \varepsilon^2 \left( D_0 X_2 + D_1 X_1 + D_2 X_0 \right) + \cdots, \\
    \begin{aligned}
        \frac{d^{2} x}{d t^{2}} &= \left( D_{0}^{2} + \varepsilon \left( 2 D_{0} D_{1} \right) + \varepsilon^{2} \left( 2 D_{0} D_{2} + D_{1}^{2} \right) + \cdots \right) \left( X_0 + \varepsilon X_1 + \varepsilon^2 X_2 + \cdots \right) \\
        &= D_{0}^{2} X_{0} + \varepsilon \left( 2 D_{0} D_{1} X_{0} + D_{0}^{2} X_{0} \right) + \varepsilon^{2} \left( 2 D_{0} D_{2} X_{0} + 2 D_{1} D_{0} X_{1} + D_{1}^{2} X_{0} \right) + \cdots.
    \end{aligned}
\end{gathered}
$$

For brevity, we have the following denotions:

$$
\begin{gathered}
    X_{id} = X_{i} \left( T_{0} - t_{d}, T_{1}, T_{2}, \cdots \right), \\
    D_{i} \cdots D_{j} X_{kd} = \left. \left[ D_{i} \cdots D_{j} X_{k} \right] \right \vert_{T_{0} - t_{d}, T_{1}, T_{2}, \cdots}.
\end{gathered}
$$

For delayed terms, there are

$$
\begin{gathered}
    \begin{aligned}
        x (t - t_{d}) &=&& X_{0} (T_{0} - t_{d}, T_{1} - \varepsilon t_{d}, T_{2} - \varepsilon^{2} t_{d}, \cdots) + \varepsilon X_{1} (T_{0} - t_{d}, T_{1} - \varepsilon t_{d}, T_{2} - \varepsilon^{2} t_{d}, \cdots) \\
        &&& + \varepsilon^2 X_{2} (T_{0} - t_{d}, T_{1} - \varepsilon t_{d}, T_{2} - \varepsilon^{2} t_{d}, \cdots) \\
        &=&& X_{0d} - \varepsilon t_{d} \frac{\partial X_{0d}}{\partial T_{1}} - \varepsilon^{2} t_{d} \frac{\partial X_{0d}}{\partial T_{2}} + \varepsilon X_{1d} - \varepsilon^{2} t_{d} \frac{\partial X_{1d}}{\partial T_{1}} - \varepsilon^{3} t_{d} \frac{\partial X_{1d}}{\partial T_{2}} \\
        &&& + \varepsilon^2 X_{2} \left( T_{0} - t_{d}, T_{1}, T_{2} \right) - \varepsilon^{3} t_{d} \frac{\partial X_{2d}}{\partial T_{1}} - \varepsilon^{4} t_{d} \frac{\partial X_{2d}}{\partial T_{2}} + \cdots \\
        &=&& X_{0d} + \varepsilon \left( X_{1d} - t_{d} D_{1} X_{0d} \right) + \varepsilon^{2} \left( X_{2d} - t_{d} D_{2} X_{0d} - t_{d} D_{1} X_{1d} \right) + \cdots, \\
    \end{aligned} \\
    \begin{aligned}
        \frac{d x}{d t} (t - t_{d}) &=&& \left. \left[ D_0 X_0 + \varepsilon \left( D_0 X_1 + D_1 X_0 \right) + \varepsilon^2 \left( D_0 X_2 + D_1 X_1 + D_2 X_0 \right) \right] \right \vert_{t - t_{d}} + \cdots \\
        &=&& \left[ D_{0} X_{0} \right]_{(T_{0} - t_{d}, T_{1} - \varepsilon t_{d}, T_{2} - \varepsilon^{2} t_{d}, \cdots)} \\
        &&& + \varepsilon \left( \left[ D_{0} X_{1} \right]_{(T_{0} - t_{d}, T_{1} - \varepsilon t_{d}, T_{2} - \varepsilon^{2} t_{d}, \cdots)} + \left[ D_{1} X_{0} \right]_{(T_{0} - t_{d}, T_{1} - \varepsilon t_{d}, T_{2} - \varepsilon^{2} t_{d}, \cdots)} \right) \\
        &&& + \varepsilon^{2} \left( \left[ D_{0} X_{2} \right]_{(T_{0} - t_{d}, T_{1} - \varepsilon t_{d}, T_{2} - \varepsilon^{2} t_{d}, \cdots)} + \left[ D_{1} X_{1} \right]_{(T_{0} - t_{d}, T_{1} - \varepsilon t_{d}, T_{2} - \varepsilon^{2} t_{d}, \cdots)} \right. \\
        &&& \left. + \left[ D_{2} X_{0} \right]_{(T_{0} - t_{d}, T_{1} - \varepsilon t_{d}, T_{2} - \varepsilon^{2} t_{d}, \cdots)} \right) + \cdots \\
        &=&& \left( D_{0} X_{0d} - \varepsilon t_{d} D_{0} D_{1} X_{0d} - \varepsilon^{2} t_{d} D_{0} D_{2} X_{0d} + \cdots \right) \\
        &&& + \varepsilon \left( \left( D_{0} X_{1d} - \varepsilon t_{d} D_{0} D_{1} X_{1d} \right) + \left( D_{1} X_{0d} - \varepsilon t_{d} D_{1}^{2} X_{0d} \right) + \cdots \right) \\
        &&& + \varepsilon^{2} \left( D_{0} X_{2d} + D_{1} X_{1d} + D_{2} X_{0d} + \cdots \right) + \cdots \\
        &=&& D_{0} X_{0d} + \varepsilon \left( D_{0} X_{1d} + D_{1} X_{0d} - t_{d} D_{0} D_{1} X_{0d} \right) \\
        &&& + \varepsilon^{2} \left[ D_{0} X_{2d} + D_{1} X_{1d} + D_{2} X_{0d} \right. \\
        &&& \left. - t_{d} \left( D_{0} D_{2} X_{0d} + D_{1}^{2} X_{1d} + D_{0} D_{1} X_{1d} \right) \right] + \cdots.
    \end{aligned}
\end{gathered}
$$

In a nutshell, the following 5 equations are widely used in MMS perturbation procedure for delay systems:

$$
\begin{gather}
    x = X_{0} + \varepsilon X_{1} + \varepsilon^{2} X_{2} + \cdots, \\
    \frac{d x}{d t} = D_0 X_0 + \varepsilon \left( D_0 X_1 + D_1 X_0 \right) + \varepsilon^2 \left( D_0 X_2 + D_1 X_1 + D_2 X_0 \right) + \cdots, \\
    \frac{d^{2} x}{d t^{2}} = D_{0}^{2} X_{0} + \varepsilon \left( 2 D_{0} D_{1} X_{0} + D_{0}^{2} X_{0} \right) + \varepsilon^{2} \left( 2 D_{0} D_{2} X_{0} + 2 D_{1} D_{0} X_{1} + D_{1}^{2} X_{0} \right) + \cdots, \\
    x (t - t_{d}) = X_{0d} + \varepsilon \left( X_{1d} - t_{d} D_{1} X_{0d} \right) + \varepsilon^{2} \left( X_{2d} - t_{d} D_{2} X_{0d} - t_{d} D_{1} X_{1d} \right) + \cdots, \\
    \begin{aligned}
        \frac{d x}{d t} (t - t_{d}) &=&& D_{0} X_{0d} + \varepsilon \left( D_{0} X_{1d} + D_{1} X_{0d} - t_{d} D_{0} D_{1} X_{0d} \right) + \varepsilon^{2} \left[ D_{0} X_{2d} + D_{1} X_{1d} \right. \\
        &&& + D_{2} X_{0d} \left. - t_{d} \left( D_{0} D_{2} X_{0d} + D_{1}^{2} X_{1d} + D_{0} D_{1} X_{1d} \right) \right] + \cdots.
    \end{aligned}
\end{gather}
$$

Consider the equation

$$
\begin{equation}
    \dot{x} (t) = - x \left( t - \frac{\pi}{2} \right) - \varepsilon \left[ x \left( t - \frac{\pi}{2} \right) + x^{3} (t) \right].
\end{equation}
$$

For the equation above, a Hopf bifurcation occurs at $\varepsilon = 0$ and a stable periodic solution exists for small $\varepsilon > 0$.

With Eq. (1)-(5), and truncate $\varepsilon$ to 1st order and $t$ to $T_{1}$, it can be obtained that

$$
\begin{equation}
    \begin{gathered}
        D_{0} X_{0} + \varepsilon \left( D_{0} X_{1} + D_{1} X_{0} \right) = - \left( X_{0d} + \varepsilon \left( X_{1d} - \frac{\pi}{2} D_{1} X_{0d} \right) \right) - \varepsilon \left( X_{0d} + X_{0}^{3} \right) + \cdots \\
        \Rightarrow \left( D_{0} X_{0} + X_{0d} \right) + \varepsilon \left( D_{0} X_{1} + X_{1d} + D_{1} X_{0} + X_{0d} - \frac{\pi}{2} D_{1} X_{0d} + X_{0}^{3} \right) = 0.
    \end{gathered}
\end{equation}
$$

For $\varepsilon$'s 0th order, it can be obtained that

$$
\begin{equation}
    \frac{\partial X_{0}}{\partial T_{0}} + X_{0d} = 0,
\end{equation}
$$

whose solution has the following form

$$
\begin{equation}
    X_{0} = A(T_{1}) \sin{(T_{0})} + B(T_{1}) \cos{(T_{0})}.
\end{equation}
$$

For $\varepsilon$'s 1st order, it can be obtained that

$$
\begin{equation*}
    \frac{\partial X_{1}}{\partial T_{0}} + X_{1d} + D_{1} X_{0} + X_{0d} - \frac{\pi}{2} D_{1} X_{0d} + X_{0}^{3} = 0,
\end{equation*}
$$

which can be simplified as

$$
\begin{equation}
    \frac{\partial X_{1}}{\partial T_{0}} + X_{1d} + P_{1} \sin{(T_{0})} + P_{2} \cos{(T_{0})} + P_{3} \sin{(3 T_{0})} + P_{4} \cos{(3 T_{0})} = 0,
\end{equation}
$$

where

$$
\begin{aligned}
    & P_{1} = D_{1} A - \frac{\pi}{2} D_{1} B + \frac{3}{4} A^{3} + \frac{3}{4} A B^{2} + B, \\
    & P_{2} = \frac{\pi}{2} D_{1} A + D_{1} B - A + \frac{3}{4} A^{2} B + \frac{3}{4} B^{3}, \\
    & P_{3} =  - \frac{1}{4} A^{3} + \frac{3}{4} A B^{2}, \\
    & P_{4} = - \frac{3}{4} A^{2} B + \frac{1}{4} B^{3}.
\end{aligned}
$$

To eliminate secular terms, $P_{1}$ and $P_{2}$ should be equal to zero, yielding:

$$
\begin{gather}
    D_{1} A = -\frac{3 A^3}{4+\pi ^2}-\frac{3 \pi  A^2 B}{2 \left(4+\pi
   ^2\right)}-\frac{3 A B^2}{4+\pi ^2}+\frac{2 \pi  A}{4+\pi
   ^2}-\frac{3 \pi  B^3}{2 \left(4+\pi ^2\right)}-\frac{4
   B}{4+\pi ^2}, \\
   D_{1} B = \frac{3 \pi  A^3}{2 \left(4+\pi ^2\right)}-\frac{3 A^2 B}{4+\pi
   ^2}+\frac{3 \pi  A B^2}{2 \left(4+\pi ^2\right)}+\frac{4
   A}{4+\pi ^2}-\frac{3 B^3}{4+\pi ^2}+\frac{2 \pi  B}{4+\pi ^2}.
\end{gather}
$$

Then $A$'s and $B$'s derivative to $t$ are:

$$
\begin{gather}
    \frac{d A}{d t} = (D_{0} + \varepsilon D_{1}) A (T_{1}) + \mathcal{O} (\varepsilon^{2}) = \varepsilon D_{1} A + \mathcal{O} (\varepsilon^{2}), \\
    \frac{d B}{d t} = (D_{0} + \varepsilon D_{1}) B (T_{1}) + \mathcal{O} (\varepsilon^{2}) = \varepsilon D_{1} B + \mathcal{O} (\varepsilon^{2}).
\end{gather}
$$

Change variables in the two equations above to polar coordinates, the transformation equations are:

$$
A (t) = R (t) \cos{(\varphi (t))}, \qquad B (t) = R (t) \sin{(\varphi (t))}.
$$

Therefore, it's easy to obtain that

$$
\begin{gather}
    \begin{aligned}
        \frac{d R}{d t} &= \frac{d A}{d t} \cos{(\varphi)} + \frac{d B}{d t} \sin{(\varphi)} \\
        &= \varepsilon \frac{2 \pi R - 3 R^{3}}{4 + \pi^{2}} + \mathcal{O} (\varepsilon^{2}) ,
    \end{aligned} \\
    \begin{aligned}
        \frac{d \varphi}{d t} &= - \frac{d A}{d t} \frac{\sin{(\varphi)}}{R} + \frac{d B}{d t} \frac{\cos{(\varphi)}}{R} \\
        &= \varepsilon \frac{8 + 3 \pi R^{2}}{2 (4 + \pi^{2})}.
    \end{aligned}
\end{gather}
$$

I detailed the author's process of proof to $\varepsilon^{1}$ and $T_{1}$. If one furthers the above process to $\varepsilon^{2}$ and $T_{2}$, the numericaol results of Eq. (15) would match that of Eq. (6) well.
