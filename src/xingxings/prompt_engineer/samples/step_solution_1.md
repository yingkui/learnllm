在三角形 \( ABC \) 中，已知角 \( A = \dfrac{\pi}{3} \) 和边 \( a = 3 \)，我们需要求三角形面积的最大值。以下是详细的解答步骤：

---

### 第一步：理解已知条件
依据 [已知条件]，我们有以下信息：
1. 角 \( A = \dfrac{\pi}{3} \)（即 \( 60^\circ \)）；
2. 边 \( a = 3 \)，即边 \( a \) 是角 \( A \) 的对边。

---

### 第二步：利用正弦定理
依据 [正弦定理]，在任意三角形中，有：
\[
\frac{a}{\sin A} = \frac{b}{\sin B} = \frac{c}{\sin C}
\]
将已知条件代入，得到：
\[
\frac{3}{\sin \dfrac{\pi}{3}} = \frac{b}{\sin B} = \frac{c}{\sin C}
\]
计算 \( \sin \dfrac{\pi}{3} = \dfrac{\sqrt{3}}{2} \)，因此：
\[
\frac{3}{\dfrac{\sqrt{3}}{2}} = \frac{2 \cdot 3}{\sqrt{3}} = \frac{6}{\sqrt{3}} = 2\sqrt{3}
\]
所以，正弦定理可以写成：
\[
\frac{b}{\sin B} = \frac{c}{\sin C} = 2\sqrt{3}
\]
即：
\[
b = 2\sqrt{3} \sin B, \quad c = 2\sqrt{3} \sin C
\]

---

### 第三步：表达面积公式
依据 [三角形面积公式]，三角形的面积 \( S \) 可以表示为：
\[
S = \frac{1}{2} \cdot b \cdot c \cdot \sin A
\]
将 \( b = 2\sqrt{3} \sin B \)、\( c = 2\sqrt{3} \sin C \) 和 \( \sin A = \sin \dfrac{\pi}{3} = \dfrac{\sqrt{3}}{2} \) 代入，得到：
\[
S = \frac{1}{2} \cdot (2\sqrt{3} \sin B) \cdot (2\sqrt{3} \sin C) \cdot \dfrac{\sqrt{3}}{2}
\]
化简：
\[
S = \frac{1}{2} \cdot 4 \cdot 3 \cdot \sin B \cdot \sin C \cdot \dfrac{\sqrt{3}}{2} = 3\sqrt{3} \sin B \sin C
\]

---

### 第四步：利用角关系
依据 [三角形内角和]，有：
\[
A + B + C = \pi
\]
已知 \( A = \dfrac{\pi}{3} \)，因此：
\[
B + C = \pi - \dfrac{\pi}{3} = \dfrac{2\pi}{3}
\]
利用三角恒等式，可以将 \( \sin B \sin C \) 表示为：
\[
\sin B \sin C = \frac{1}{2} [\cos(B - C) - \cos(B + C)]
\]
由于 \( B + C = \dfrac{2\pi}{3} \)，因此：
\[
\sin B \sin C = \frac{1}{2} \left[ \cos(B - C) - \cos \dfrac{2\pi}{3} \right]
\]
计算 \( \cos \dfrac{2\pi}{3} = -\dfrac{1}{2} \)，因此：
\[
\sin B \sin C = \frac{1}{2} \left[ \cos(B - C) + \dfrac{1}{2} \right] = \frac{1}{2} \cos(B - C) + \dfrac{1}{4}
\]

---

### 第五步：求面积的最大值
将 \( \sin B \sin C \) 的表达式代入面积公式：
\[
S = 3\sqrt{3} \left( \frac{1}{2} \cos(B - C) + \dfrac{1}{4} \right) = \frac{3\sqrt{3}}{2} \cos(B - C) + \dfrac{3\sqrt{3}}{4}
\]
为了使面积 \( S \) 最大，需要使 \( \cos(B - C) \) 最大。由于 \( \cos(B - C) \) 的最大值为 \( 1 \)，因此：
\[
S_{\text{max}} = \frac{3\sqrt{3}}{2} \cdot 1 + \dfrac{3\sqrt{3}}{4} = \frac{3\sqrt{3}}{2} + \dfrac{3\sqrt{3}}{4} = \dfrac{9\sqrt{3}}{4}
\]

---

### 最终答案
三角形面积的最大值为：
\[
\boxed{\dfrac{9\sqrt{3}}{4}}
\]