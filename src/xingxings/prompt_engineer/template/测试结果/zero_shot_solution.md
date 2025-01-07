我们需要在三角形 $ABC$ 中，已知角 $A = \dfrac{\pi}{3}$，边 $a = 2$，$D$ 是 $BC$ 边的中点，求中线 $AD$ 的最大值。

### 步骤 1：理解已知条件
- 角 $A = \dfrac{\pi}{3}$。
- 边 $a = 2$，即边 $BC = 2$。
- $D$ 是 $BC$ 边的中点，因此 $BD = DC = 1$。
- $AD$ 是中线，我们需要求 $AD$ 的最大值。

### 步骤 2：应用余弦定理
在三角形 $ABC$ 中，根据余弦定理，我们有：
$$
b^2 + c^2 - 2bc \cos A = a^2
$$
代入已知条件：
$$
b^2 + c^2 - 2bc \cos \dfrac{\pi}{3} = 2^2
$$
因为 $\cos \dfrac{\pi}{3} = \dfrac{1}{2}$，所以：
$$
b^2 + c^2 - bc = 4
$$

### 步骤 3：表达中线 $AD$ 的长度
中线 $AD$ 的长度可以通过中线公式表示：
$$
AD = \dfrac{1}{2} \sqrt{2b^2 + 2c^2 - a^2}
$$
代入 $a = 2$：
$$
AD = \dfrac{1}{2} \sqrt{2b^2 + 2c^2 - 4}
$$

### 步骤 4：利用已知关系简化表达式
从步骤 2 中，我们有 $b^2 + c^2 - bc = 4$，可以将其代入中线公式：
$$
AD = \dfrac{1}{2} \sqrt{2(b^2 + c^2) - 4}
$$
因为 $b^2 + c^2 = 4 + bc$，所以：
$$
AD = \dfrac{1}{2} \sqrt{2(4 + bc) - 4} = \dfrac{1}{2} \sqrt{8 + 2bc - 4} = \dfrac{1}{2} \sqrt{4 + 2bc}
$$
进一步简化：
$$
AD = \dfrac{1}{2} \sqrt{2(2 + bc)} = \dfrac{\sqrt{2}}{2} \sqrt{2 + bc}
$$

### 步骤 5：应用基本不等式
根据基本不等式，我们有：
$$
b^2 + c^2 \geqslant 2bc
$$
从步骤 2 中，$b^2 + c^2 = 4 + bc$，所以：
$$
4 + bc \geqslant 2bc \implies 4 \geqslant bc
$$
因此，$bc \leqslant 4$。

### 步骤 6：求 $AD$ 的最大值
由于 $AD = \dfrac{\sqrt{2}}{2} \sqrt{2 + bc}$，且 $bc \leqslant 4$，所以当 $bc = 4$ 时，$AD$ 取得最大值：
$$
AD_{\text{max}} = \dfrac{\sqrt{2}}{2} \sqrt{2 + 4} = \dfrac{\sqrt{2}}{2} \sqrt{6} = \dfrac{\sqrt{12}}{2} = \dfrac{2\sqrt{3}}{2} = \sqrt{3}
$$

### 最终答案
中线 $AD$ 的最大值为 $\sqrt{3}$。