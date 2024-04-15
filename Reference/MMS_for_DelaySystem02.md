<!--
 * @Author: CTC 2801320287@qq.com
 * @Date: 2024-04-11 20:56:54
 * @LastEditors: CTC 2801320287@qq.com
 * @LastEditTime: 2024-04-15 22:11:59
 * @Description: 
 * 
 * Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
-->
# MMS for Delay Systems Example 02

The equation of the delay system studied is:

$$
\begin{equation}
    \begin{aligned}
        \frac{d^{2} x}{d t^{2}} (t) + x (t) &=&& -2 \varepsilon \zeta \frac{d x}{d t} (t) - \varepsilon \mu x^{3} (t) + 2 \varepsilon u x(t - \tau) \\
        &&& + 2 \varepsilon v \frac{d x}{d t} (t - \tau) + \varepsilon f \cos{\left( (1 + \varepsilon \sigma) t \right)}.
    \end{aligned}
\end{equation}
$$

The author assume a two scale expansion of the solution:

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

With Eq.(1)(2)(3), it can be obtained from $\varepsilon$'s 0th order terms that:

$$
\begin{equation}
    D_{0}^{2} x_{0} (T_{0}, T_{1}) + x_{0} (T_{0}, T_{1}) = 0,
\end{equation}
$$

Then,

$$
\begin{equation}
    x_{0} (T_{0}, T_{1}) = A(T_{1}) e^{i T_{0}} + cc.
\end{equation}
$$

Similarly, it can be obtained from $\varepsilon$'s 1storder terms that:

$$
\begin{equation}
    \begin{aligned}
        2 D_{0} D_{1} x_{0} (T_{0}, T_{1}) + D_{0}^{2} x_{1} (T_{0}, T_{1}) + x_{1} (T_{0}, T_{1}) &=&& - 2 \zeta D_{0} x_{0} (T_{0}, T_{1}) - \mu x_{0}^{3} (T_{0}, T_{1}) \\
        &&& + 2 u x_{0} (T_{0} - \tau, T_{1}) + 2 v D_{0} x_{0} (T_{0} - \tau, T_{1}) \\
        &&& + f \cos{(T_{0} + \sigma T_{1})}
    \end{aligned}
\end{equation}
$$

Substituting Eq.(5) into Eq.(6) yields:

$$
\begin{equation}
    \begin{aligned}
        D_{0}^{2} x_{1} (T_{0}, T_{1}) + x_{1} (T_{0}, T_{1}) &=&& - 2 D_{0} D_{1} x_{0} (T_{0}, T_{1}) - 2 \zeta D_{0} x_{0} (T_{0}, T_{1}) - \mu x_{0}^{3} (T_{0}, T_{1}) \\
        &&& + 2 u x_{0} (T_{0} - \tau, T_{1}) + 2 v D_{0} x_{0} (T_{0} - \tau, T_{1}) + \frac{f}{2} e^{i T_{0}} e^{i \sigma T_{1}} + cc \\
        &=&& - 2 i e^{i T_{0}} D_{1}A - 2 i \zeta e^{i T_{0}} A - \mu \left( A^{3} e^{3 i T_{0}} + 3 A^{2} \bar{A} e^{i T_{0}} \right) \\
        &&& + 2 u e^{- i \tau} e^{i T_{0}} A + 2 i v e^{- i \tau} e^{i T_{0}} A + \frac{f}{2} e^{i T_{0}} e^{i \sigma T_{1}} + cc \\
        &=&& e^{i T_{0}} \left[ \left( - 3 \mu A^{2} \bar{A} + 2 u A e^{- i \tau} + \frac{f}{2} e^{i \sigma T_{1}} \right) \right. \\
        &&& \left. + i \left( - 2 D_{1} A - 2 \zeta A + 2 v e^{- i \tau} A \right) \right] - \mu A^{3} e^{3 i T_{0}} + cc.
    \end{aligned}
\end{equation}
$$

To eliminate secular terms, there are:

$$
\begin{equation}
    - 3 \mu A^{2} \bar{A} + 2 u A e^{- i \tau} + \frac{f}{2} e^{i \sigma T_{1}} - 2 i \left( D_{1} A + \zeta A - v e^{- i \tau} A \right) = 0.
\end{equation}
$$

Suppose $A=A(T_{1})$ follows:

$$
\begin{equation}
    A(T_{1}) = \frac{1}{2} \alpha(T_{1}) e^{i \beta(T_{1})},
\end{equation}
$$

where $\alpha(T_{1})$ and $\beta(T_{1})$ are real functions of $T_{1}$. With Eq.(9), it can be obtained from Eq.(8) that:

$$
\begin{equation}
    \begin{aligned}
        & - \frac{3}{8} \mu \alpha^{3} e^{2 i \beta} + u \alpha e^{ - i \tau} + \frac{f}{2} e^{i \left( \sigma T_{1} - \beta \right)} \\
        & - i \left( \left( D_{1} \alpha \right) + i \alpha \left( D_{1} \beta \right) + \zeta \alpha - v \alpha e^{- i \tau} \right) &= 0, \\
    \end{aligned}
\end{equation}
$$

Define

$$
\varphi (T_{1}) = \sigma T_{1} - \beta.
$$

Then,

$$
D_{1} \beta = \sigma - D_{1} \varphi.
$$

Eq.(10) can be rewritten as:

$$
\begin{equation}
    \begin{aligned}
        & - \frac{3}{8} \mu \alpha^{3} e^{2 i \left( \sigma T_{1} - \varphi \right)} + u \alpha e^{ - i \tau} + \frac{f}{2} e^{i \varphi} \\
        & - i \left( \left( D_{1} \alpha \right) - i \alpha \left( D_{1} \varphi \right) + i \alpha \sigma + \zeta \alpha - v \alpha e^{- i \tau} \right) &= 0, \\
    \end{aligned}
\end{equation}
$$
