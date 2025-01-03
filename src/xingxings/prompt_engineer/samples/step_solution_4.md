在 $\triangle ABC$ 中，已知角 $A = \dfrac{\pi}{3}$，边 $a = 3$，我们需要求三角形面积的最大值。

### 第一步：利用余弦定理
依据 [余弦定理]，我们有：
$$
a^2 = b^2 + c^2 - 2bc \cos A
$$
将已知值代入：
$$
3^2 = b^2 + c^2 - 2bc \cos \dfrac{\pi}{3}
$$
$$
9 = b^2 + c^2 - bc
$$

### 第二步：利用基本不等式
依据 [基本不等式]，对于任意正数 $b$ 和 $c$，有：
$$
b^2 + c^2 \geq 2bc
$$
因此：
$$
9 = b^2 + c^2 - bc \geq 2bc - bc = bc
$$
$$
bc \leq 9
$$

### 第三步：计算面积
依据 [三角形面积公式]，面积 $S$ 为：
$$
S = \dfrac{1}{2} bc \sin A
$$
将已知值代入：
$$
S = \dfrac{1}{2} bc \sin \dfrac{\pi}{3} = \dfrac{1}{2} bc \cdot \dfrac{\sqrt{3}}{2} = \dfrac{\sqrt{3}}{4} bc
$$
由于 $bc \leq 9$，所以：
$$
S \leq \dfrac{\sqrt{3}}{4} \times 9 = \dfrac{9\sqrt{3}}{4}
$$

### 结论
三角形面积的最大值为 $\dfrac{9\sqrt{3}}{4}$。