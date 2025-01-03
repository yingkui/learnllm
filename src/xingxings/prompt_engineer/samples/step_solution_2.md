在三角形 $ABC$ 中，已知角 $A = \dfrac{\pi}{3}$，边 $a = 3$，我们需要求三角形面积的最大值。

### 第一步：确定已知条件
依据 [已知条件]，我们有：
- 角 $A = \dfrac{\pi}{3}$
- 边 $a = 3$

### 第二步：应用正弦定理
依据 [正弦定理]，我们有：
$$
\frac{a}{\sin A} = \frac{b}{\sin B} = \frac{c}{\sin C}
$$
代入已知值：
$$
\frac{3}{\sin \dfrac{\pi}{3}} = \frac{b}{\sin B} = \frac{c}{\sin C}
$$
计算 $\sin \dfrac{\pi}{3}$：
$$
\sin \dfrac{\pi}{3} = \dfrac{\sqrt{3}}{2}
$$
所以：
$$
\frac{3}{\dfrac{\sqrt{3}}{2}} = \frac{b}{\sin B} = \frac{c}{\sin C} \Rightarrow \frac{6}{\sqrt{3}} = \frac{b}{\sin B} = \frac{c}{\sin C}
$$
简化：
$$
\frac{6}{\sqrt{3}} = 2\sqrt{3}
$$
因此：
$$
b = 2\sqrt{3} \sin B, \quad c = 2\sqrt{3} \sin C
$$

### 第三步：表达面积公式
依据 [三角形面积公式]，面积 $S$ 可以表示为：
$$
S = \dfrac{1}{2} \times b \times c \times \sin A
$$
代入已知值：
$$
S = \dfrac{1}{2} \times 2\sqrt{3} \sin B \times 2\sqrt{3} \sin C \times \sin \dfrac{\pi}{3}
$$
简化：
$$
S = \dfrac{1}{2} \times 4 \times 3 \times \sin B \times \sin C \times \dfrac{\sqrt{3}}{2} = 3\sqrt{3} \sin B \sin C
$$

### 第四步：利用角度关系
在三角形中，角 $A + B + C = \pi$，已知 $A = \dfrac{\pi}{3}$，所以：
$$
B + C = \dfrac{2\pi}{3}
$$
我们可以设 $B = \theta$，则 $C = \dfrac{2\pi}{3} - \theta$。

### 第五步：表达面积关于 $\theta$ 的函数
将 $B = \theta$ 和 $C = \dfrac{2\pi}{3} - \theta$ 代入面积公式：
$$
S = 3\sqrt{3} \sin \theta \sin \left( \dfrac{2\pi}{3} - \theta \right)
$$
利用三角恒等式：
$$
\sin \left( \dfrac{2\pi}{3} - \theta \right) = \sin \dfrac{2\pi}{3} \cos \theta - \cos \dfrac{2\pi}{3} \sin \theta = \dfrac{\sqrt{3}}{2} \cos \theta + \dfrac{1}{2} \sin \theta
$$
所以：
$$
S = 3\sqrt{3} \sin \theta \left( \dfrac{\sqrt{3}}{2} \cos \theta + \dfrac{1}{2} \sin \theta \right) = 3\sqrt{3} \left( \dfrac{\sqrt{3}}{2} \sin \theta \cos \theta + \dfrac{1}{2} \sin^2 \theta \right)
$$
进一步简化：
$$
S = 3\sqrt{3} \left( \dfrac{\sqrt{3}}{4} \sin 2\theta + \dfrac{1}{2} \sin^2 \theta \right)
$$

### 第六步：求面积的最大值
为了求面积的最大值，我们需要对 $S$ 关于 $\theta$ 求导并找到极值点。然而，这里我们可以通过观察来简化问题。

注意到当 $B = C$ 时，三角形为等腰三角形，此时面积可能达到最大值。设 $B = C = \dfrac{\pi}{3}$，则 ：
$$
S = 3\sqrt{3} \sin \dfrac{\pi}{3} \sin \dfrac{\pi}{3} = 3\sqrt{3} \left( \dfrac{\sqrt{3}}{2} \right)^2 = 3\sqrt{3} \times \dfrac{3}{4} = \dfrac{9\sqrt{3}}{4}
$$

### 最终结果
三角形面积的最大值为：
$$
\boxed{\dfrac{9\sqrt{3}}{4}}
$$