# Surrogate Model for the Linear System

Eq. (13) follows:

$$
\frac{d^{2} y}{d \tau^{2}} + \omega_{0}^{2} y(\tau - 3 \pi) = \varepsilon [ 2 \pi \omega_{0} f(\tau) - \mu ] \frac{d y}{d \tau} (\tau - 3 \pi) + \varepsilon^{2} [2 \pi^{2} \omega_{0}^{4} f^{2} (\tau) - 2 \pi \mu \omega_{0}^{2} f(\tau)] y (\tau - 6 \pi),
$$

where

$$
\omega_{s} = \frac{2 \pi}{t_{s}}, \qquad \omega_{0} = \frac{\sqrt{P}}{\omega_{s}}, \qquad \mu = \frac{D}{\omega_{s}}.
$$

Due to the donation that

$$
y (\tau) = x (t), \qquad \tau = \omega_{s} t.
$$

Besides, we have

$$
\frac{d y}{d \tau} = \frac{1}{\omega_{s}} \frac{d x}{d t}, \qquad \frac{d^{2} y}{d \tau^{2}} = \frac{1}{\omega_{s}^{2}} \frac{d^{2} x}{d t^{2}}, \\
y (\tau - 3 \pi) = x \left( t - \frac{3 \pi}{\omega_{s}} \right), \qquad \frac{d y}{d \tau} (\tau - 3 \pi) = \frac{1}{\omega_{s}} \frac{d x}{d t} \left( t - \frac{3 \pi}{\omega_{s}} \right), \\
f_{k}' (t) = f_{k} (\tau) = \sum_{n =1}^{k} \frac{1}{n} \sin{(\omega_{s} t)}
$$

Therefore, Eq. (13) can be written as

$$
\begin{gathered}
    \frac{d^{2} x}{d t^{2}} + \omega_{s}^{2} \omega_{0}^{2} x (t - \frac{3 \pi}{\omega_{s}}) = \varepsilon \omega_{s} [ 2 \pi \omega_{0} f'(t) - \mu ] \frac{d x}{d t} (t - \frac{3 \pi}{\omega_{s}}) \\
    - \varepsilon^{2} \omega_{s}^{2} [2 \pi^{2} \omega_{0}^{4} f'^{2} (t) - 2 \pi \mu \omega_{0}^{2} f' (t)] x (t - \frac{6 \pi}{\omega_{s}})
\end{gathered}
$$
