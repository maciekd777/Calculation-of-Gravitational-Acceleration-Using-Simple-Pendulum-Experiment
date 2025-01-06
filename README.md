# Calculation of Gravitational Acceleration

If you've had physics laboratory classes at some point as a student, there is a big chance that you've come across this experiment. Basically, it is about calculation of gravitational acceleration $g$ using an equation for period $T$ of mathematical pendulum:

$$T = 2\pi\sqrt{\frac{l}{g}} .$$

The experiment involves measurements, uncertainty evaluation, least squares coefficients calculation, and plotting a graph of the best approximation of linear function fitting the measurements.

## Authors

- [@maciekd777](https://github.com/maciekd777)

## Tech Stack

**Data manipulaition:** Pandas

**Data visualization:** Matplotlib

**Linear model data fitting:** Statmodels

**Statistics:** SciPy, NumPy

## Installation

Get the source code and assets from github. Then, install requirements from requirements.txt.

```bash
git clone https://github.com/maciekd777/Calculation-of-Gravitational-Acceleration-Using-Simple-Pendulum-Experiment.git
python -m pip install -r requirements.txt
python main.py
```

## Course of the experiment

1. Measure length $l$ of the pendulum's rod and make sure that it is significantly longer than radius $r$ of the pendulum's bulb. In general, length of the pendulum is equal to length of the rod plus radius $r$ of the bulb.
2. Measure couple times 10 swings of the pendulum (the time of 10 periods $T$). It reduces the uncertainty regarding to stopping the time in the correct frame.
3. Repeat the step 1 and 2 for at least 3 different lengths of the pendulum, and make sure that there is at least 5 cm difference between the lengths

However, be sure that:

- The mass of the rod is negligible compared to mass of the blob
- The time is measured in seconds, and the length is measured in meters
- The pendulum is swung by a small angle (less than about $10 \degree$) to maintain the small angle aproximation
- Start counting the time of the 10 periods when the pendulum is passing the equlibrium position

To calculate the value of $g$ the equations below will be used:

$$T = 2\pi \sqrt{\frac{l}{g}}. $$

$$T^2 = \frac{4\pi^2l}{g},$$

So, the function $f(l) = T^2$ can be rewritten in the following form:

$$T^2 = \frac{4\pi^2}{g} \cdot l,$$

which now is nothing but a linear function:

$$f(x) = mx + b,$$

with coefficient $m$ equal to:

$$m = \frac{4\pi^2}{g},$$

which makes $g$ equal to:

$$g = \frac{4\pi^2}{m}.$$

If all measurements were done with the perfect precision, the points $(l, T^2)$ would form a straight line. Of course, this probably won't be the case, because there is no way that measurements were done with perfect precision, so the points will lie a bit off the perfect line. However, there is still a possibility to calculate coefficient $m$ with it's uncertainty, and draw the best possible approximation of a linear function from the measurement points, by using linear regression, and the least squares method. If the model is linear

$$y = mx + b$$

and couple points $(x_i, y_i)$ are measured, the set of linear equations with every point applied can be represented as follows:

$$y_1 = mx_1 + b$$

$$y_2 = mx_2 + b$$

$$\vdots$$

$$y_i = mx_i + b$$

And in a matrix form:

$$
\begin{align}
\begin{pmatrix}
y_1 \\
y_2 \\
\vdots \\
y_i
\end{pmatrix}
= \begin{pmatrix}
x_1 & 1 \\
x_2 & 1 \\
\vdots & \vdots \\
x_i & 1 \\
\end{pmatrix}
\cdot \begin{pmatrix}
m \\
b \\
\end{pmatrix}
\end{align}
$$

The coefficient $m$ can be approximated with the least squares method and the following equation:

$$m = \frac{(\sum_{i=1}^n x_i) \cdot (\sum_{i=1}^n y_i) - n\sum_{i=1}^n(x_ix_i)}{(\sum_{i=1}^n x_i)^2 - n\sum_{i=1}^n x_i^2} $$

and its uncertainty:

$$ u(m) = \sqrt{\frac{1}{n-2}\sum_{i=1}^n (y_i - (mx_i + b))^2} \cdot \sqrt{\frac{\sum_{i=1}^n x_i^2}{n\sum_{i=1}^n x_i^2 - (\sum_{i=1}^n x_i)^2}} $$

## Example

The mesurements were done in Łódź (latitude $51\degree$) for lengths 0.6 m, 0.55 m, 0.5 m, 0.45 m, and 0.4 m, which makes the number of different lengths of the pendulum for which the measurements were done equal to 5. Every length of the pendulum was measured only once, but for each length the time of the 10 swings of the pendulum was measured 10 times. The length was measured with the measuring device with resolution 0.01 m, as well as the time was measured with the measuring device with resolution 0.01 s.

<div align="center">
<img width=90% src="https://github.com/user-attachments/assets/2c2998ec-e52b-4482-8daa-ad8686a743c4">
</div>

All of the measured values are shown on the picture below:

<div align="center">
<img width=70% src="https://github.com/user-attachments/assets/4f120e22-435f-4649-a686-f66367c91d36">
</div>

Typed values for the length 0.6 m and 0.55 m:

<div align="center">
<img width=60% src="https://github.com/user-attachments/assets/54658833-a61f-404f-ac48-60ca1afc5644">
</div>

After typing all the values, the measurements table is printed, which part is shown at the picture below:

<div align="center">
<img width=60% src="https://github.com/user-attachments/assets/1b9405df-e25a-476e-8545-eba02e9d3b16">
</div>

and graph of the best approximation of linear function that's fitting the measurements is displayed (with measurements points and uncertainties bars):

<div align="center">
<img width=100% src="https://github.com/user-attachments/assets/a48ee19c-0684-4b98-9c2c-bc0993b4419a">
</div>

At last, calculated values of $g$ from latitude, and $g$ from the usage of measurements points and coefficient $m$ of the linear function are displayed with their uncertainties:

<div align="center">
<img width=100% src="https://github.com/user-attachments/assets/edef6c4e-5d9f-4e2b-99b3-0b60ce4277f5">
</div>

## Appendix: Physics and Math Concepts Behind the Experiment

### 1 Physics

#### 1.1 Harmonic oscilator basics

Pendulum is one of the classic examples of harmonic oscilator - a system that performs harmonic motion (a motion that is repeated overtime). Cause of its characteristic nature, specific physical quantities are used to describe its behaviour, among which are:
- Period $T$ - Time of one complete cycle of the pendulum (after that time the harmonic motion repeats again)
- Equilibrium position - A position in space at which pendulum would be if left intact
- Displacement $x$ - A measure of change of the pendulum's position compared to its equilibrium position 
- Amplitude $A$ - Value of the greatest displacement of the pendulum
- Angular frequency $w$ - A measure of how fast the pendulum is covering the angles. While making one complete cycle, the pendulum covers whole $360^\degree = 2\pi$ angle.

The change of displacement $x$ overtime $t$ of every harmonic oscilator can be written, using the following formula:

$$x(t) = A\cos{(\omega t + \phi)},$$

where $\phi$ is, so called, phase of the harmonic oscilator - displacement value of the oscilator relative to the equilibrium position at the start of the observation. For example, if one started the observation halfway the pendulum's cycle, the phase would be equal to $pi$, which is half of the angle covered while making a complete cycle. To make the derivations easier, the value of $\phi$ is often set to zero (a case in which start of one's observation is aligned with start of the pendulum's cycle):

$$x(t) = A\cos{(\omega t)}.$$

Using the equation above, the velocity $v(t)$ and acceleration $a(t)$ equations can be derived:

$$v(t) = \frac{d x}{dt} = -A\omega\sin{\omega t},$$

$$a(t) = \frac{d v}{dt} = -A\omega^2\cos{\omega t}.$$

The next step is to find the equation for the pendulum's $\omega$ and use it to obtain formula for $T$ from $\omega = \frac{2\pi}{T}$.

#### 1.2 Pendulum's $\omega$ and $T$ derivation

To make the derivation simpler, the following form of writing derivatives respect to time $t$ will be used:

$$\frac{\text{d} x}{\text{d} t} = \dot{x},$$

$$\frac{\text{d}^2 x}{\text{d} t^2} = \ddot{x}.$$

To obtain the formula for $\omega$, one need to solve the equation of motion for the pendulum system. One of the methods is to use the Euler-Lagrange equations, which can be obtained solving the equation below:

$$\frac{\text{d}}{\text{d} t}\left(\frac{\partial L}{\partial \dot{q}_j}\right) = \frac{\partial L}{\partial q_j},$$

where $L$ is, so called, Lagrangian of the system and $q_j$ is it's $j$'s generalized coordinate. To figure out Lagrangian is to solve the following equation:

$$L = T - V,$$

where $T$ is the kinetic energy of the system and $V$ - it's potential energy. However, before the calculation of Lagrangian, the generalized coordinates $q_j$ needs to be figured out. They form a set of quantities which allows to describe the position of the mechanical system in a simplest possible way. The most common quantities are the cartesian coordinates, such as $x$ and $y$, but in many cases there is a way to use less quantities, and it also applies to the pendulum case!

<div align="center">
<img width=40% src="https://github.com/user-attachments/assets/1d656c46-5311-4556-ae33-27300652add4">
<p>Simple pendulum, source: Wikimedia Commons</p>
</div>

The next step is to try to calculate the kinetic energy of the pendulum's bulb. By looking at the picture above one can say that the pendulum has velocity on the $x$ axis, but also on the $y$ axis, thus the following can be written:

$$ T = \frac{1}{2} m\dot{x}^2 + \frac{1}{2} m\dot{y}^2.$$

Also, during its movement, the pendulum is converting kinetic energy to potential energy $V$, changing its height $h$ over the equilibrium position. Thus, potential energy of the pendulum is equal to:

$$ V = mgh = mg(l - y), $$

where $l$ is **fixed** length of the rod of the pendulum. 

However, this is not the simplest way to write those quantities, because the number of degrees of freedom can be reduced to just one! Both $x$ and $y$ positions can be written using the angle $\theta$, which is the angle between current position of the pendulum's rod and it's position in the equlibrium position:

$$ x = l\sin{\theta}, $$
$$ y = -l\cos{\theta}, $$

With displacement written like this, the following equations for velocity for both axis can be written:

$$ \dot{x} = \frac{\text{d} x}{\text{d} t} = -l\dot{\theta}\cos{\theta} ,$$
$$ \dot{y} = \frac{\text{d} y}{\text{d} t} = l\dot{\theta}\sin{\theta} ,$$

and total kinetic energy of the system can be expressed using just one variable $\theta$, instead two cartesian coordinates:

$$ T = \frac{1}{2} m\dot{x}^2 + \frac{1}{2} m\dot{y}^2 = \frac{1}{2} l^2\dot{\theta}^2\cos^2{\theta} + \frac{1}{2} l^2\dot{\theta}^2\sin^2{\theta} = \frac{1}{2}m\dot{\theta}^2(\sin^2{\theta} + \cos^2{\theta}) = \frac{1}{2}m\dot{\theta}^2 .$$

Thus, the Lagrangian of our pendulum is:

$$ L = T - V = \frac{1}{2}m\dot{\theta}^2 - mg(l - (-l\cos{\theta})) = \frac{1}{2}ml^2\dot{\theta}^2 - mgl + mg\cos{\theta} .$$

Now, the Euler-Lagrange equations can be solved as follows (in this case it will be just one equation, beacause only one generalized coordinate was used):

$$ \frac{\partial L}{\partial \dot{\theta}} = ml^2\dot{\theta}

$$ \frac{\text{d}}{\text{d} t}\left(\frac{\partial L}{\partial \dot{q}_j}\right) = ml^2\ddot{\theta} ,$$

$$ \frac{\partial L}{\partial \theta} = -mgl\sin{\theta} .$$

And finally, the equation of motion of the pendulum is equal to:

$$ ml^2\ddot{\theta} = -mgl\sin{\theta} ,$$

$$ \ddot{\theta} = -\frac{g}{l}\sin{\theta} .$$

The equation above is still not as simple as it could be due to the factor $\sin{\theta}$ on the right side of the equation. It can be simplified using an approximation, which is called **small-angle approximation**. If the angle $\theta$ is quite small (less than about $10\degree$), $\sin{\theta}$ is approximately equal to $\theta$ itself (in radian, of course). Thus, the following can be written:

$$ \ddot{\theta} = -\frac{g}{l}\theta .$$

Looking at the equations from the beggining:

$$x(t) = A\cos{(\omega t)},$$

$$a(t) = -A\omega^2\cos{\omega t},$$

the second equation can be expressed in the following way:

$$a(t) = -\omega^2x(t),$$

and note that exactly this form was derived with the usage of Euler-Lagrange equation:

$$ \ddot{\theta} = -\frac{g}{l}\theta .$$

From the equation above one can deduce that the $\omega^2$ for the simple pendulum can be written in a following way:

$$\omega^2 = \frac{g}{l},$$

and the $\omega$ itself:

$$\omega = \sqrt{\frac{g}{l}}.$$

Finally, the formula for $T$ of the simple pendulum:

$$ \omega = \frac{2\pi}{T} ,$$

$$ T = \frac{2\pi}{\omega} ,$$

$$ T = 2\pi\sqrt{\frac{l}{g}}, $$

where $l$ is a length of the pendulum's rod and $g$ is gravitational acceleration.

#### 1.3 Gravitational acceleration

For two masses $m_1$ and $m_2$ there exist a gravitational force $F$ that makes the masses attract each other. Its value can be calculated using the equation below:

$$ F = \text{G}\frac{m_1m_2}{r^2} ,$$

where $r$ is a length of a vector connecting center of masses of the system and $\text{G}$ is gravitational constant. This gravitational force is affecting everything on Earth, thus for mass $m$ on the Earth's surface, the following equation can be written:

$$ F = \text{G}\frac{Mm}{R^2} ,$$

where $M$ is a mass of the Earth and $R$ is its radius. In this equation $\text{G}, M, R$ are all constants, thus convinient is to write all of this as one constant $g$:

$$ F = gm ,$$

where $g$ is gravitational acceleration and is equal to $g = \text{G}\frac{M}{R^2}$. On the poles value of $g$ is about 9.78 m/s$^2$, but with change of latitude, altitude, and longitude, value of $g$ also changes, because the Earth is not a perfect sphere and its radius slightly changes, as well as the centrifugal force due to Earth's rotation. To avoid at least some of the differences, to calculate the "real" value of $g$ the following equation will be used, that is based on a latitude of the place where the measurements were made:

$$g = 9.7803267714 \cdot \left(\frac{1 + 0.00193185138639 \cdot \sin^2{\phi}}{\sqrt{1 - 0.00669437999013 \cdot \sin^2{\phi}}}\right) ,$$

where $\phi$ is the latitude in $\degree$.

### 2 Uncertainties evaluation methods

#### 2.1 Postulates related to uncertainties and measurements in this experiment

With every measurement comes uncertainty - a value that describes a range in which the experimentator is cofident the real value of a measurand lands. For the sake of this experiment, the following is postulated:

- All measurements are independent
- If only one measurement of the measurand was made, or all values from the set of measurements are the same, distribution of values of the measurand follows the continous uniform distribution, and uncertainty of the most probable value of the measurand is equal to the type B uncertainty
- If values of the measurements are not the same, value of uncertainty of the most probable value of the measurand is equal to the expanded uncertainty of the total uncertainty, calculated with type A and type B uncertainty
- Type B uncertainty (uncertainty which value depends on all of the things that could have an impact on the observed values, but are not related to statistic of the measured values, e.g. the deficiency of the device, imperfection of the system, approximations, experimenter not perfectly reading the values, etc.) is reduced to uncertainty of the calibration of the measuring device
- **All measurements of the same measurand (length or time) should be done the same number of times for each length of the pendulum (for example, there shouldn't be a situation where for one length of the pendulum the length was measured 2 times and for the other 5 times)**
- **All measurements of the same measurand (length or time) should be done with the same measuring device and on the same range (the resolution of the measuring device should be the same for all the measurements)**
- Values of uncertainties should be rounded to 2 significant figures, and the most probable values of the measurands should be rounded to the same digit as its uncertainties
- If the most probable value of the measurand is less than its uncertainty, it should be rounded to standard 3 significant digits
- Table with all of the measurements will be printed with all of the values that the user has typed, unchanged. The only values rounded will be the most probable values of the measurands and its uncertainties

#### 2.2 Type A uncertainty

If values of measurements of the measurand $x$ are not the same, the expected value of the measurand $x$ is the mean value $\bar{x}$ of the values measured:

$$ \bar{x} = \frac{\sum_{i=1}^{n} x_i}{n} ,$$

where $n$ is the number of the values measured and $x_i$ is the $i$ measured value. Thus, the uncertainty in this case should be somehow related to standard deviation of the measured values, and in fact it is. To calculate standard deviation in this situation, the following formula for standard deviation of a population from a sample (the values obtained in the measurements done during the experiment are only a sample from infinite number of values that could occur in the whole population of infinite number of measurements) can be used:

$$ s(X) = \sqrt{\frac{\sum_{i=1}^{n} (x_i - \bar{x})^2}{n-1}} ,$$

where $s(x_i)$ is standard deviation of measurand $X$ and $\bar{x}$ is a mean of measured values. Note that this formula is a bit different from the standard deviation of the population, in which the denominator is equal to $n$. However, this is not yet the uncertainty of measurand $x$. To calculate $u(x)$ the equation below is used:

$$ u_A(x) = \frac{s(X)}{\sqrt{n}} ,$$

where fraction $\frac{s(x_i)}{\sqrt{n}}$ is called standard deviation of the mean, which is also often reffered as standard error of the mean or uncertainty type A.

#### 2.2 Type B uncertainty

Uncertainty related to the measuring device can be calculated using the following formula:

$$ u_B(x) = \frac{u_c(x)}{\sqrt{3}} ,$$

where $u_c(x)$ is the calibration uncertainty, which one can calculate using resolution $\Delta _r x$ of the measuring device:

$$ u_c(x) = \Delta _r x .$$

*Example.*

<div align="center">
<img width=80% src="https://github.com/user-attachments/assets/15d8ab0d-5ee6-491d-8cd7-dcc553bc860e">
<p>Ruler with resolution equal to 0.1 cm</p>
</div>

There are many other ways to calculate type B uncertainty, but in this experiment the only measured quantities are time and length, thus there is no need to use more advanced measuring instruments like analog and digital ones. Type B uncertainty is also calculated when the values of the measurements are different, because even then the uncertainty related to the measuring device need to be taken into account. But, if all values of measurements are the same, or there was only one measurement done, the uncertainty of the most probable value of the measurand will be equal to only type B uncertainty.

#### 2.3 Total standart uncertainty and expanded uncertainty

After calculating type A and type B uncertainty, total standart uncertainty $u(x)$ can be calculated in a following way:

$$ u(x) = \sqrt{u_A^2(x) + u_B^2(x)}, $$

which is then used to evaluate expanded uncertainty $U(x)$:

$$ U(x) = u(x) \cdot k .$$

Factor $k$ is called coverage factor and is dependent on the one's confidence that chosing a random sample from the population of our measurements results in a confidence interval which contains the true value being estimated, and degrees of freedom of the sample. Values of $k$ can be found using the table of Student's critical values $t$:

<div align="center">
<img width=40% src="https://github.com/user-attachments/assets/005efe49-9690-4d8c-ae3d-dbb35e059075">
<p>Table of Student's $t$ critical values, source: https://people.richland.edu</p>
</div>

In the case of this experiment, the assumed confidence level is 95% (which means 95% probability that chosing a random sample from the population of the measurements results in a confidence interval which contains the true value being estimated) with $n-1$ degrees of freedom (whenever calculating standard deviation for some measurand $X$ there is $n-1$ independent variables, because the mean $\bar{x}$ also contains value $x_i$, so $x_i$ and $\bar{x}$ are dependent values).

#### 2.4 Uncertainty equations for $T^2$ and $g$

Because $T^2$ and $g$ are values measured indirectly, they uncertainties need to be calculated using propagation of uncertainty:

$$ u(x_1, x_2,..., x_i) = \sqrt{\left(\frac{\partial f}{\partial x_1}\right)^2 \cdot u(x_1)^2 + \left(\frac{\partial f}{\partial x_2}\right)^2 \cdot u(x_2)^2 + \cdots + \left(\frac{\partial f}{\partial x_i}\right)^2 \cdot u(x_i)^2 } ,$$

where $x_1,...,x_i$ are the quantities measured directly. For the $T^2$ the equation becomes:

$$ u(T^2) = \sqrt{\left(\frac{\partial (\frac{T_{10}}{10})^2}{\partial T}\right)^2 \cdot u^2(T_{10})} = \sqrt{\left(\frac{2T_{10}}{100}\right)^2 \cdot u^2(T_{10})} = \frac{T_{10}}{50} \cdot u(T_{10}) $$

and for $g$:

$$ u(g) = \sqrt{\left(\frac{\partial (\frac{4\pi^2}{m})}{\partial m}\right)^2 \cdot u^2(m)} = \frac{4\pi^2}{m^2} \cdot u(m) $$

## Badges

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

