<!--
 * @Author: CTC 2801320287@qq.com
 * @Date: 2024-04-15 22:12:16
 * @LastEditors: CTC 2801320287@qq.com
 * @LastEditTime: 2024-05-06 17:11:27
 * @Description: 
 * 
 * Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
-->
# MMS for Linear System with Time-varyingly Delayed Feedback

**Wrong!**

## 1. Description

The equation of the delay system studied is:

$$
\begin{equation}
    \ddot{x} (t) = - P x (t - t_{d}) - D \dot{x} (t - t_{d}),
\end{equation}
$$

where the sawtooth-wave delay $t_{d}$ can be written in Fourier series form:

$$
\begin{equation}
    t_{d} (t, t_{s}) = t_{s} \left( \frac{3}{2} - \frac{1}{\pi} \sum_{n = 1}^{\infty} \frac{1}{n} \sin{\left( \frac{2 n \pi t}{t_{s}} \right)} \right).
\end{equation}
$$

If the delay is time-constant, the characteristic equation of the delay system at trivial equilibrium is:

$$
\begin{equation}
    \lambda^{2} + P e^{- \lambda t_{d}} + D \lambda e^{- \lambda t_{d}} = 0.
\end{equation}
$$

The eigenvalue $\lambda$ on the critical boundary of stability should be purely imaginary pairs or zero. We'll study Hopf bifurcation cases where $\lambda = \pm i \omega$. Substitute $\lambda = i \omega$ in Eq. (3) yields the critical boundary of stability zone:

$$
\begin{gather}
    P \cos{(\omega t_{d})} - D \omega \sin{(\omega t_{d})} = \omega^{2}, \\
    P \sin{(\omega t_{d})} - D \omega \cos(\omega t_{d}) = 0.
\end{gather}
$$

Eq. (4) and (5) remain holded if substitute $\omega$ with $- \omega$. Thus, Eq. (4) and (5) describe the stability boundary for Hopf bifurcation cases.

We can obtain analytical solutions of Eq. (4) and (5) if $P = 0$ or $D = 0$.

If $P = 0$, then

$$
\begin{gathered}
    \omega = - \frac{\pi}{2 t_{d}} + 2 k \frac{\pi}{t_{d}}, \qquad k \in \mathbb{Z}^{+}, \\
    D = \omega = - \frac{\pi}{2 t_{d}} + 2 k \frac{\pi}{t_{d}}, \qquad k \in \mathbb{Z}^{+}.
\end{gathered}
$$

If $D = 0$, then

$$
\begin{gathered}
    \omega = \frac{2 k \pi}{t_{d}}, \qquad k \in \mathbb{Z}^{+}, \\
    P = \omega^{2} = \frac{4 k^{2} \pi^{2}}{t_{d}^{2}}, \qquad k \in \mathbb{Z}^{+}.
\end{gathered}
$$

## 2. Solution with MMS

The following 5 general equations are going to be used in following MMS perturbation procedure for delay systems. See `README.md` for details.

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

Define

$$
\begin{equation}
    \tau = 2 \pi \frac{t}{t_{s}},
\end{equation}
$$

and

$$
y (\tau) = x(t).
$$

The velocity gain $D$ is assumed to be $\mathcal{O} (\varepsilon)$-scaled, and is substituted with $\varepsilon D$ in following analysis to emphasize it. Then Eq.(1) can be written as:

$$
\left( \frac{2 \pi}{t_{s}} \right)^{2} \frac{d^{2} y}{d \tau^{2}} (\tau)= - P y (\tau - \tau_{d}) - \varepsilon D \left( \frac{2 \pi}{t_{s}} \right) \frac{d y}{d \tau} (\tau - \tau_{d}),
$$

which yields dynamics under time scale $\tau$:

$$
\begin{equation}
    \frac{d^{2} y}{d \tau^{2}} (\tau)= - \omega_{0}^{2} y (\tau - \tau_{d}) - \varepsilon d \frac{d y}{d \tau} (\tau - \tau_{d}),
\end{equation}
$$

where

$$
\begin{gather}
    \omega_{0}^{2} = \frac{t_{s}^{2}}{4 \pi^{2}} P, \\
    d = \frac{t_{s}}{2 \pi} D.
\end{gather}
$$

With Eq. (3)-(7), and truncate $y$ to $\varepsilon$'s 2nd order, $t$ to $T_{2} = \varepsilon^{2} \tau$, we have:

$$
\begin{equation}
    \begin{aligned}
        & D_{0}^{2} Y_{0} + \varepsilon \left( 2 D_{0} D_{1} Y_{0} + D_{0}^{2} Y_{1} \right) + \varepsilon^{2} \left( 2 D_{0} D_{2} Y_{0} + 2 D_{1} D_{0} Y_{1} + D_{1}^{2} Y_{0} \right) = \\
        & - \omega_{0}^{2} Y_{0d} - \varepsilon \omega_{0}^{2} \left( Y_{1d} - t_{d} D_{1} Y_{0d} \right) - \varepsilon^{2} \omega_{0}^{2} \left( Y_{2d} - t_{d} D_{2} Y_{0d} - t_{d} D_{1} Y_{1d} \right) \\
        & - \varepsilon D_{0} Y_{0d} - \varepsilon^{2} \left( D_{0} Y_{1d} + D_{1} Y_{0d} - t_{d} D_{0} D_{1} Y_{0d} \right) + \mathcal{O} (\varepsilon^{3}).
    \end{aligned}
\end{equation}
$$

For $\varepsilon$'s 0th order, Eq. (12) yields:

$$
\begin{equation}
    D_{0}^{2} Y_{0} + \omega_{0}^{2} Y_{0d} = 0,
\end{equation}
$$

whose solution is:

$$
Y_{0} = A (T_{1}, T_{2}) \sin{(\omega_{0} T_{0})} + B (T_{1}, T_{2}) \cos{(\omega_{0} T_{0})},
$$

For $\varepsilon$'s 1st order, Eq. (12) yields:

$$
\begin{equation}
    \begin{gathered}
        2 D_{0} D_{1} Y_{0} + D_{0}^{2} Y_{1} + \omega_{0}^{2} \left( Y_{1d} - t_{d} D_{1} Y_{0d} \right) + D_{0} Y_{0d} = 0 \\
        \Rightarrow D_{0}^{2} Y_{1} + \omega_{0}^{2} Y_{1d} + \bigg( D_{0} Y_{0d} - \omega_{0}^{2} t_{d} D_{1} Y_{0d} + 2 D_{0} D_{1} Y_{0} \bigg) = 0.
    \end{gathered}
\end{equation}
$$
