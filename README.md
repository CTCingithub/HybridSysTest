<!--
 * @Author: CTC 2801320287@qq.com
 * @Date: 2024-03-26 10:56:14
 * @LastEditors: CTC 2801320287@qq.com
 * @LastEditTime: 2024-04-25 23:11:34
 * @Description: 
 * 
 * Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
-->
# Continuous-time Approximation of Digital Sampling Systems

## 1. Description

Numerical simulation on systems with digital input, and their surrogate time-varying delay systems.

Mechanical systems with control input obtained from digital signals often have the following dynamics:

$$
\begin{equation}
    M (\vec{q}) \ddot{\vec{q}} + C (\vec{q}, \dot{\vec{q}}) \vec{q} + G (\vec{q}) + f (\dot{\vec{q}}) = \tau \left( \dot{\vec{q}} \left( (k-1) t_{s} \right), \vec{q} \left( (k-1) t_{s} \right) \right).
\end{equation}
$$

when $t \in [k t_{s}, (k+1) t_{s})$.

Eq. (1) can be handled as a DDE

$$
\begin{equation}
    M (\vec{q}) \ddot{\vec{q}} + C (\vec{q}, \dot{\vec{q}}) \vec{q} + G (\vec{q}) + f (\dot{\vec{q}}) = \tau \left( \dot{\vec{q}} \left( t - t_{d} \right), \vec{q} \left( t - t_{d} \right) \right),
\end{equation}
$$

where the delay $t_{d}$ is a sawtooth wave function of time $t$:

$$
\begin{equation}
    t_{d} = t - t_{s} \left( \left \lfloor \frac{t}{t_{s}} \right \rfloor - 1 \right).
\end{equation}
$$

The sawtooth-wave delay $t_{d}$ can be written in Fourier series form:

$$
\begin{equation}
    t_{d} (t, t_{s}) = t_{s} \left( \frac{3}{2} - \frac{1}{\pi} \sum_{n = 1}^{\infty} \frac{1}{n} \sin{\left( \frac{2 n \pi t}{t_{s}} \right)} \right).
\end{equation}
$$

## 2. MMS for Delayed Systems

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
        &= D_{0}^{2} X_{0} + \varepsilon \left( 2 D_{0} D_{1} X_{0} + D_{0}^{2} X_{1} \right) + \varepsilon^{2} \left( 2 D_{0} D_{2} X_{0} + 2 D_{1} D_{0} X_{1} + D_{1}^{2} X_{0} \right) + \cdots.
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
    \frac{d^{2} x}{d t^{2}} = D_{0}^{2} X_{0} + \varepsilon \left( 2 D_{0} D_{1} X_{0} + D_{0}^{2} X_{1} \right) + \varepsilon^{2} \left( 2 D_{0} D_{2} X_{0} + 2 D_{1} D_{0} X_{1} + D_{1}^{2} X_{0} \right) + \cdots, \\
    x (t - t_{d}) = X_{0d} + \varepsilon \left( X_{1d} - t_{d} D_{1} X_{0d} \right) + \varepsilon^{2} \left( X_{2d} - t_{d} D_{2} X_{0d} - t_{d} D_{1} X_{1d} \right) + \cdots, \\
    \begin{aligned}
        \frac{d x}{d t} (t - t_{d}) &=&& D_{0} X_{0d} + \varepsilon \left( D_{0} X_{1d} + D_{1} X_{0d} - t_{d} D_{0} D_{1} X_{0d} \right) + \varepsilon^{2} \left[ D_{0} X_{2d} + D_{1} X_{1d} \right. \\
        &&& + D_{2} X_{0d} \left. - t_{d} \left( D_{0} D_{2} X_{0d} + D_{1}^{2} X_{1d} + D_{0} D_{1} X_{1d} \right) \right] + \cdots.
    \end{aligned}
\end{gather}
$$
