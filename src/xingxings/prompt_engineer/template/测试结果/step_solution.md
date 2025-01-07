我们来逐步解答这个问题。

**已知条件：**
1. 在 $\triangle ABC$ 中，$a^2 - b^2 + c^2 = 2$。
2. $\sin B = \dfrac{1}{3}$，且 $B \in \left(0, \dfrac{\pi}{2}\right)$。

**目标：**
求三角形的面积 $S_{\triangle ABC}$。

---

### 第一步：利用余弦定理

在 $\triangle ABC$ 中，余弦定理为：
$$
b^2 = a^2 + c^2 - 2ac \cos B
$$

将已知条件 $a^2 - b^2 + c^2 = 2$ 代入余弦定理：
$$
a^2 - (a^2 + c^2 - 2ac \cos B) + c^2 = 2
$$

化简：
$$
a^2 - a^2 - c^2 + 2ac \cos B + c^2 = 2
$$
$$
2ac \cos B = 2
$$
$$
ac \cos B = 1
$$

**结果：**
$$
ac \cos B = 1 \quad (1)
$$

---

### 第二步：利用 $\sin B$ 求 $\cos B$

已知 $\sin B = \dfrac{1}{3}$，且 $B \in \left(0, \dfrac{\pi}{2}\right)$，所以 $\cos B$ 为正数。

根据三角恒等式：
$$
\sin^2 B + \cos^2 B = 1
$$

代入 $\sin B = \dfrac{1}{3}$：
$$
\left(\dfrac{1}{3}\right)^2 + \cos^2 B = 1
$$
$$
\dfrac{1}{9} + \cos^2 B = 1
$$
$$
\cos^2 B = 1 - \dfrac{1}{9} = \dfrac{8}{9}
$$
$$
\cos B = \dfrac{2\sqrt{2}}{3}
$$

**结果：**
$$
\cos B = \dfrac{2\sqrt{2}}{3} \quad (2)
$$

---

### 第三步：求 $ac$

将式 $(2)$ 代入式 $(1)$：
$$
ac \cdot \dfrac{2\sqrt{2}}{3} = 1
$$
$$
ac = \dfrac{3}{2\sqrt{2}}
$$

对分母有理化：
$$
ac = \dfrac{3}{2\sqrt{2}} \cdot \dfrac{\sqrt{2}}{\sqrt{2}} = \dfrac{3\sqrt{2}}{4}
$$

**结果：**
$$
ac = \dfrac{3\sqrt{2}}{4} \quad (3)
$$

---

### 第四步：求面积 $S_{\triangle ABC}$

三角形的面积公式为：
$$
S_{\triangle ABC} = \dfrac{1}{2} ac \sin B
$$

将式 $(3)$ 和 $\sin B = \dfrac{1}{3}$ 代入：
$$
S_{\triangle ABC} = \dfrac{1}{2} \cdot \dfrac{3\sqrt{2}}{4} \cdot \dfrac{1}{3}
$$
$$
S_{\triangle ABC} = \dfrac{1}{2} \cdot \dfrac{\sqrt{2}}{4} = \dfrac{\sqrt{2}}{8}
$$

**最终结果：**
$$
S_{\triangle ABC} = \dfrac{\sqrt{2}}{8}
$$