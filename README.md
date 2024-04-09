<!--
 * @Author: CTC 2801320287@qq.com
 * @Date: 2024-03-26 10:56:14
 * @LastEditors: CTC 2801320287@qq.com
 * @LastEditTime: 2024-04-07 10:17:03
 * @Description: 
 * 
 * Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
-->
# Continuous-time Approximation of Digital Sampling Systems

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
    M (\vec{q}) \ddot{\vec{q}} + C (\vec{q}, \dot{\vec{q}}) \vec{q} + G (\vec{q}) + f (\dot{\vec{q}}) = \tau \left( \dot{\vec{q}} \left( t - t_{d} \right), \vec{q} \left( t - t_{d} \right) \right).
\end{equation}
$$

, where the delay $t_{d}$ is a sawtooth wave function of time $t$:

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
