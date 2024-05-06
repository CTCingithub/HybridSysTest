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

## 2. Suggorate Constant-Delay System

The velocity gain $D$ is assumed to be $\mathcal{O} (\varepsilon)$-scaled, and is substituted with $\varepsilon D$ in following analysis to emphasize it.

The time-varying delay in Eq. (2)'s $k$th-order approximation is shown below, which is separated to two parts:

$$
\begin{equation}
    t_{d} = \frac{3}{2} t_{s} - \varepsilon F_{k} (t),
\end{equation}
$$

where

$$
\begin{equation}
    F_{k} (t) = \frac{1}{\varepsilon \pi} t_{s} \sum_{n = 1}^{k} \frac{1}{n} \sin{\left( \frac{2 n \pi t}{t_{s}} \right)}.
\end{equation}
$$

Then

$$
\begin{gather}
    \begin{aligned}
        x (t - t_{d}) &= x \left( t - \frac{3}{2} t_{s} - \varepsilon F_{k} (t) \right) \\
        &= x \left( t - \frac{3}{2} t_{s} \right) - \varepsilon F_{k} (t) \dot{x} \left( t - \frac{3}{2} t_{s} \right) - \frac{1}{2} \varepsilon^{2} F_{k}^{2} (t) \ddot{x} \left( t - \frac{3}{2} t_{s} \right) + \mathcal{O} (\varepsilon^{3}), \\
    \end{aligned} \\
    \begin{aligned}
        \dot{x} (t - t_{d}) &= \dot{x} \left( t - \frac{3}{2} t_{s} - \varepsilon F_{k} (t) \right) \\
        &= \dot{x} \left( t - \frac{3}{2} t_{s} \right) - \varepsilon F_{k} (t) \ddot{x} \left( t - \frac{3}{2} t_{s} \right) + \mathcal{O} (\varepsilon^{2}). \\
    \end{aligned}
\end{gather}
$$

By substituting $t$ with $t - \frac{3}{2} t_{s}$ in Eq. (1), it can be obtained that

$$
\begin{equation}
    \begin{aligned}
        \ddot{x} \left( t - \frac{3}{2} t_{s} \right) &=&& - P x \left( t - 3 t_{s} - \varepsilon F_{k} (t) \right) - \varepsilon D \dot{x} \left( t - 3 t_{s} - \varepsilon F_{k} (t) \right) \\
        &=&& - P \left[ x (t - 3 t_{s}) - \varepsilon F_{k} (t) \dot{x} \left( t - 3 t_{s} \right) + \mathcal{O} (\varepsilon^{2}) \right] \\
        &&& - \varepsilon D \left[ \dot{x} (t - 3 t_{s}) + \mathcal{O} (\varepsilon^{1}) \right] \\
        &=&& - P x (t - 3 t_{s}) + \varepsilon \bigg( P F_{k} (t) - D \bigg) \dot{x} (t - 3 t_{s}) + \mathcal{O} (\varepsilon^{2}), \\
    \end{aligned}
\end{equation}
$$

yielding

$$
\begin{gather}
    \begin{aligned}
        x \left( t - \frac{3}{2} t_{s} - \varepsilon F_{k} (t) \right) &= x \left( t - \frac{3}{2} t_{s} \right) - \varepsilon F_{k} (t) \dot{x} \left( t - \frac{3}{2} t_{s} \right) - \frac{1}{2} \varepsilon^{2} F_{k}^{2} (t) \ddot{x} \left( t - \frac{3}{2} t_{s} \right) + \mathcal{O} (\varepsilon^{3}) \\
        &= x \left( t - \frac{3}{2} t_{s} \right) - \varepsilon F_{k} (t) \dot{x} \left( t - \frac{3}{2} t_{s} \right) + \varepsilon^{2} \frac{P}{2} F_{k}^{2} (t) x (t - 3 t_{s}) + \mathcal{O} (\varepsilon^{3}), \\
    \end{aligned} \\
    \begin{aligned}
        \dot{x} \left( t - \frac{3}{2} t_{s} - \varepsilon F_{k} (t) \right) &= \dot{x} \left( t - \frac{3}{2} t_{s} \right) - \varepsilon F_{k} (t) \ddot{x} \left( t - \frac{3}{2} t_{s} \right) + \mathcal{O} (\varepsilon^{2}) \\
        &= \dot{x} \left( t - \frac{3}{2} t_{s} \right) + \varepsilon P F_{k} (t) x (t - 3 t_{s}) + \mathcal{O} (\varepsilon^{2}).
    \end{aligned}
\end{gather}
$$

With Eq. (11) and (12), the delayed system's dynamics can be rewritten as:

$$
\begin{gathered}
    \begin{aligned}
        \ddot{x} (t) &=&& - P x \left( t - \frac{3}{2} t_{s} - \varepsilon F_{k} (t) \right) - \varepsilon D \dot{x} \left( t - \frac{3}{2} t_{s} - \varepsilon F_{k} (t) \right) \\
        &=&& - P x \left( t - \frac{3}{2} t_{s} \right) + \varepsilon \left[ P F_{k} (t) \dot{x} \left( t - \frac{3}{2} t_{s} \right) - D \dot{x} \left( t - \frac{3}{2} t_{s} \right) \right] \\
        &&& - \varepsilon^{2} \bigg[ \frac{P^{2}}{2} F_{k}^{2} (t) x (t - 3 t_{s}) + P D F_{k} (t) x (t - 3 t_{s}) \bigg] + \mathcal{O} (\varepsilon^{3}),
    \end{aligned}
\end{gathered}
$$

which can be simplified as

$$
\begin{equation}
    \begin{aligned}
        \ddot{x} (t) &=&& - P x \left( t - \frac{3}{2} t_{s} \right) + \varepsilon \left[ P F_{k} (t) - D \right] \dot{x} \left( t - \frac{3}{2} t_{s} \right) \\
        &&& - \varepsilon^{2} \frac{P}{2} \left[ P F_{k}^{2} (t) + 2 D F_{k} (t) \right] x (t - 3 t_{s}) + \mathcal{O} (\varepsilon^{3}).
    \end{aligned}
\end{equation}
$$

Denote new time scale

$$
\omega_{s} = \frac{2 \pi}{t _{s}}, \qquad \tau = \frac{2 \pi}{t_{s}} t= \omega_{s} t,
$$

and

$$
y (\tau) = x(t).
$$

There are

$$
\begin{gathered}
    \begin{aligned}
        x \left( t - \frac{3}{2} t_{s} \right) &= y \left( \tau - \frac{2 \pi}{t_{s}} \frac{3 t_{s}}{2} \right) \\
        &= y \left( \tau - 3 \pi \right),
    \end{aligned} \qquad \qquad \qquad
    \begin{aligned}
        \frac{d x}{d t} (t) &= \left( \frac{d}{d \tau} \frac{\partial \tau}{\partial t} \right) y (t) \\
        &= \omega_{s}  \frac{d y}{d \tau} (\tau),
    \end{aligned} \\
    \begin{aligned}
        \frac{d^{2} x}{d t^{2}} (t) &= \left( \frac{d}{d \tau} \frac{\partial \tau}{\partial t} \right)^{2} y (t) \\
        &= \omega_{s}^{2} \frac{d^{2} y}{d \tau^{2}} (\tau),
    \end{aligned} \qquad \qquad \qquad
    \frac{d x}{d t} \left( t - \frac{3}{2} t_{s} \right) = \omega_{s}  \frac{d y}{d \tau} (\tau - 3 \pi), \\
    \begin{aligned}
        F_{k} (t) &= \frac{1}{\varepsilon \pi} t_{s} \sum_{n = 1}^{k} \frac{1}{n} \sin{\left( \frac{2 n \pi t}{t_{s}} \right)} \\
        &= \frac{1}{\varepsilon \pi} t_{s} \sum_{n = 1}^{k} \frac{1}{n} \sin{\left( n \tau \right)} \\
        &= t_{s} f_{k} (\tau),
    \end{aligned}
\end{gathered}
$$

where $f_{k} (\tau) = \frac{1}{\varepsilon \pi} \sum_{n = 1}^{k} \frac{1}{n} \sin{\left( n \tau \right)}$.

Eq. (13)'s dynamics under $\tau$ time scale is:

$$
\begin{aligned}
    \omega_{s}^{2} \frac{d^{2} y}{d \tau^{2}} (\tau) &=&& - P y (\tau - 3 \pi) + \varepsilon \bigg[ P t_{s} f_{k} (\tau) - D \bigg] \omega_{s}  \frac{d y}{d \tau} (\tau - 3 \pi) \\
    &&& - \varepsilon^{2} \frac{P}{2} \bigg[ P t_{s}^{2} f_{k}^{2} (\tau) + 2 D t_{s} f_{k} (\tau) \bigg] y (\tau - 6 \pi) + \mathcal{O} (\varepsilon^{3}) , \\
    \Rightarrow \frac{d^{2} y}{d t^{2}} &=&& - \frac{P t_{s}^{2}}{4 \pi^{2}} y (\tau - 3 \pi) + \varepsilon \bigg[ \frac{P t_{s}^{2}}{2 \pi} f_{k} (\tau) - \frac{D t_{s}}{2 \pi} \bigg] \frac{d y}{d \tau} (\tau - 3 \pi) \\
    &&& - \varepsilon^{2} \bigg[ \frac{P^{2} t_{s}^{4}}{8 \pi^{2}} f_{k}^{2} (\tau) + \frac{P D t_{s}^{3}}{2 \pi^{2}} f_{k} (\tau) \bigg] y (\tau - 6 \pi) + \mathcal{O} (\varepsilon^{3}).
\end{aligned}
$$

Denote

$$
\begin{equation}
    \omega_{0} = \frac{\sqrt{P}}{\omega_{s}} = \frac{t_{s} \sqrt{P}}{2 \pi}, \qquad d = \frac{D}{\omega_{s}} = \frac{D t_{s}}{2 \pi},
\end{equation}
$$

then the suggorate constant-delay system follows:

$$
\begin{equation}
    \begin{aligned}
        \frac{d^{2} y}{d \tau^{2}} + \omega_{0}^{2} y (\tau - 3 \pi) &=&& \varepsilon \bigg[ 2 \pi \omega_{0}^{2} f_{k} (\tau) - d \bigg] \frac{d y}{d \tau} (\tau - 3 \pi) \\
        &&& - \varepsilon^{2} \bigg[ 2 \pi^{2} \omega_{0}^{4} f_{k}^{2} (\tau) + 4 \pi d \omega_{0}^{2} f_{k} (\tau) \bigg] y (\tau - 6 \pi) + \mathcal{O} (\varepsilon^{3}).
    \end{aligned}
\end{equation}
$$

## 3. MMS Analysis

The following 5 general equations are going to be used in following MMS perturbation procedure for delay systems. See `README.md` for details.

$$
\begin{gather}
    y = Y_{0} + \varepsilon Y_{1} + \varepsilon^{2} Y_{2} + \cdots, \\
    \frac{d y}{d \tau} = D_0 Y_0 + \varepsilon \left( D_0 Y_1 + D_1 Y_0 \right) + \varepsilon^2 \left( D_0 Y_2 + D_1 Y_1 + D_2 Y_0 \right) + \cdots, \\
    \frac{d^{2} y}{d \tau^{2}} = D_{0}^{2} Y_{0} + \varepsilon \left( 2 D_{0} D_{1} Y_{0} + D_{0}^{2} Y_{1} \right) + \varepsilon^{2} \left( 2 D_{0} D_{2} Y_{0} + 2 D_{1} D_{0} Y_{1} + D_{1}^{2} Y_{0} \right) + \cdots, \\
    y (\tau - \tau_{d}) = Y_{0d} + \varepsilon \left( Y_{1d} - \tau_{d} D_{1} Y_{0d} \right) + \varepsilon^{2} \left( Y_{2d} - \tau_{d} D_{2} Y_{0d} - \tau_{d} D_{1} Y_{1d} \right) + \cdots, \\
    \begin{aligned}
        \frac{d y}{d \tau} (\tau - \tau_{d}) &=&& D_{0} Y_{0d} + \varepsilon \left( D_{0} Y_{1d} + D_{1} Y_{0d} - \tau_{d} D_{0} D_{1} Y_{0d} \right) + \varepsilon^{2} \left[ D_{0} Y_{2d} + D_{1} Y_{1d} \right. \\
        &&& + D_{2} Y_{0d} \left. - \tau_{d} \left( D_{0} D_{2} Y_{0d} + D_{1}^{2} Y_{1d} + D_{0} D_{1} Y_{1d} \right) \right] + \cdots.
    \end{aligned}
\end{gather}
$$

In practice, the sampling frequency is far bigger than the system's natural frequency(or forced frequency), indicating that $\omega_{0} \ll 1$. Truncate $t$ to $T_{2} = \varepsilon^{2} \tau$ and $y$ to $\varepsilon^{2}$. We denote $\square_{id}$ for $\square_{i} (T_{0} - 3 \pi, T_{1}, T_{2})$ and $\square_{i2d}$ for $\square_{i} (T_{0} - 6 \pi, T_{1}, T_{2})$ respectively for brevity.

With the above 5 equations, the following equation can be obtained for $\varepsilon$'s 0th order:

$$
\begin{equation}
    D_{0}^{2} Y_{0} + \omega_{0}^{2} Y_{0d} = 0,
\end{equation}
$$

whose solution is

$$
\begin{equation}
    Y_{0} = A_{0} (T_{1}, T_{2}) \cos{\left( \omega_{0} T_{0} \right)} + B_{0} (T_{1}, T_{2}) \sin{\left( \omega_{0} T_{0} \right)}.
\end{equation}
$$

For $\varepsilon$'s 1st order, the following equation can be obtained:

$$
2 D_{0} D_{1} Y_{0} + D_{0}^{2} Y_{1} + \omega_{0}^{2} Y_{1d} - 3 \pi \omega_{0}^{2} D_{1} Y_{0d} = \bigg[ 2 \pi \omega_{0}^{2} f_{k} (T_{0}) - d \bigg] D_{0} Y_{0d},
$$

Substituting Eq. (22) in the equation above yields:

$$
\begin{equation}
    \begin{aligned}
        D_{0}^{2} Y_{1} + \omega_{0}^{2} Y_{1d} &=&& 3 \pi \omega_{0}^{2} D_{1} Y_{0d} - 2 D_{0} D_{1} Y_{0} + \bigg[ 2 \pi \omega_{0}^{2} f_{k} (T_{0}) - d \bigg] D_{0} Y_{0d} \\
        &=&& 3 \pi \omega_{0}^{2} \bigg[ D_{1} A_{0} \cos{(\omega_{0} T_{0} - 3 \pi \omega_{0})} + D_{1} B_{0} \sin{(\omega_{0} T_{0}B_{1} - 3 \pi \omega_{0})} \bigg] \\
        &&& - 2 \omega_{0} \bigg[ - D_{1} A_{0} \sin{(\omega_{0} T_{0})} + D_{1} B_{0} \cos{(\omega_{0} T_{0})} \bigg] \\
        &&& + \bigg[ 2 \pi \omega_{0}^{2} f_{k} (T_{0}) - d \bigg] \bigg[ - A_{0} \sin{(\omega_{0} T_{0} - 3 \pi \omega_{0})} + B_{0} \cos{(\omega_{0} T_{0} - 3 \pi \omega_{0})} \bigg] \\
        &=&& P_{1} \sin{(\omega_{0} T_{0})} + P_{2} \cos{(\omega_{0} T_{0})},
    \end{aligned}
\end{equation}
$$

where

$$
\begin{gather}
    \begin{aligned}
        P_{1} &=&& \bigg[ -A_{0} \cos{(3 \pi \omega_{0})} + B_{0} \sin{(3 \pi \omega_{0})} \bigg] \bigg[ 2 \pi \omega_{0}^{2} f_{k} (T_{0}) - d \bigg] \\
        &&& + D_{1} A_{0} \bigg[ 2 \omega_{0} + 3 \pi \omega_{0}^{2} \sin{(3 \pi \omega_{0})} \bigg] + D_{1} B_{0} \bigg[ 3 \pi \omega_{0}^{2} \cos{(3 \pi \omega_{0})} \bigg],
    \end{aligned} \\
    \begin{aligned}
        P_{2} &=&& \bigg[ A_{0} \sin{(3 \pi \omega_{0})} + B_{0} \cos{(3 \pi \omega_{0})} \bigg] \bigg[ 2 \pi \omega_{0}^{2} f_{k} (T_{0}) - d \bigg] \\
        &&& + D_{1} A_{0} \bigg[ 3 \pi \omega_{0}^{2} \cos{(3 \pi \omega_{0})} \bigg] - D_{1} B_{0} \bigg[ 2 \omega_{0} + 3 \pi \omega_{0}^{2} \sin{(3 \pi \omega_{0})} \bigg].
    \end{aligned}
\end{gather}
$$

To eliminate secular terms, $P_{1}$ and $P_{2}$ should be equal to zero. However, they're fast-time varying coefficients (compared to $\omega_{0} t$). Therefore, we convert them to integral forms, as are shown below:

$$
\begin{gathered}
    D_{1} A_{0} \cdot 2 \pi \bigg[ 2 \omega_{0} + 3 \pi \omega_{0}^{2} \sin{(3 \pi \omega_{0})} \bigg] + D_{1} B_{0} \cdot 2 \pi \bigg[ 3 \pi \omega_{0}^{2} \cos{(3 \pi \omega_{0})} \bigg] \\
    = - \bigg[ -A_{0} \cos{(3 \pi \omega_{0})} + B_{0} \sin{(3 \pi \omega_{0})} \bigg] \int_{0}^{2 \pi} \bigg[ 2 \pi \omega_{0}^{2} f_{k} (T_{0}) - d \bigg] d T_{0}, \\
    D_{1} A_{0} \cdot 2 \pi \bigg[ 3 \pi \omega_{0}^{2} \cos{(3 \pi \omega_{0})} \bigg] - D_{1} B_{0} \cdot 2 \pi \bigg[ 2 \omega_{0} + 3 \pi \omega_{0}^{2} \sin{(3 \pi \omega_{0})} \bigg] \\
    = - \bigg[ A_{0} \sin{(3 \pi \omega_{0})} + B_{0} \cos{(3 \pi \omega_{0})} \bigg] \int_{0}^{2 \pi} \bigg[ 2 \pi \omega_{0}^{2} f_{k} (T_{0}) - d \bigg] d T_{0}.
\end{gathered}
$$

As $\omega_{0}$ is a subtle parameter, we have

$$
\begin{gather}
    \omega_{0}^{2} \cos{(3 \pi \omega_{0})} = \omega_{0}^{2} \left( 1 - \frac{1}{2} (3 \pi \omega_{0})^{2} + \mathcal{O} (\omega_{0}^{4}) \right) = \omega_{0}^{2} + \mathcal{O} (\omega_{0}^{4}), \\
    \omega_{0}^{2} \sin{(3 \pi \omega_{0})} = \omega_{0}^{2} \left( 3 \pi \omega_{0} + \mathcal{O} (\omega_{0}^{3}) \right) = \mathcal{O} (\omega_{0}^{3}), \\
    -A_{0} \cos{(3 \pi \omega_{0})} + B_{0} \sin{(3 \pi \omega_{0})} = \left( \frac{9 \pi^{2}}{2} \omega_{0}^{2} - 1 \right) A_{0} + 3 \pi \omega_{0} B_{0} + \mathcal{O} (\omega_{0}^{3}), \\
    A_{0} \sin{(3 \pi \omega_{0})} + B_{0} \cos{(3 \pi \omega_{0})} = 3 \pi \omega_{0} A_{0} - \left( \frac{9 \pi^{2}}{2} \omega_{0}^{2} - 1 \right) B_{0} + \mathcal{O} (\omega_{0}^{3}),
\end{gather}
$$

and noting that

$$
\begin{aligned}
    \int_{0}^{2 \pi} \pi f_{k} (T_{0}) d T_{0} &= \frac{1}{\varepsilon} \sum_{n = 1}^{k} \left( \int_{0}^{2 \pi} \frac{1}{n} \sin{\left( n \tau \right)} d T_{0} \right) \\
    &= \frac{1}{\varepsilon} \sum_{n = 1}^{k} \left( 0 \right) \\
    &= 0,
\end{aligned}
$$

Then we have:

$$
\begin{align}
    & 2 \pi \bigg[ 2 \omega_{0} \left( D_{1} A_{0} \right) + 3 \pi \omega_{0}^{2} \left( D_{1} B_{0} \right) \bigg] = - \left[ \left( \frac{9 \pi^{2}}{2} \omega_{0}^{2} - 1 \right) A_{0} + 3 \pi \omega_{0} B_{0} \right] (- 2 \pi d), \\
    & 2 \pi \bigg[ 3 \pi \omega_{0}^{2} \left( D_{1} A_{0} \right) - 2 \omega_{0} \left( D_{1} B_{0} \right) \bigg] = - \left[ 3 \pi \omega_{0} A_{0} - \left( \frac{9 \pi^{2}}{2} \omega_{0}^{2} - 1 \right) B_{0} \right] (- 2 \pi d).
\end{align}
$$

With the above 2 equations, it can be obtained that

$$
\begin{gather}
    D_{1} A_{0} = \frac{d}{2} \left(\frac{45 \pi ^2 \omega _0}{9 \pi ^2 \omega _0^2+4}-\frac{1}{\omega_0}\right) A_0+\frac{3 \pi d}{2} \left(\frac{10}{9 \pi ^2 \omega _0^2+4} - 1 \right) B_0, \\
    D_{1} B_{0} = \frac{3 \pi d}{2} \left(3 \pi -\frac{30 \pi }{9 \pi ^2 \omega _0^2+4}\right) A_{0} +\frac{d}{2} \left(\frac{45 \pi ^2 \omega _0}{9 \pi ^2 \omega _0^2+4}-\frac{1}{\omega_0}\right) B_0.
\end{gather}
$$

Eq. (23) is reduced to:

$$
D_{0}^{2} Y_{1} + \omega_{0}^{2} Y_{1d} = 0,
$$

whose solution is:

$$
\textcolor{red}{Y_{1} = 0 \quad ?}
$$

For $\varepsilon$'s 2nd order, the following equation can be obtained:

$$
\begin{gathered}
    2 D_{0} D_{2} Y_{0} + 2 D_{1} D_{0} Y_{1} + D_{1}^{2} Y_{0} + \omega_{0}^{2} \left( Y_{2d} - 3 \pi D_{2} Y_{0d} - 3 \pi D_{1} Y_{1d} \right) \\
    = \bigg[ 2 \pi \omega_{0}^{2} f_{k} (\tau) - d \bigg] \left( D_{0} Y_{1d} + D_{1} Y_{0d} - 3 \pi D_{0} D_{1} Y_{0d} \right) - \bigg[ 2 \pi^{2} \omega_{0}^{4} f_{k}^{2} (\tau) + 4 \pi d \omega_{0}^{2} f_{k} (\tau) \bigg] Y_{02d},
\end{gathered}
$$

Noting that $Y_{1} = 0$, the equation above can be simplified to:

$$
\begin{aligned}
    D_{1}^{2} Y_{0} + \omega_{0}^{2} Y_{2d} &=&& 3 \pi \omega_{0}^{2} D_{2} Y_{0d} - 2 D_{0} D_{2} Y_{0} + \bigg[ 2 \pi \omega_{0}^{2} f_{k} (\tau) - d \bigg] \left( D_{1} Y_{0d} - 3 \pi D_{0} D_{1} Y_{0d} \right) \\
    &&& - \bigg[ 2 \pi^{2} \omega_{0}^{4} f_{k}^{2} (\tau) + 4 \pi d \omega_{0}^{2} f_{k} (\tau) \bigg] Y_{02d} \\
    &=&& 3 \pi \omega_{0}^{2} \bigg[ D_{2} A_{0} \cos{(\omega_{0} T_{0} - 3 \pi \omega_{0})} + D_{2} B_{0} \sin{(\omega_{0} T_{0} - 3 \pi \omega_{0})} \bigg] \\
    &&& - 2 \omega_{0} \bigg[ - D_{2} A_{0} \sin{(\omega_{0} T_{0})} + D_{2} B_{0} \cos{(\omega_{0} T_{0})} \bigg] \\
    &&& + \bigg[ 2 \pi \omega_{0}^{2} f_{k} (\tau) - d \bigg] \Bigg[ D_{1} A_{0} \cos{(\omega_{0} T_{0} - 3 \pi \omega_{0})} + D_{1} B_{0} \sin{(\omega_{0} T_{0} - 3 \pi \omega_{0})} \\
    &&& - 3 \pi \omega_{0} \bigg[ - D_{1} A_{0} \sin{(\omega_{0} T_{0} - 3 \pi \omega_{0})} + D_{1} B_{0} \cos{(\omega_{0} T_{0} - 3 \pi \omega_{0})} \bigg] \Bigg] \\
    &&& - \bigg[ 2 \pi^{2} \omega_{0}^{4} f_{k}^{2} (\tau) + 4 \pi d \omega_{0}^{2} f_{k} (\tau) \bigg] \bigg[ A_{0} \cos{(\omega_{0} T_{0} - 6 \pi \omega_{0})} + B_{0} \sin{(\omega_{0} T_{0} - 6 \pi \omega_{0})} \bigg] \\
    &=&& P_{3} \sin{(\omega_{0} T_{0})} + P_{4} \cos{(\omega_{0} T_{0})},
\end{aligned}
$$

<!--
Then, $A_{0}$'s and $B_{0}$'s derivative to time $\tau$ follows:

$$
\begin{gathered}
    \begin{aligned}
        \frac{d A_{0}}{d \tau} &= \varepsilon D_{1} A_{0} + \mathcal{O} (\varepsilon^{2}) \\
        &= - \frac{2}{4 + 9 \pi^{2} \omega_{0}^{2}} \left( \frac{A_{0}}{\pi \omega_{0}} + \frac{3 B_{0}}{2} \right) \left( - \varepsilon \pi d \right) + \mathcal{O} (\varepsilon^{2}),
    \end{aligned} \\
    \begin{aligned}
        \frac{d B_{0}}{d \tau} &= \varepsilon D_{1} B_{0} + \mathcal{O} (\varepsilon^{2}) \\
        &= \frac{2}{4 + 9 \pi^{2} \omega_{0}^{2}} \left( - \frac{3 A_{0}}{2} + \frac{B_{0}}{\pi \omega_{0}} \right) \left( - \varepsilon \pi d \right) + \mathcal{O} (\varepsilon^{2}).
    \end{aligned}
\end{gathered}
$$

Change variables in the two equations above to polar coordinates, the transformation equations are:

$$
A_{0} (t) = R (t) \cos{(\varphi (t))}, \qquad B_{0} (t) = R (t) \sin{(\varphi (t))}.
$$

Therefore, it's easy to obtain that

$$
\begin{gather}
    \begin{aligned}
        \frac{d R}{d t} &= \frac{d A_{0}}{d t} \cos{(\varphi)} + \frac{d B_{0}}{d t} \sin{(\varphi)} \\
        &= \frac{2 d \varepsilon \left(9 \pi ^2 \text{$\omega $0}^2-1\right)}{\text{$\omega $0} \left(9 \pi ^2 \text{$\omega $0}^2+4\right)} R + \mathcal{O} (\varepsilon^{2}),
    \end{aligned} \\
    \begin{aligned}
        \frac{d \varphi}{d t} &= - \frac{d A_{0}}{d t} \frac{\sin{(\varphi)}}{R} + \frac{d B_{0}}{d t} \frac{\cos{(\varphi)}}{R} \\
        &=  - \frac{3 \pi \varepsilon d}{4 + 9 \pi^{2} \omega_{0}^{2}} + \mathcal{O} (\varepsilon^{2})
    \end{aligned}
\end{gather}
$$

-->
