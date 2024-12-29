请老师解答我的问题：在 $\triangle ABC$ 中，$\angle C >90^\circ$，$\sin C = \dfrac{2\sqrt{2}}{3}$，$a = 2$，$b = 3$，求 $c$

要解决这个问题，我们可以将其拆分为以下几个小问题：

### 小问题 1：已知 $\sin C = \dfrac{2\sqrt{2}}{3}$，求 $\cos C$。
**解析：**
由于 $\angle C > 90^\circ$，所以 $\cos C$ 为负数。根据三角恒等式：
$$
\sin^2 C + \cos^2 C = 1
$$
代入已知的 $\sin C$：
$$
\left(\dfrac{2\sqrt{2}}{3}\right)^2 + \cos^2 C = 1 \\
\dfrac{8}{9} + \cos^2 C = 1 \\
\cos^2 C = 1 - \dfrac{8}{9} = \dfrac{1}{9} \\
\cos C = -\dfrac{1}{3}
$$

### 小问题 2：利用余弦定理求 $c$。
**解析：**
余弦定理公式为：
$$
c^2 = a^2 + b^2 - 2ab \cos C
$$
代入已知的 $a = 2$，$b = 3$，$\cos C = -\dfrac{1}{3}$：
$$
c^2 = 2^2 + 3^2 - 2 \times 2 \times 3 \times \left(-\dfrac{1}{3}\right) \\
c^2 = 4 + 9 + 4 = 17 \\
c = \sqrt{17}
$$

### 最终答案：
$$
c = \sqrt{17}
$$