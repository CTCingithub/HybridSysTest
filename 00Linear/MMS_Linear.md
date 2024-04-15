<!--
 * @Author: CTC 2801320287@qq.com
 * @Date: 2024-04-15 22:12:16
 * @LastEditors: CTC 2801320287@qq.com
 * @LastEditTime: 2024-04-15 22:48:16
 * @Description: 
 * 
 * Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
-->
# MMS for Linear System with Time-varyingly Delayed Feedback

The equation of the delay system studied is:

$$
\begin{equation}
    \ddot{x} (t) = - p x (t - t_{d}) - d \dot{x} (t - t_{d}),
\end{equation}
$$

where the sawtooth-wave delay $t_{d}$ can be written in Fourier series form:

$$
\begin{equation}
    t_{d} (t, t_{s}) = t_{s} \left( \frac{3}{2} - \frac{1}{\pi} \sum_{n = 1}^{\infty} \frac{1}{n} \sin{\left( \frac{2 n \pi t}{t_{s}} \right)} \right).
\end{equation}
$$

## 1st Order Approximation

Delay $t_{d}$ follows:

$$
\begin{equation}
    t_{d} (t, t_{s}) = t_{s} \left( \frac{3}{2} - \frac{1}{\pi} \sin{ \left(\frac{2 \pi t}{t_{s}} \right)} \right).
\end{equation}
$$

We assume a two scale expansion of the solution:

$$
\begin{equation}
    x(t) = x_{0} (T_{0}, T_{1}) + \varepsilon x_{1} (T_{0}, T_{1}) + O(\varepsilon^{2}),
\end{equation}
$$

where

$$
\begin{equation*}
    T_{0} = t, \qquad T_{1} = \varepsilon t.
\end{equation*}
$$

The following differential operators are utilized:

$$
\begin{equation*}
    \left \{ \begin{aligned}
        & \frac{d}{d t} = \frac{\partial}{\partial T_{0}} + \varepsilon \frac{\partial}{\partial T_{1}} + O(\varepsilon^{2}) = D_{0} + \varepsilon D_{1} + O(\varepsilon^{2}), \\
        & \frac{d^{2}}{d t^{2}} = D_{0}^{2} + 2 \varepsilon D_{0} D_{1} + O(\varepsilon^{2}) .
    \end{aligned} \right.
\end{equation*}
$$

Then we have

$$\begin{equation}
    \left \{ \begin{aligned}
        & \frac{d x}{d t} &&= \left( D_{0} + \varepsilon D_{1} \right) \left( x_{0} + \varepsilon x_{1} \right) \\
        &&&= D_{0} x_{0} + \varepsilon \left( D_{0} x_{1} + D_{1} x_{0} \right), \\
        & \frac{d^{2} x}{d t^{2}} &&= \left( D_{0}^{2} + 2 \varepsilon D_{0} D_{1} \right) \left( x_{0} + \varepsilon x_{1} \right) \\
        &&&= D_{0}^{2} x_{0} + \varepsilon \left( 2 D_{0} D_{1} x_{0} + D_{0}^{2} x_{1} \right), \\
        & x (t - \tau) &&= x_{0} (T_{0} - \tau, T_{1}) + \varepsilon x_{1} (T_{0} - \tau, T_{1}) \\
        &&&= x_{0d} + \varepsilon x_{1d}, \\
        & \frac{d x}{d t} (t - \tau) &&= \left( D_{0} + \varepsilon D_{1} \right) \left( x_{0} (T_{0} - \tau, T_{1}) + \varepsilon x_{1} (T_{0} - \tau, T_{1}) \right) \\
        &&&= D_{0} x_{0} (T_{0} - \tau, T_{1}) + \varepsilon \left( D_{0} x_{1} (T_{0} - \tau, T_{1}) + D_{1} x_{0} (T_{0} - \tau, T_{1}) \right) \\
        &&&= D_{0} x_{0d} + \varepsilon \left( D_{0} x_{1d} + D_{1} x_{0d} \right).
    \end{aligned} \right.
\end{equation}
$$
