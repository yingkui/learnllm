我们来逐步解决这个问题。

**第一步：向量关系**

在三角形 $ABC$ 中，$D$ 是 $BC$ 的中点，因此中线 $AD$ 可以表示为：
$$
\overrightarrow{AD} = \dfrac{1}{2} (\overrightarrow{AB} + \overrightarrow{AC})
$$

**第二步：平方等式**

对 $\overrightarrow{AD}$ 进行平方，得到：
$$
|\overrightarrow{AD}|^2 = \left|\dfrac{1}{2} (\overrightarrow{AB} + \overrightarrow{AC})\right|^2 = \dfrac{1}{4} |\overrightarrow{AB} + \overrightarrow{AC}|^2
$$

展开后得到：
$$
|\overrightarrow{AD}|^2 = \dfrac{1}{4} (|\overrightarrow{AB}|^2 + |\overrightarrow{AC}|^2 + 2 \overrightarrow{AB} \cdot \overrightarrow{AC})
$$

**第三步：余弦定理**

在三角形 $ABC$ 中，根据余弦定理，我们有：
$$
a^2 = b^2 + c^2 - 2bc \cos A
$$
已知 $A = \dfrac{\pi}{3}$，$a = 2$，代入得到：
$$
2^2 = b^2 + c^2 - 2bc \cos \dfrac{\pi}{3}
$$
$$
4 = b^2 + c^2 - bc
$$

**第四步：结合向量关系和余弦定理**

根据向量关系，我们有：
$$
|\overrightarrow{AD}|^2 = \dfrac{1}{4} (b^2 + c^2 + 2bc \cos A)
$$
代入 $A = \dfrac{\pi}{3}$，得到：
$$
|\overrightarrow{AD}|^2 = \dfrac{1}{4} (b^2 + c^2 + bc)
$$

根据余弦定理的结果 $b^2 + c^2 = 4 + bc$，代入上式：
$$
|\overrightarrow{AD}|^2 = \dfrac{1}{4} (4 + bc + bc) = \dfrac{1}{4} (4 + 2bc) = 1 + \dfrac{bc}{2}
$$

**第五步：利用基本不等式求 $bc$ 的最大值**

根据基本不等式，我们有：
$$
b^2 + c^2 \geqslant 2bc
$$
根据余弦定理的结果 $b^2 + c^2 = 4 + bc$，代入上式：
$$
4 + bc \geqslant 2bc
$$
$$
4 \geqslant bc
$$
因此，$bc$ 的最大值为 $4$。

**第六步：求 $AD$ 的最大值**

根据第四步的结果：
$$
|\overrightarrow{AD}|^2 = 1 + \dfrac{bc}{2}
$$
当 $bc$ 取最大值 $4$ 时：
$$
|\overrightarrow{AD}|^2 = 1 + \dfrac{4}{2} = 3
$$
因此，$AD$ 的最大值为：
$$
AD = \sqrt{3}
$$

**最终答案：**
中线 $AD$ 的最大值为 $\sqrt{3}$。