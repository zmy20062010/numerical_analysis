#!/usr/bin/env python
# coding: utf-8

# # <center> 第14章: 线性方程组求解</center>
# <center>（Chapter 14: Linear System of Equations）</center>

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#序言" data-toc-modified-id="序言-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>序言</a></span></li><li><span><a href="#线性代数基础" data-toc-modified-id="线性代数基础-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>线性代数基础</a></span><ul class="toc-item"><li><span><a href="#集合" data-toc-modified-id="集合-2.1"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>集合</a></span></li><li><span><a href="#矢量" data-toc-modified-id="矢量-2.2"><span class="toc-item-num">2.2&nbsp;&nbsp;</span>矢量</a></span></li><li><span><a href="#矩阵" data-toc-modified-id="矩阵-2.3"><span class="toc-item-num">2.3&nbsp;&nbsp;</span>矩阵</a></span><ul class="toc-item"><li><span><a href="#矩阵的基本运算" data-toc-modified-id="矩阵的基本运算-2.3.1"><span class="toc-item-num">2.3.1&nbsp;&nbsp;</span>矩阵的基本运算</a></span></li></ul></li><li><span><a href="#线性变换" data-toc-modified-id="线性变换-2.4"><span class="toc-item-num">2.4&nbsp;&nbsp;</span>线性变换</a></span></li><li><span><a href="#矢量空间、矢量与范数" data-toc-modified-id="矢量空间、矢量与范数-2.5"><span class="toc-item-num">2.5&nbsp;&nbsp;</span>矢量空间、矢量与范数</a></span><ul class="toc-item"><li><span><a href="#矢量空间" data-toc-modified-id="矢量空间-2.5.1"><span class="toc-item-num">2.5.1&nbsp;&nbsp;</span>矢量空间</a></span></li><li><span><a href="#矢量空间的范数" data-toc-modified-id="矢量空间的范数-2.5.2"><span class="toc-item-num">2.5.2&nbsp;&nbsp;</span>矢量空间的范数</a></span></li><li><span><a href="#矩阵的范数" data-toc-modified-id="矩阵的范数-2.5.3"><span class="toc-item-num">2.5.3&nbsp;&nbsp;</span>矩阵的范数</a></span></li></ul></li></ul></li><li><span><a href="#线性方程组的解" data-toc-modified-id="线性方程组的解-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>线性方程组的解</a></span><ul class="toc-item"><li><span><a href="#线性方程组示例" data-toc-modified-id="线性方程组示例-3.1"><span class="toc-item-num">3.1&nbsp;&nbsp;</span>线性方程组示例</a></span></li><li><span><a href="#线性方程组的解的存在唯一性定理" data-toc-modified-id="线性方程组的解的存在唯一性定理-3.2"><span class="toc-item-num">3.2&nbsp;&nbsp;</span>线性方程组的解的存在唯一性定理</a></span></li></ul></li><li><span><a href="#解线性方程组的直接法" data-toc-modified-id="解线性方程组的直接法-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>解线性方程组的直接法</a></span><ul class="toc-item"><li><span><a href="#消元法" data-toc-modified-id="消元法-4.1"><span class="toc-item-num">4.1&nbsp;&nbsp;</span>消元法</a></span><ul class="toc-item"><li><span><a href="#高斯消元法（Gauss-Elimination）" data-toc-modified-id="高斯消元法（Gauss-Elimination）-4.1.1"><span class="toc-item-num">4.1.1&nbsp;&nbsp;</span>高斯消元法（Gauss Elimination）</a></span></li><li><span><a href="#列主元消元法（Gauss-Elimination-with-Partial-Pivoting）" data-toc-modified-id="列主元消元法（Gauss-Elimination-with-Partial-Pivoting）-4.1.2"><span class="toc-item-num">4.1.2&nbsp;&nbsp;</span>列主元消元法（Gauss Elimination with Partial Pivoting）</a></span></li><li><span><a href="#全主元消元法（Gauss-Elimination-with-Complete-Pivoting）" data-toc-modified-id="全主元消元法（Gauss-Elimination-with-Complete-Pivoting）-4.1.3"><span class="toc-item-num">4.1.3&nbsp;&nbsp;</span>全主元消元法（Gauss Elimination with Complete Pivoting）</a></span></li><li><span><a href="#高斯-约旦消元法（Gauss-Jordan-Elimination）" data-toc-modified-id="高斯-约旦消元法（Gauss-Jordan-Elimination）-4.1.4"><span class="toc-item-num">4.1.4&nbsp;&nbsp;</span>高斯-约旦消元法（Gauss-Jordan Elimination）</a></span></li><li><span><a href="#消元法的python实现" data-toc-modified-id="消元法的python实现-4.1.5"><span class="toc-item-num">4.1.5&nbsp;&nbsp;</span>消元法的python实现</a></span></li></ul></li><li><span><a href="#矩阵分解法" data-toc-modified-id="矩阵分解法-4.2"><span class="toc-item-num">4.2&nbsp;&nbsp;</span>矩阵分解法</a></span><ul class="toc-item"><li><span><a href="#高斯消元法与矩阵分解（Gauss-Elimination-as-Matrix-Decomposition）" data-toc-modified-id="高斯消元法与矩阵分解（Gauss-Elimination-as-Matrix-Decomposition）-4.2.1"><span class="toc-item-num">4.2.1&nbsp;&nbsp;</span>高斯消元法与矩阵分解（Gauss Elimination as Matrix Decomposition）</a></span></li><li><span><a href="#矩阵的LU分解（LU-decomposition-of-matrices）" data-toc-modified-id="矩阵的LU分解（LU-decomposition-of-matrices）-4.2.2"><span class="toc-item-num">4.2.2&nbsp;&nbsp;</span>矩阵的LU分解（LU decomposition of matrices）</a></span></li><li><span><a href="#LU分解法解线性方程组" data-toc-modified-id="LU分解法解线性方程组-4.2.3"><span class="toc-item-num">4.2.3&nbsp;&nbsp;</span>LU分解法解线性方程组</a></span></li><li><span><a href="#矩阵的PLU分解" data-toc-modified-id="矩阵的PLU分解-4.2.4"><span class="toc-item-num">4.2.4&nbsp;&nbsp;</span>矩阵的PLU分解</a></span></li><li><span><a href="#PLU分解法解线性方程组" data-toc-modified-id="PLU分解法解线性方程组-4.2.5"><span class="toc-item-num">4.2.5&nbsp;&nbsp;</span>PLU分解法解线性方程组</a></span></li><li><span><a href="#对称矩阵及对称正定矩阵的分解" data-toc-modified-id="对称矩阵及对称正定矩阵的分解-4.2.6"><span class="toc-item-num">4.2.6&nbsp;&nbsp;</span>对称矩阵及对称正定矩阵的分解</a></span></li><li><span><a href="#矩阵分解法的python实现" data-toc-modified-id="矩阵分解法的python实现-4.2.7"><span class="toc-item-num">4.2.7&nbsp;&nbsp;</span>矩阵分解法的python实现</a></span></li></ul></li><li><span><a href="#迭代法求线性方程组" data-toc-modified-id="迭代法求线性方程组-4.3"><span class="toc-item-num">4.3&nbsp;&nbsp;</span>迭代法求线性方程组</a></span><ul class="toc-item"><li><span><a href="#迭代法的基本构造方法" data-toc-modified-id="迭代法的基本构造方法-4.3.1"><span class="toc-item-num">4.3.1&nbsp;&nbsp;</span>迭代法的基本构造方法</a></span></li><li><span><a href="#迭代法的收敛特性" data-toc-modified-id="迭代法的收敛特性-4.3.2"><span class="toc-item-num">4.3.2&nbsp;&nbsp;</span>迭代法的收敛特性</a></span></li><li><span><a href="#Gauss-Seidel迭代" data-toc-modified-id="Gauss-Seidel迭代-4.3.3"><span class="toc-item-num">4.3.3&nbsp;&nbsp;</span>Gauss-Seidel迭代</a></span></li><li><span><a href="#Jacobi迭代" data-toc-modified-id="Jacobi迭代-4.3.4"><span class="toc-item-num">4.3.4&nbsp;&nbsp;</span>Jacobi迭代</a></span></li><li><span><a href="#超松弛(SOR)迭代" data-toc-modified-id="超松弛(SOR)迭代-4.3.5"><span class="toc-item-num">4.3.5&nbsp;&nbsp;</span>超松弛(SOR)迭代</a></span></li></ul></li></ul></li><li><span><a href="#小结" data-toc-modified-id="小结-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>小结</a></span></li><li><span><a href="#思考和习题" data-toc-modified-id="思考和习题-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>思考和习题</a></span></li></ul></div>

# ## 序言

# 工程实践和科学研究中许多问题最终都使用线性方程组进行表示或者近似。
# 
# 一方面，线性化是我们认识世界的基本哲学。尽管我们对物理世界的认识已经非常深刻，构建了
# 许多非线性的物理模型，但是在理论和数值上处理这些非线性模型，获得对应物理问题的内在性
# 质任然是依靠在特定工作点处的线性化。例如，对单摆对应的动力系统而言
# $$
#    \ddot{\theta} = \frac{g}{l} \sin\theta
# $$
# 由于其非线性，获得其解析解比较困难。比较通行的做法是，在零点$\theta = 0$（该点是
# 该系统的一个平衡）附近，对该动力系统进行线性化获得
# $$
#    \ddot{\theta} = \frac{g}{l} \theta.
# $$
# 这个方程即是我们非常熟悉的单摆方程。其周期，振动幅值等动力学信息能够很轻松的获得。
# 
# 
# 另一方面，线性化是我们改造世界的基本方法。对于线性问题，我们目前已经发展出一套比较完善
# 的理论，这对于我们在工程实践中解决问题非常有利。此外，由于工程实践问题很多受限于测量和
# 加工误差等，只能够近似描述，线性化成为我们对这些工程实践问题进行研究的不二法门。

# ![image.png](./images/truss_analysis_example.jpg)
# ![image.png](./images/electrical-network-analysis_example.jpg)

# 实际上很多数值计算方法，最终也会涉及到线性方程组的求解问题：
# - 样条插值的$M$和$m$关系式；
# - 曲线拟合的法方程；
# - 方程组的$Newton$迭代；
# - 求解常微分方程组的隐式方法；
# - 求解偏微分方程的有限元，有限体积，有限差分等方法。
# 
# 这些线性方程组的系数矩阵大致分为两种；
# - 低阶稠密矩阵（如阶数不超过$150$的矩阵等）
# - 大型稀疏矩阵（即矩阵阶数高且零元素较多）
# 
# 低阶稠密矩阵一般使用直接法进行求解，而大型稀疏矩阵采用迭代法计算能够获得更高的效率。

# ## 线性代数基础
# 在进一步介绍线性方程组的解的直接法和迭代法之前，我们首先回顾总结一下线性代数的基础知识点。

# ### 集合

# 数学上，集合是由一个或多个确定的具有某种性质的对象所构成的整体。构成集合的这些对象则称为该集合的元素。例如，全中国人的集合，它的元素就是每一个中国人。通常用大写字母如$A$，$B$，$S$，$T$等表示集合，而用小写字母如$a$，$b$，$x$，$y$等表示集合的元素。若$x$是集合$S$的元素，则称$x$属于$S$，记为$x \in S$。若$y$不是集合$S$的元素，则称$y$不属于$S$，记为$y \notin S$。
# 
# 集合中元素的数目称为集合的基数，集合A的基数记作$card(A)$。当其为有限大时，集合$A$称为有限集，反之则为无限集。一般的，把含有有限个元素的集合叫做有限集，含无限个元素的集合叫做无限集。

# - 有一类特殊的集合，它不包含任何元素，如$\{x| x\in R: x^2 +1=0\}$ ，称之为空集，记为$\emptyset$。空集是个特殊的集合，它有2个特点：
#     - 空集∅是任意一个非空集合的真子集。
#     - 空集是任何一个集合的子集。
# - 设$S$，$T$是两个集合，如果$S$的所有元素都属于$T$ ，即$x \in S \Rightarrow x \in T$，则称$S$是$T$的子集，记为$S \subseteq T$。显然，对任何集合$S$，都有$S \subseteq S, \emptyset \subseteq S$。其中，符号$\subseteq$读作包含于，表示该符号左边的集合中的元素全部是该符号右边集合的元素。如果$S$是$T$的一个子集，即$S \subseteq T$，但在$T$中存在一个元素$x$不属于$S$，即$S \subset T$，则称$S$是$T$的一个真子集。
# - 交集是由属于$A$且属于$B$的相同元素组成的集合，记作$A \cap B$（或$B\cap A$），读作"A交B"（或"B交A"），即$A∩B=\{x|x \in A,\mbox{且}x \in B\}$。注意交集越交越少。若$A$包含$B$，则$A \cap B=B$。
# 
# - 并集是由所有属于集合$A$或属于集合$B$的元素所组成的集合，记作$A \cup B$（或$B \cup A$），读作"A并B"（或"B并A"），即$A \cup B=\{x|x\in A,\mbox{或}x \in B\}$。注意并集越并越多，这与交集的情况正相反。
# 
# - 补集又可分为相对补集和绝对补集。相对补集由属于A而不属于B的元素组成的集合，称为$B$关于$A$的相对补集，记作$A-B$或$A \backslash B$，即$A-B=\{x|x \in A，\mbox{且}x \notin B\}$。集合$A$关于全集合$U$的相对补集称作$A$的绝对补集，记作$A^\prime$或$ \complement_U (A）$或$\sim A$。有$U^\prime= \emptyset$；$\emptyset^\prime = U$。
# 
# - 设有集合$A$，由集合$A$所有子集组成的集合，称为集合$A$的幂集。对于幂集有定理如下：有限集$A$的幂集的基数等于$2$的有限集$A$的基数次幂。

# 几种标准的数集： **自然数**,  **整数**, **有理数**, **无理数**, **实数**, 和 **复数**.  
# 
# | 集合名  | 符号  | 描述  |
# |------|------|------------|
# |   自然数  | $\mathbb{N}$| ${\mathbb{N}} = \{0, 1, 2, 3, 4, \cdots\}$|
# |   整数    | $\mathbb{Z}$| ${\mathbb{Z}} = \mathbb{W} \cup \{-1, -2, -3, \cdots\}$|
# |   有理数  | $\mathbb{Q}$| ${\mathbb{Q}} = \{\frac{p}{q} : p\in {\mathbb{Z}}, q\in {\mathbb{Z}} \backslash \{0\}\}$|
# |   无理数  | $\mathbb{I}$| ${\mathbb{I}}$是由不能表示成整数之比的数组成的集合.|
# |   实数    | $\mathbb{R}$| ${\mathbb{R}} = \mathbb{Q} \cup \mathbb{I}$|
# |   复数    | $\mathbb{C}$| ${\mathbb{C}} = \{a + bi : a,b\in {\mathbb{R}}, i = \sqrt{-1}\}$|

# **回顾!** 令$S$表示所有满足$x^2 + y^2 = 1$的实数对$(x,y)$构成的集合。利用集合的符号写出$S$。
# 
# 
# $S = \{(x,y) : x,y \in {\mathbb{R}}, x^2 + y^2 = 1\}$

# ### 矢量

# 集合${\mathbb{R}}^n$是所有实数$n$元组构成的集合，可表示为${\mathbb{R}}^n = \{(x_1, x_2, x_3, \cdots, x_n): x_1, x_2, x_3, \cdots, x_n \in {\mathbb{R}}\}$. 
# 
# 以${\mathbb{R}}^3$为例，它表示了所有实数三元组，即$(x,y,z)$，的集合，可以与三维空间中的点一一对应起来。

# ${\mathbb{R}}^n$ 中的**矢量**是一个属于${\mathbb{R}}^n$的$n$元组。它有两种书写方式：行向量和列向量。**行向量**一般的表示方式为$[x_1, x_2, x_3, \cdots, x_n]$，**列向量**一般的表示方式为$[x_1, x_2, x_3, \cdots, x_n]^T$，这里的上标$T$表示转置。若未特别说明，**矢量一般是指列矢量**。一般我们还定义**零矢量** 为${\mathbb{R}}^n$中的全零$n$元组。

# **!例** 利用python的numpy包创建行矢量和列矢量，并获得矢量的**形状**.

# In[1]:


import numpy as np
vector_row = np.array([[1, -5, 3, 2, 4]])
vector_column = np.array([[1], 
                          [2], 
                          [3], 
                          [4]])
print(vector_row), print(vector_column)
print(vector_row.shape)
print(vector_column.shape)

vrow = np.array([1,2,3,4,5,6,7])
vcol = vrow.T
print(vrow),print(vcol)

print(vrow.shape)
print(vcol.shape)


# In[2]:


import numpy as np

vec_class  = np.array([
    [1,2,34,5],
    [3,2,1,4],
    [1,5,2,3]
])
print(vec_class.shape)

vec_class  = np.array([
    [[1,2],[1,2],[1,2]],
    [[3,2],[1,4],[5,5]],
    [[1,5],[2,3],[2,4]]
])
print(vec_class.shape)

vec_class  = np.array([
    [[1,2],[1,2],[1,2]],
    [[3,2],[1,4],[5,5]],
    [[1,5],[2,3]]
])
print(vec_class.shape)


# **! 注意** 在numpy中，1维数组（array）和二维数组是有一些不一样的。二维数组可以进行转置获得行矢量和列矢量的转换，而一维数组虽然可以进行转置，但并未获得任何不同结果。

# **矢量加法** 定义为两个被加矢量的对应分量的分别相加。例如，如果$v$和$w$是${\mathbb{R}}^n$中的两个矢量，那么$u = v + w$定义为$u_i = v_i + w_i,\ i = 1,2,\cdots, n$.

# **矢量数乘** 表示一个矢量与一个**标量**(如${\mathbb{R}}$中的一个实数)的乘积，其定义为矢量的每个元素与标量的乘积。若$\alpha$是一个标量，$v$是一个矢量，则$u = \alpha v$定义为$u_i = \alpha v_i,\ i = 1,2,\cdots, n$.

# **！例!** 证明 $a(v + w) = av + aw$。

# **矢量点乘** 又称为两个矢量的内积，表示两个矢量$v$和$w$对应分量之间的乘积的和，记为$v \cdot w$。具体而言，对于${\mathbb{R}}^n$中的两个矢量$v$和$w$，$d = v\cdot w$定义为
# $$d = \sum_{i = 1}^{n} v_i w_i$$

# **矢量之间的夹角**， $\theta$，定义为
# 
# $$
# v \cdot w = \sqrt{v \cdot v} \sqrt{w \cdot w} \cos{\theta}
# $$

# 如果两个矢量相互垂直，则矢量之间的夹角为$0$。

# **！例 ！** 计算矢量 $v = [10, 9, 3]$ 和 $w = [2, 5, 12]$ 之间的夹角。 

# In[3]:


import numpy as np
import numpy.linalg as npl

v = np.array([[10, 9, 3]])
w = np.array([[2, 5, 12]])
theta = np.arccos(np.dot(v, w.T)/(npl.norm(v)*npl.norm(w)))
print(theta)
print(np.dot(v,w.T))
print(np.dot(v.T,w))
# print(np.dot(v,w))


# In[4]:


import numpy as np
import numpy.linalg as npl

v = np.array([10, 9, 3])
w = np.array([2, 5, 12])

print(np.dot(v,w))


# 两个矢量$v$和$w$ 的 **矢量叉积** 写作 $v \times w$，定义为 $v \times w = \mathbf{n} \sqrt{v \cdot v} \sqrt{w \cdot w} \sin\theta $。其中$\theta$是两个矢量$v$和$w$之间的夹角， **$n$** 是一个与$v$和$w$同时垂直的矢量。

# **！例！** 给定矢量$v = [0, 2, 0]$ 和 $w = [3, 0, 0]$, 计算$v$和$w$ 的叉积。

# In[5]:


v = np.array([[0, 2, 0]])
w = np.array([[3, 0, 0]])
print(np.cross(v, w))


# 考虑$S$是一个定义了加法和数乘的集合，则$S$的**线性组合**定义为
# $$
# \sum \alpha_i s_i,
# $$
# 其中$\alpha_i$是任意实数，$s_i$是$S$的第$i$个元素。$\alpha_i$也称为$s_i$的**系数**。
# 
# 一个集合称为**线性无关** （**linearly independent**），如果其中的任何一个元素都不能表示为其他元素的线性组合。本课程中我们一般涉及矢量的线性无关。一个矢量的集合如果不是线性无关，则称为线性相关。

# **！ 例 ！** 给定行矢量 $v = [0, 3, 2]$，$w = [4, 1, 1]$，和 $u = [0, -2, 0]$，将矢量$x = [-8, -1, 4]$表示为$v$， $w$，和 $u$的线性组合。

# In[6]:


v = np.array([[0, 3, 2]])
w = np.array([[4, 1, 1]])
u = np.array([[0, -2, 0]])
x = 3*v-2*w+4*u
print(x)


# **！ 例 ！** 确定以下矢量是否线性无关：$v = [1, 1, 0]$， $w = [1, 0, 0]$，和$u = [0, 0, 1]$.
# 
# Clearly $u$ is linearly independent from $v$ and $w$ because only $u$ has a nonzero third element. The vectors $v$ and $w$ are also linearly independent because only $v$ has a nonzero second element. Therefore, $v, w$, and $u$ are linearly independent.

# ### 矩阵

# 一个${m} \times {n}$ **矩阵**是一个$m$行$n$列的矩形数据表。一般用$\mathbb{R}^{m \times n}$表示全部${m} \times {n}$实矩阵的矢量空间，用$\mathbb{C}^{m \times n}$表示全部${m} \times {n}$复矩阵的矢量空间。

# $$
# \mathbf{A} \in \mathbb{R}^{m \times n} \Leftrightarrow \mathbf{A} = (a_{ij}) = \begin{pmatrix}
#     a_{11} & a_{12} & \cdots & a_{1n} \\
#     a_{21} & a_{22} & \cdots & a_{2n} \\
#     \vdots & \vdots & \ddots & \vdots \\
#     a_{n1} & a_{n2} & \cdots & a_{nn} \\
# \end{pmatrix}
# $$

# #### 矩阵的基本运算

# - 矩阵加法

# $$
#    \mathbf{C} = \mathbf{A}  +  \mathbf{B},\quad c_{ij} = a_{ij} + b_{ij},\quad \mathbf{A},\ \mathbf{B},\ \mathbf{C} \in \mathbb{R}^{m \times n}
# $$

# - 矩阵与标量的乘法

# $$
#    \mathbf{C} = \alpha \mathbf{A},\quad c_{ij} = \alpha a_{ij}
# $$

# - 矩阵与矩阵的乘法

# $$
#    \mathbf{C} = \mathbf{A} \mathbf{B},\quad c_{ij} = \sum_{k=1}^{n} a_{ik} b_{kj},\quad \mathbf{A}\in \mathbb{R}^{m \times n},\ \mathbf{B}\in \mathbb{R}^{n \times p},\ \mathbf{C} \in \mathbb{R}^{m \times p}
# $$

# - 矩阵的转置

# $$
#    \mathbf{A} \in \mathbb{R}^{m \times n},\quad \mathbf{C} = \mathbf{A}^T ,\quad c_{ij} = a_{ji}
# $$

# - 单位矩阵

# $$
# \mathbf{I} = \begin{pmatrix}
#        1   &    0   & \cdots &    0    \\
#        0   &    1    & \cdots &    0    \\
#     \vdots & \vdots & \ddots & \vdots \\
#        0   &    0   & \cdots &    1    \\
# \end{pmatrix}$$

# - 非奇异矩阵

# 设$\mathbf{A} \in \mathbb{R}^{n \times n}$，$\mathbf{B} \in \mathbb{R}^{n \times n}$。如果$\mathbf{A} \mathbf{B} = \mathbf{B} \mathbf{A} = \mathbf{I}$，则称$\mathbf{B}$是$\mathbf{A}$的**逆矩阵**，记为$\mathbf{A}^{-1}$，且$(\mathbf{A}^{-1})^T = (\mathbf{A}^T)^{-1}$。
# 
# 如果$\mathbf{A}^{-1}$存在，则称$\mathbf{A}$为**非奇异矩阵**。如果$\mathbf{A},\mathbf{B} \in \mathbb{R}^{n \times n}$均为非奇异矩阵，则$(\mathbf{A}\mathbf{B})^{-1} = \mathbf{B}^{-1}\mathbf{A}^{-1}$。

# - 矩阵的行列式

# 设$\mathbf{A} \in \mathbb{R}^{n \times n}$，则$\mathbf{A}$的行列式可按任一行或一列展开，即
# $$
# det(\mathbf{A}) = \sum_{j=1}^{n} a_{ij}A_{ij},\quad i=1,2,\cdots, n,
# $$
# 其中$A_{ij}$为$a_{ij}$的代数余子式，$A_{ij} = (-1)^{i+j} M_{ij}$，$M_{ij}$为元素$a_{ij}$的余子式。
# 
# 在$n$阶行列式中，划去元$a_{ij}$所在的第$i$行与第$j$列的元，剩下的元不改变原来的顺序所构成的$n-1$阶行列式称为元$a_{ij}$的余子式。

# **! 例 !** Let the Python matrices $P = [[1, 7], [2, 3], [5, 0]]$ and $Q = [[2, 6, 3, 1], [1, 2, 3, 4]]$. Compute the matrix product of $P$ and $Q$. Show that the product of $Q$ and $P$ will produce an error.
# $$
#   P = \begin{pmatrix}
#       1 & 7 \\
#       2 & 3 \\
#       5 & 0 \\
#   \end{pmatrix},\quad
#   Q = \begin{pmatrix}
#       2 & 6 & 3 & 1 \\
#       1 & 2 & 3 & 4 \\
#   \end{pmatrix}
# $$
# 

# In[7]:


P = np.array([[1, 7], [2, 3], [5, 0]])
Q = np.array([[2, 6, 3, 1], [1, 2, 3, 4]])
print(P)
print(Q)
print(np.dot(P, Q))
# np.dot(Q, P)
P*Q


# **TRY IT!** Use Python to find the determinant of the matrix $M = [[0, 2, 1, 3], [3, 2, 8, 1], [1, 0, 0, 3], [0, 3, 2, 1]]$. Use the *np.eye* function to produce a ${4} \times {4}$ identity matrix, $I$. Multiply $M$ by $I$ to show that the result is $M$.

# In[29]:


import numpy.linalg as npl

M = np.array([[0,2,1,3], 
             [3,2,8,1], 
             [1,0,0,3],
             [0,3,2,1]])
print('M:\n', M)

print('Determinant: %.1f'%npl.det(M))
I = np.eye(4)
print('I:\n', I)
print('M*I:\n', np.dot(M, I))


# **! 例 !** The matrix $M$ (in the previous example) has a nonzero determinant. Compute the inverse of $M$. Show that the matrix $P = [[0, 1, 0], [0, 0, 0], [1, 0, 1]]$ has a determinant value of 0 and therefore has no inverse.

# In[30]:


from numpy.linalg import inv

print('Inv M:\n', inv(M))
P = np.array([[0,1,0],
              [0,0,0],
              [1,0,1]])
print('det(p):\n', det(P))


# ### 线性变换

# 对于矢量$x$和$y$，以及标量$a$和$b$而言，函数，$F$，称为**线性变换**，如果它满足
# $$
# F(a x + by) = aF(x) + bF(y)
# $$

# 对于一个${m} \times {n}$的矩阵$A$而言，它可以看作是一个线性变换，讲一个${n} \times {1}$的矢量$v$通过矩阵乘法变换为一个${m} \times {1}$的矢量。

# 对于一个${m} \times {n}$的矩阵$A$而言，有两个重要的关联空间：${\mathbb{R}}^n$和${\mathbb{R}}^m$。$A$的**定义域**是${\mathbb{R}}^n$的子空间，是所有能够与矩阵$A$进行乘积的矢量的集合。$A$的**值域**是${\mathbb{R}}^m$的子空间，是所有能够表示成$y=Ax$的矢量$y$的集合，其中$x\in{\mathbb{R}}^n$。

# $A$的**值域**可以表示为$\mathcal{R}(\mathbf{A})$，其中 $\mathcal{R}(\mathbf{A}) = \{y \in {\mathbb{R}}^m: Ax = y\}$。值域的另一种理解方式是矩阵$A$中所有列矢量的所有线性组合的集合。

# **矩阵$A$的零空间** 定义为$\mathcal{N}(\mathbf{A}) = \{x \in {\mathbb{R}}^n: Ax = 0_m\}$，是$A$的**定义域**的子空间，其中$0_m$是**零矢量** (所有分量都为$0$).

# **! 例 !** 设$A = [[1, 0, 0], [0, 1, 0], [0, 0, 0]]$，令$A$的定义域为${\mathbb{R}}^3$. 求$A$的值域和零空间.
#   
# Let $v = [x,y,z]$ be a vector in ${\mathbb{R}}^3$. Then $u = Av$ is the vector $u = [x,y,0]$. Since $x,y\in {\mathbb{R}}$, the range of $A$ is the $x$-$y$ plane at $z = 0$.
# 
# Let $v = [0,0,z]$ for $z\in {\mathbb{R}}$. Then $u = Av$ is the vector $u = [0, 0, 0]$. Therefore, the nullspace of $A$ is the $z$-axis (i.e., the set of vectors $[0,0,z]$ $z\in {\mathbb{R}}$).
# 
# Therefore, this linear transformation "flattens" any $z$-component from a vector.

# ### 矢量空间、矢量与范数

# #### 矢量空间
# 
# 矢量空间的定义必须依赖一个**域$\mathbb{F}$ (field)** ．简单来说，域就是能进行加减乘除的对象的一个集合，比如实数域域$\mathbb{R}$和复数域域$\mathbb{C}$．这个域本身被称为该矢量空间的**标量域（scalar field）**或**标域**，它的元素被称为矢量空间的标量（scalar），它们不是矢量空间的元素，但是可以用来和矢量进行数乘．那么，我们就说矢量空间是 “域$\mathbb{F}$上的”．矢量空间选择的域几乎都是$\mathbb{R}$或$\mathbb{C}$，即讨论的是实数（或复数）域上的矢量空间．所以即使我们不了解域的具体定义也没关系，只要知道实数和复数是两种常见的域就足够了．

# **!定义 1!**　<font color='red'>矢量空间</font> 标量域$\mathbb{F}$上的矢量空间定义了矢量的集合$X$、两个矢量间的加法运算$X \times X \to X$以及标量和矢量间的数乘运算$F \times X \to X$。令矢量$u,v,w \in X$，标量$\lambda, \mu \in F$，矢量加法记为$u \bigoplus v$，数乘记为$\lambda \bigodot u$．两种运算必须满足以下性质：
# 
# - 加法运算
#     1. 满足加法交换律  $u \bigoplus v = v \bigoplus u$．
#     1. 满足加法结合律  $(u \bigoplus v ) \bigoplus w = u \bigoplus ( v \bigoplus w )$ ．
#     1. 存在零矢量，使得 $v \bigoplus 0 = v$ ．
#     1. 空间中任意矢量$v$  存在逆矢量  $− v$ ，使得  $v \bigoplus ( − v ) = 0$ ．
# - 数乘运算
#     1. 乘法分配律 $\lambda \bigodot ( u \bigoplus v ) = (\lambda \bigodot u) \bigoplus (\lambda \bigodot v)$ 
#     1. 乘法分配律 $( \lambda + \mu ) v = (\lambda \bigodot v) \bigoplus (\mu \bigodot v)$
#     1. 乘法结合律 $\lambda \bigodot  ( \mu \bigodot v ) = (\lambda \cdot \mu) \bigodot v$
#     1. 存在数量$1$， 使得 $1\bigodot u = u$
#     
# 注意，上述式子重，$+$和$\cdot$ 是定义在域$\mathbb{F}$上的四则运算。

# 矢量空间中的元素之间的线性组合所得到的元素仍然属于矢量空间。因此，矢量空间通常也称为线性空间。

# 矢量空间的定义非常抽象，实际上工程中经常遇到的数学对象多半可以看作是矢量空间的元素。
# - 一般定义里的矢量
# - 矩阵
# - 。。。

# #### 矢量空间的范数

# **范数(norm)** 可以看作几何矢量的模长在一般矢量空间上的拓展．

# **!定义 2!**  设$X$是实数或复数域上的矢量空间。$X$上的范数是满足如下条件的非负函数$\Vert \cdot \Vert$:
# 1. $\Vert x \Vert \geq 0$(正定)
# 1. $\Vert x \Vert = 0$ 当且仅当$x=0$
# 1. $\Vert \lambda x \Vert = \left| \lambda \right| \Vert x \Vert$，对任意$\lambda \in \mathbb{F}$，$x \in \mathbb{R}^n$
# 1. $\Vert x_1 + x_2 \Vert \leq \Vert x_1 \Vert + \Vert x_2 \Vert$（三角不等式）
# 
# 如果一个矢量空间中定义了范数，我们就把它称为**赋范空间（normed space）**．

# $\mathbb{R}^n$空间上常见的向量范数：
# - $1$-范数 ($L_1$范数)：
# 
# \begin{equation}
#     \Vert x \Vert_1 = \sum_{i=1}^n |x_i| = |x_1| + |x_2| + \cdots + |x_n|
# \end{equation}
#     
# - $2$-范数 ($L_2$范数)： 
#     
# $$\Vert x \Vert_2 = \left( \sum_{i=1}^n x_i^2 \right)^{1/2} = \sqrt{x_1^2 + x_2^2 + \cdots + x_n^2}  $$ 
#     
# - $p$-范数 ($L_p$范数)： 
#     
# $$\Vert x \Vert_p = \left( \sum_{i=1}^n |x_i|^p \right)^{1/p}  = \sqrt[p]{|x_1|^p + |x_2|^p + \cdots + |x_n|^p} $$  
#     
# - $\infty$-范数（也称为最大范数）($L_\infty$范数)： 
#     
# $$\Vert x \Vert_\infty = \max_{1 \leq i \leq n} |x_i| $$  
#     

# **! 例 !** Transpose the row vector we defined above into a column vector and calculate the $L_1$, $L_2$, and $L_\infty$ norm of it. Verify that the $L_\infty$ norm of a vector is equivalent to the maximum value of the elements in the vector.

# In[6]:


from numpy.linalg import norm

vector_row = np.array([[1,-5,3,2,4,9,8,7]])
new_vector = vector_row.T

print(new_vector)
norm_1   = norm(new_vector, 1)
norm_2   = norm(new_vector, 2)
norm_inf = norm(new_vector, np.inf)
print('L_1 is: %.1f'%norm_1)
print('L_2 is: %.1f'%norm_2)
print('L_inf is: %.1f'%norm_inf)


# **范数的性质**：
# - 连续性：设$f$是$\mathbb{R}^n$上的任一向量范数，则$f$关于$x$的每个分量是连续函数。
# - 等价性：设$\Vert \cdot \Vert_s$和$\Vert \cdot \Vert_s$是$\mathbb{R}^n$上的任意两个范数，则存在常数$c_1$和$c_2$，使得对于任意的$x \in \mathbb{R}^n$有
# \begin{equation*}
#     c_1 \Vert x \Vert_s \leq \Vert x \Vert_t \leq c_2 \Vert x \Vert_s
# \end{equation*}
# - $Cauchy-Schwarz$不等式：
# $$|(x,y)| \leq \Vert x \Vert_2 \cdot \Vert y \Vert_2$$

# **！例！** 已知矢量$v= [ 0.1, 0.3, 0.5, 0.8 ]^T$，求$\Vert v \Vert_1$，$\Vert v \Vert_2$，$\Vert v \Vert_4$，和$\Vert v \Vert_\infty$

# In[39]:


from numpy.linalg import norm
new_vector = np.array([0.1, 0.3, 0.5, 0.8])
print(new_vector)
norm_1   = norm(new_vector, 1)
norm_2   = norm(new_vector, 2)
norm_4   = norm(new_vector, 4)
norm_inf = norm(new_vector, np.inf)
print('L_1 is: %.4f'%norm_1)
print('L_2 is: %.4f'%norm_2)
print('L_4 is: %.4f'%norm_4)
print('L_inf is: %.4f'%norm_inf)
ord = 4
sum(abs(new_vector)**ord)**(1./ord)


# #### 矩阵的范数

# 矩阵的范数一般有三种定义方法：一种是将矩阵空间看作是矢量空间，利用矢量空间的范数定义来定义矩阵的范数；另一种是根据矩阵的运算特性，直接定义矩阵范数满足的条件；还有一种定义方式是利用矩阵与普通矢量的乘积来依靠矢量范数的定义导出矩阵范数。

# **1. 将矩阵空间看作是矢量空间，定义范数**

# 矢量$1$-范数：
# $$\Vert A \Vert_{1} = \sum_i^m \sum_j^n |a_{ij}|^p$$

# $F$-范数($Frobenious$范数)：
# \begin{equation}
#     \Vert A \Vert_F = \left( \sum_{i=1}^n \sum_{i=1}^n a_{ij}^2  \right)^{\frac{1}{2}}
# \end{equation}

# 矢量$p$-范数：
# $$\Vert A \Vert_{p} = \sqrt[p]{(\sum_i^m \sum_j^n |a_{ij}|^p)}$$

# 矢量$\infty$-范数：
# $$\Vert A \Vert_{\infty} = \max_{i,j}|a_{ij}|$$

# **2. 直接定义矩阵的范数**

# 设$f$是$\mathbb{R}^{n \times n} \to \mathbb{R}$，若$f$满足
# - <font color="blud">正定性</font>：$f(A) \leq 0$，$\forall A \in \mathbb{R}^{n \times n}$，且等号成立当且仅当$A=0$
# - <font color="blud">齐次性</font>：$f(\alpha A) = |\alpha| \cdot f(A)$，$\forall A \in \mathbb{R}^{n \times n}$，$\forall \alpha \in \mathbb{R}$
# - <font color="blud">三角不等式</font>：$f(A+B) \leq f(A) + f(B)$
# - <font color="blud">相容性</font>：$f(AB) \leq f(A)  f(B)$
# 
# 则称$f$为$\mathbb{R}^{n \times n} \to \mathbb{R}$上的（矩阵）范数，通常记为$\Vert \cdot \Vert$。

# 前述定义的$Frobenious$范数就是$\mathbb{R}^{n \times n}$上的一个矩阵范数

# **3. 基于矢量范数导出的矩阵范数**

# 设$x \in \mathbb{R}^{n}$， $\mathbf{A} \in \mathbb{R}^{n \times n}$，给出一种矢量范数$\Vert x \Vert_\nu$，相应地可以定义一个矩阵的非负函数
# 
# \begin{equation}
#     \Vert A \Vert_\nu = \sup_{x\in \mathbb{R}^n,\ x \neq 0} \frac{\Vert Ax \Vert_\nu}{\Vert x \Vert_\nu} = \max_{\Vert x \Vert_\nu = 1 }\Vert Ax \Vert_\nu
# \end{equation}
# 
# 可以验证，$\Vert A \Vert_\nu$满足上面的矩阵范数的直接定义，所以$\Vert A \Vert_\nu$称为$\mathbb{R}^{n \times n}$上矩阵的范数，称为$\mathbf{A}$的**算子范数**，也称为**从属范数**，**导出范数**。

# **4. 常见的算子范数**

# - $1$-范数(列范数)：
# \begin{equation}
#     \Vert A \Vert_1 = \max_{1 \leq j \leq n } \sum_{i=1}^n |a_{ij}|
# \end{equation}
# 
# - $2$-范数(谱范数)：
# \begin{equation}
#     \Vert A \Vert_2 = \sqrt{\rho(A^T A)} = \sqrt{\lambda_{max}(A^T A)} 
# \end{equation}
# 
# - $\infty$-范数(行范数)：
# \begin{equation}
#     \Vert A \Vert_\infty = \max_{1 \leq i \leq n } \sum_{j=1}^n |a_{ij}|
# \end{equation}

# **！例！** 设$A = \begin{bmatrix}
#             1   & -2 \\
#             -3  &  4 \\
#         \end{bmatrix}$
#         计算$\Vert A \Vert_1$，$\Vert A \Vert_2$，$\Vert A \Vert_\infty$，$\Vert A \Vert_F$。

# **！解！** 
# 
# \begin{equation*}
#     \Vert A \Vert_1 = \max \{ |1|+|-2|, |-3|+|4| \} = 7
# \end{equation*}
# 
# \begin{equation*}
#     \Vert A \Vert_2 = \sqrt{ \max \{ 15 + \sqrt{221}, 15 - \sqrt{221} \} } = \sqrt{15 + \sqrt{221}} \approx 5.46
# \end{equation*}
# 
# \begin{equation*}
#     \Vert A \Vert_\infty = \max \{ |1|+|-3|, |-2|+|4| \} = 6
# \end{equation*}
# 
# \begin{equation*}
#     \Vert A \Vert_F = \sqrt{1^2 + (-2)^2 + (-3)^2 + (4)^2 } = \sqrt{30} \approx 5.477
# \end{equation*}

# **5. 矩阵范数的性质**

# - 连续性：设$f$是$\mathbb{R}^{n \times n}$上的任一矩阵范数，则$f$关于$A$的每个分量是连续函数。

# - 等价性：设$\Vert \cdot \Vert_s$和$\Vert \cdot \Vert_s$是$\mathbb{R}^{n \times n}$上的任意两个矩阵范数，则存在常数$c_1$和$c_2$，使得对于任意的$x \in \mathbb{R}^n$有
# \begin{equation*}
#     c_1 \Vert x \Vert_s \leq \Vert x \Vert_t \leq c_2 \Vert x \Vert_s
# \end{equation*}

# - 定理：若$A$是对称矩阵，则$\Vert A \Vert_2 = \rho(A)$，其中$\rho(A) = \max {|\lambda_i(A)|}$为矩阵$A$的**谱半径**，是其特征值的绝对值大的那一个的绝对值。

# - 定理：设$\Vert \cdot \Vert$是$\mathbb{R}^n$上任意向量范数，其对应的算子范数也记为$\Vert \cdot \Vert$，则有
# \begin{equation*}
#     \Vert A x \Vert \leq \Vert A \Vert \cdot \Vert x \Vert
# \end{equation*}

# - 定理：设$\Vert \cdot \Vert$是任意算子范数，则
# $$\rho(A) \leq \Vert A \Vert$$

# - 定理：对任意的$\epsilon > 0$，总存在一个算子范数$\Vert \cdot \Vert_\epsilon$，使得
# \begin{equation}
#     \Vert A \Vert_\epsilon \leq \rho(A) + \epsilon
# \end{equation}

#  - 定理：设$\Vert \cdot \Vert$是任意算子范数，若$\Vert B \Vert < 1$，则$I \pm B$非奇异，且
# \begin{equation*}
#     \left\Vert (I\pm B)^{-1} \right\Vert \leq \frac{1}{ 1 - \Vert B \Vert}
# \end{equation*}

# **6. 矩阵的条件数**

# **！定义！**：考虑线性方程组$A x =b$，如果$A$或者$b$的微小变化会导致解的巨大变化，则称此线性方程组是**病态的**，并称矩阵$A$是**病态的**，反之则称矩阵$A$是良态的。例如下式中，系数矩阵的微小变化造成了最终解的巨大变化，系数矩阵是病态的。
# 
# $$
# \begin{bmatrix}
#     1 & 1 \\
#     1 & 1.0001 \\
# \end{bmatrix}
# \begin{bmatrix}
#     x_1 \\
#     x_2
# \end{bmatrix}=
# \begin{bmatrix}
#     2 \\
#     2
# \end{bmatrix} \quad \Longrightarrow \quad
# \begin{bmatrix}
#     x_1 \\
#     x_2
# \end{bmatrix}=
# \begin{bmatrix}
#     2 \\
#     0
# \end{bmatrix}
# $$
# 
# $$
# \begin{bmatrix}
#     1 & 1 \\
#     1 & 1.0001
# \end{bmatrix}
# \begin{bmatrix}
#     x_1 \\
#     x_2
# \end{bmatrix}=
# \begin{bmatrix}
#     2 \\
#     2.0001
# \end{bmatrix} \quad \Longrightarrow \quad
# \begin{bmatrix}
#     x_1 \\
#     x_2
# \end{bmatrix}=
# \begin{bmatrix}
#     1 \\
#     1
# \end{bmatrix}
# $$

# **！矩阵的条件数！** ：设$A$非奇异，则称
# 
# \begin{equation}
#   Cond(A) _s = \Vert A^{-1} \Vert_s \Vert A \Vert_s
# \end{equation}
# 
# 为$A$的条件数，其中$s$是$1$，$2$或$\infty$。

# **！定理！**：考虑线性方程组$A x = b$，设$A$是精确的，$b$有微小的扰动$\delta b$，新的方程组的解为$x + \delta x$，即$A(x + \delta x) = b + \delta b$，则
# 
# \begin{equation}
#     \frac{\Vert \delta x \Vert}{\Vert x \Vert} \leq \left\Vert A^{-1} \right\Vert \left\Vert A \right\Vert \frac{\Vert \delta b \Vert}{\Vert b \Vert}
# \end{equation}

# **！定理！**：考虑线性方程组$A x = b$，设$b$是精确的，$A$有微小的扰动$\delta A$，新的方程组的解为$x + \delta x$。假定$ \left\Vert A^{-1} \right\Vert \left\Vert \delta A \right\Vert < 1 $，则
# 
# \begin{equation}
#     \frac{\Vert \delta x \Vert}{\Vert x \Vert} \leq \frac{\left\Vert A^{-1} \right\Vert \left\Vert A \right\Vert \frac{\Vert \delta A \Vert}{\Vert A \Vert}}{ 1 - \left\Vert A^{-1} \right\Vert \left\Vert A \right\Vert \frac{\Vert \delta A \Vert}{\Vert A \Vert}}
# \end{equation}
# 
# 
# - 当$\delta A$充分小时，不等式右端约为$\left\Vert A^{-1} \right\Vert \left\Vert A \right\Vert \frac{\Vert \delta A \Vert}{\Vert A \Vert}$
# - 通常，当$A$的条件数较大时，就称$A$是病态的
# - 一般来说，条件数越大，病态越严重，此时就越难用一般方法求得线性方程组的比较精确的解。
# 

# **！条件数的基本性质！**
# - $Cond(A) \geq 1$
# - $Cond(\alpha A) = Cond(A)$，其中$\alpha$是任意非零实数
# - 若$A$是正交矩阵，则$Cond(A)_2 = 1$
# - 若$A$是正交矩阵，则对任意的非奇异矩阵$B$，有
# 
# \begin{equation}
#     Cond(BA)_2  =  Cond(AB)_2 = Cond(B)_2
# \end{equation}

# **！例！**
# $A = \begin{bmatrix}
#             1  &  1 \\
#             1  &  1.0001
#         \end{bmatrix}$，
#         计算$Cond(A)_\infty$和$Cond(A)_2$。

# 解：
# 
# $$
# A^{-1} = 
# \begin{bmatrix}
#     10001   &  -10000 \\
#     -10000  &   10000
# \end{bmatrix}
# $$

# $$
# Cond(A)_\infty = \Vert A^{-1} \Vert\_\infty  \Vert A \Vert\_\infty \approx 4 \times 10^4
# $$
# <!-- Cond(A)_\infty = \Vert A^{-1} \Vert_\infty  \Vert A \Vert_\infty \approx 4 \times 10^4 -->

# $A$是对称矩阵，且
# 
# $$
# \lambda(A) = \frac{2.0001 \pm \sqrt{2.0001^2 - 0.0004}}{2} > 0
# $$

# $$
# Cond(A)_2 = \lambda\_{max} / \lambda\_{min} \approx 4 \times 10^4
# $$
# <!-- Cond(A)_2 = \lambda_{max} / \lambda_{min} \approx 4 \times 10^4 -->

# ## 线性方程组的解

# ### 线性方程组示例

# $$
# \left[ \begin{array}{rrr} 4 & 2 & 7 \\ 3 & 5 & -6 \\ 1 & -3 & 2 \end{array} \right]
# \left[ \begin{array}{r} x_1 \\ x_2 \\ x_3 \end{array} \right]
# = \left[ \begin{array}{r} 2 \\ 3 \\ 4 \end{array} \right]
# $$

# $$
# \begin{pmatrix}
#     1 & 2 & 3 \\
#     3 & 2 & 1 \\
#     2 & 1 & 3 \\
# \end{pmatrix}
# \begin{pmatrix}
#     x_1 \\
#     x_2 \\
#     x_3 \\
# \end{pmatrix}=
# \begin{pmatrix}
#     12 \\
#     24 \\
#     36 \\
# \end{pmatrix}
# $$

# $$
# \begin{pmatrix}
#     6 & -2 & 2 & 4 \\
#     -6 & 4 & 1 & -18\\
#     3 & -13 & 9 & 3 \\
#     12 & -8 & 6 & 10 \\
# \end{pmatrix}
# \begin{pmatrix}
#     x_1 \\
#     x_2 \\
#     x_3 \\
#     x_4 \\
# \end{pmatrix}=
# \begin{pmatrix}
#     16 \\
#     -34 \\
#     -19 \\
#     26 \\
# \end{pmatrix}
# $$

# $$
# \begin{pmatrix}
#     0 & 2 & 0 & 1 \\
#     2 & 2 & 3 & 2 \\
#     4 & -3 & 0 & 1 \\
#     6 & 1 & -6 & -5 \\
# \end{pmatrix}
# \begin{pmatrix}
#     x_1 \\
#     x_2 \\
#     x_3 \\
#     x_4 \\
# \end{pmatrix}=
# \begin{pmatrix}
#     0 \\
#     -2 \\
#     -7 \\
#     6 \\
# \end{pmatrix}
# $$

# ### 线性方程组的解的存在唯一性定理

# **！定理！**：（<font color="red">解的存在性与唯一性</font>）下列论断之间是相互等价的
# - 方程$A x = b$存在唯一解
# - $det(A) \neq 0$
# - 矩阵$A$可逆
# - 方程$A x = 0$只有零解
# - 矩阵$A$满秩，即$A$的秩为$n$

# **！定理！**：（<font color="red">对称正定矩阵的性质</font>）若$A$对称正定，则
# - $A$ 非奇异，且 $A^{-1}$也对称正定；
# - $A$ 的所有顺序主子阵都对称正定；
# - $A$ 的所有特征值都是正实数；
# - $A$ 的所有顺序主子式都大于 $0$。

# **！定理！**：（<font color="red">对称正定矩阵的判定</font>）
# - 若$A$对称，且所有顺序主子式都大于$0$，则$A$对称正定。
# - 若$A$对称，且所有特征值都大于$0$，则$A$对称正定。

# **！定理！**：（<font color="red">Jordan 标准型</font>）
# 
# 设$A \in \mathbb{R}^{n \times n} $，则存在非奇异矩阵$X$，使得
# 
# $$
# X^{-1} A X = \begin{pmatrix}
#   J_1(\lambda_1) &                &        & \\
#                  & J_2(\lambda_2) &        & \\
#                  &                & \ddots  & \\
#                  &                &         & J_r(\lambda_r) \\
# \end{pmatrix}
# $$
# 
# 其中
# 
# $$
# J_i(\lambda_i) = \begin{pmatrix}
#   \lambda_i &      1    &        &           \\
#             & \lambda_i & \ddots &           \\
#             &           & \ddots &     1     \\
#             &           &        & \lambda_i \\
# \end{pmatrix} \in \mathbb{R}^{n_i \times n_i} 
# $$
# 
# 为$Jordan$块，且$\sum_{i=1}^r n_i = n$。

# ## 解线性方程组的直接法

# 对于中小型方程组，常用直接解法。从本质上来说，直接方法的原理是找一个可逆矩阵$M$，使得$MA$是一个上三角阵，这一过程一般称为“<font color="red">**消元**</font>”过程，消元之后再进行“<font color="red">**回代**</font>”，即求解$MAx=Mb$。

# 对于线性方程组$Ax = b$而言，有三种方程的解我们是可以直接求出的。
# - 情形一：当
# 
# \begin{equation}
# A = diag(a_{11}, a_{22}, \cdots , a_{nn} ) 
# \end{equation}
# 
# 时，我们有
# 
# \begin{equation}
# x_i = \frac{b_i}{a_{ii}},\quad i =1,2,\cdots,n,
# \end{equation}
# 
# 总共需要进行$ n $次运算。
# 
# - 情形二：当
# 
# $$
# A =
# \begin{pmatrix}
#  l_{11} &        &        &         \\
#  l_{21} & l_{22} &        &         \\
#  \vdots & \vdots & \ddots &         \\
#  l_{n1} & l_{n1} & \cdots & l_{nn}  \\
# \end{pmatrix} 
# $$
# 
# 时，我们有
# 
# \begin{equation}
# x_i = \frac{b_i - \sum_{j=1}^{i-1} l_{ij} x_j }{l_{ii}},\quad i =1,2,\cdots,n,
# \end{equation}
# 
# 总共需要进行$ \frac{n(n+1)}{2} $次运算。
# 
# - 情形三：当
# 
# $$
#  A =
#  \begin{pmatrix}
#      u_{11} & u_{12} & \cdots & u_{1n}  \\
#             & l_{22} & \cdots & u_{2n}  \\
#             &        & \ddots & \vdots  \\
#             &        &        & u_{nn}  \\
#  \end{pmatrix} 
# $$
# 
# 时，我们有
# 
# \begin{equation}
# x_i = \frac{b_i - \sum_{j=i+1}^{n} u_{ij} x_j }{u_{ii}},\quad i =1,2,\cdots,n,
# \end{equation}
# 
# 总共需要进行$ \frac{n(n+1)}{2} $次运算。

# 对线性方程组$Ax = b$而言，进行如下的变换，解不变
# - 交换两个方程的次序
# - 一个方程的两边同时乘以一个非$0$的数
# - 一个方程的两边同时乘以一个非$0$的数，加到另一个方程

# 因此，如果我们对增广矩阵$(A,b)$做如下变换，解不变
# - 交换矩阵的两行
# - 某一行的两边同时乘以一个非$0$的数
# - 某一行的两边同时乘以一个非$0$的数，加到另一行

# 消去法就是对增广矩阵作上述行的变换，变为我们已知的$3$种类型之一，而后求根。

# ### 消元法

# 我们把线性方程组$Ax = b$写成
# 
# $$
# \left\{
# \begin{aligned}
# a_{11} x_1 + a_{12} x_2 + \cdots + a_{1n} x_n = b_1 &= a_{1,n+1} \\
# a_{21} x_1 + a_{22} x_2 + \cdots + a_{2n} x_n = b_2 &= a_{2,n+1} \\
# \cdots &= \cdots \\
# a_{n1} x_1 + a_{11} x_2 + \cdots + a_{nn} x_n = b_n &= a_{n,n+1} \\
# \end{aligned}
# \right.
# $$

# #### 高斯消元法（Gauss Elimination）

# $Gauss$消元法的主要思路：将线性方程组的系数矩阵$A$转化为上三角矩阵，然后回代求解。

# 记$A^{(1)} = \left( a_{ij}^{(1)} \right)_{n \times n}$，$b^{(1)} = \left( b_1^{(1)}, \cdots, b_n^{(1)} \right)^T = b$ ，即 $a_{ij} = a_{ij}^{(1)}$，$b_i^{(1)} = b_i$
# 
# <font color="red" face = "bold">第1步</font>：消第$1$列。
# 
# 设$a_{11}^{(1)} \neq 0$，计算
# 
# $$m_{i1} = a_{i1}^{(1)} / a_{11}^{(1)} \,  (i=2,...,n)$$
# 
# 依次将增广矩阵的第$i$行$-m_{i1}\times$第$1$行，得
# 
# $$
# \begin{pmatrix}
#     A^{(2)}  & b^{(2)}
# \end{pmatrix} = \left[ \begin{array}{c|c}
#     \begin{matrix}
#     a_{11}^{(1)}  & a_{12}^{(1)}   &  \cdots   &  a_{1n}^{(1)} \\
#                   & a_{22}^{(2)}   &  \cdots   &  a_{2n}^{(2)} \\
#                   & \vdots         &  \ddots   &  \vdots       \\
#                   & a_{n2}^{(2)}   &  \cdots   &  a_{nn}^{(2)} \\
#     \end{matrix} &
#     \begin{matrix}
#     b_{1}^{(1)}  \\
#     b_{2}^{(2)}  \\
#     \vdots       \\
#     b_{n}^{(2)}  \\
#     \end{matrix}
# \end{array} \right]
# $$
# 
# 其中，$a_{ij}^{(2)} = a_{ij}^{(1)} - m_{i1} a_{1j}^{(1)}$，$b_{i}^{(2)} = b_{i}^{(1)} - m_{i1} b_{1}^{(1)}$，$i,j=2,\cdots,n$。

# <font color="red" face = "bold">第2步</font>：消第$2$列。
# 
# 设$a_{22}^{(2)} \neq 0$，计算
# 
# $$m_{i2} = a_{i2}^{(2)} / a_{22}^{(2)}\, (i=3,...,n)$$ 
# 
# 依次将$A^{(2)}$的第$i$行$-m_{i2}\times$第$2$行，得
# 
# $$
# \begin{pmatrix}
#     A^{(3)}  & b^{(3)}
# \end{pmatrix}= \left[ \begin{array}{c|c}
#     \begin{matrix}
#     a_{11}^{(1)}  & a_{12}^{(1)} & a_{13}^{(1)}  &  \cdots   &  a_{1n}^{(1)} \\
#                   & a_{22}^{(2)} & a_{23}^{(2)}  &  \cdots   &  a_{2n}^{(2)} \\
#                   &              & a_{33}^{(3)}  &  \cdots   &  a_{3n}^{(3)} \\
#                   &              & \vdots        &  \ddots   &     \vdots    \\
#                   &              & a_{n3}^{(3)}  &  \cdots   &  a_{nn}^{(3)} \\
#     \end{matrix} &
#     \begin{matrix}
#     b_{1}^{(1)}  \\
#     b_{2}^{(2)}  \\
#     b_{3}^{(3)}  \\
#     \vdots       \\
#     b_{n}^{(3)}  \\
#     \end{matrix}
# \end{array} \right]
# $$
# 
# 其中，$a_{ij}^{(3)} = a_{ij}^{(2)} - m_{i2} a_{2j}^{(2)}$，$b_{i}^{(3)} = b_{i}^{(2)} - m_{i2} b_{2}^{(2)}$，$i,j=3,\cdots,n$。

# 依次类推，<font color="red" face = "bold">第$k-1$步</font>后可得
# 
# $$
# \begin{pmatrix}
#     A^{(k)}  & b^{(k)}
# \end{pmatrix} = \left[ \begin{array}{c|c}
#     \begin{matrix}
#     a_{11}^{(1)}  &    \cdots    & a_{1k}^{(1)}  &  \cdots   &  a_{1n}^{(1)} \\
#                   &    \ddots    &     \vdots    &  \vdots   &     \vdots    \\
#                   &              & a_{kk}^{(k)}  &  \cdots   &  a_{kn}^{(k)} \\
#                   &              & \vdots        &  \ddots   &     \vdots    \\
#                   &              & a_{nk}^{(k)}  &  \cdots   &  a_{nn}^{(k)} \\
#     \end{matrix} &
#     \begin{matrix}
#     b_{1}^{(1)}  \\
#     \vdots       \\
#     b_{k}^{(k)}  \\
#     \vdots       \\
#     b_{n}^{(k)}  \\
#     \end{matrix}
# \end{array} \right]
# $$

# <font color="red" face = "bold">第$k$步</font>：消第$k$列。
# - 设$a_{kk}^{(k)} \neq 0$，
# - 先计算$m_{ik} = a_{ik}^{(k)} / a_{kk}^{(k)}$，$i=k+1,\cdots,n$，
# - 再计算$a_{ij}^{(k+1)} = a_{ij}^{(k)} - m_{ik} a_{kj}^{(k)}$，$b_{i}^{(k+1)} = b_{i}^{(k)} - m_{ik} b_{k}^{(k)}$，$i,j=k+1,\cdots,n$，
# - 获得$A^{(k+1)}$

# <font color="red" face = "bold">第$n-1$步</font>后可得
# 
# $$
# \begin{pmatrix}
#     A^{(n)}  & b^{(n)}
# \end{pmatrix}= \left[ \begin{array}{c|c}
#     \begin{matrix}
#     a_{11}^{(1)}  &    a_{12}^{(1)}    &  \cdots   &  a_{1n}^{(1)} \\
#                   &    a_{22}^{(2)}    &  \cdots   &  a_{2n}^{(2)} \\
#                   &                    &  \ddots   &     \vdots    \\
#                   &                    &           &  a_{nn}^{(n)} \\
#     \end{matrix} &
#     \begin{matrix}
#     b_{1}^{(1)}  \\
#     b_{2}^{(2)}  \\
#     \vdots       \\
#     b_{n}^{(n)}  \\
#     \end{matrix}
# \end{array} \right]
# $$
# 
# 即
# \begin{equation}
# A^{(n)} x = b^{(n)}
# \end{equation}

# <font color="red" face = "bold">回代求解可得：</font>
# \begin{equation*}
# \begin{aligned}
#     x_n &= b_n^{(n)} / a_{nn}^{(n)} \\
#     x_i &= \left( b_i^{(i)} - \sum_{j=i+1}^{n}  a_{ij}^{(i)} x_j \right) \Bigg/ a_{ii}^{(i)},\quad (i = n-1,\cdots, 1)
# \end{aligned}
# \end{equation*}

# **！几点注记！**：
# - 主元：$a_{ii}^{(i)}\quad (i=1,2,\cdots,n)$
# - $Gauss$消元法能进行到底的条件：主元全不为$0$

# **！定理！**：
# $a_{ii}^{(i)} \neq 0\ (i=1,2,\cdots,n)$ 的充要条件是$A$的顺序主子式都不为零，即 
# 
# $$
# D_1 = a_{11} \neq 0, \quad D_i = \left| \begin{matrix}
#     a_{11} & \cdots & a_{1i} \\
#     \vdots & \ddots & \vdots \\
#     a_{i1} & \cdots & a_{ii} \\
# \end{matrix} \right| \neq 0,\quad i=1,2,\cdots, n
# $$

# **！推论！**：
# 根据以上定理，主元$a_{ii}^{(i)}$可以依下式计算
# \begin{equation*}
#     a_{11}^{(1)} = D_1,\quad a_{ii}^{(i)} = D_i \big/ D_{i-1},\quad i = 2,\cdots, n
# \end{equation*}

# **！Gauss消元法的计算次数！**：
# 
# - 乘除运算的次数：
#     1. 第$k$步：消第$k$列
#         + 计算 $m_{ik} = a_{ik}^{(k)} \big/ a_{kk}^{(k)}$，共$n-k$步
#         + 计算 $a_{ij}^{(k+1)} = a_{ij}^{(k)} - m_{ik} a_{kj}^{(k)}$，共$(n-k)^2$步
#         + 计算 $b_{i}^{(k+1)} = b_{i}^{(k)} - m_{ik} b_{k}^{(k)}$，共$n-k$步
#     1. 回代求解：共$n(n+1)/2$步 
#     \begin{equation*}
#         \left\{\begin{aligned}
#             x_n &= b_n^{(n)} / a_{nn}^{(n)} \\
#             x_i &= \left( b_i^{(i)} - \sum_{j=i+1}^{n}  a_{ij}^{(i)} x_j \right) \Bigg/ a_{ii}^{(i)},\quad (i = n-1,\cdots, 1)
#         \end{aligned}\right.
#     \end{equation*}
# 
#     1. 从而，可以得到$Gauss$消元法的乘除运算量为：$\frac{n^3}{3} + n^2 - \frac{n}{3}$
# 
# - 加减运算的次数：$\frac{n^3}{3} + \frac{n^2}{2} - \frac{5n}{6}$

# **！例！**：用消元法解线性方程组
# \begin{equation*}
#     \left\{\begin{aligned}
#         x_1 - 2 x_2 + 2 x_3 &= -2 \\
#         2x_1 - 3 x_2 - 3 x_3 &= 4 \\
#         4x_1 + x_2 + 6 x_3 &= 3 \\
#     \end{aligned}\right.
# \end{equation*}

# **！解！**：
# \begin{equation}
# (A,b) = \begin{bmatrix}
#     1 & -2 & 2  & -2 \\
#     2 & -3 & -3 & 4  \\
#     4 & 1  & 6  & 3  \\
# \end{bmatrix}
# \Longrightarrow
# \begin{bmatrix}
#             1 & -2 & 2  & -2 \\
#             0 & 1  & -7 & 8  \\
#             0 & 9  & -2 & 11 \\
#         \end{bmatrix}
# \end{equation} 
# \begin{equation}
# \Longrightarrow\begin{bmatrix}
#     1 & -2 & 2  & -2   \\
#     0 & 1  & -7 & 8    \\
#     0 & 0  & 61 & -61  \\
# \end{bmatrix}
# \Longrightarrow
# \left\{\begin{aligned}
#     x_3 &= 1 \\
#     x_2 &= 8 + 7 x_3 = 1   \\
#     x_1 &= -2 + 2 x_2 - 2 x_3 = 2 \\
# \end{aligned} \right.
# \end{equation}

# **！例！**：用消元法解线性方程组
# \begin{equation*}
#     \left\{\begin{aligned}
#                      x_1 + \frac{2}{3} x_2 +   \frac{1}{3} x_3 &= 2 \\
#         \frac{9}{20} x_1 +             x_2 + \frac{11}{20} x_3 &= 2 \\
#         \frac{2}{3}  x_1 + \frac{1}{3} x_2 +               x_3 &= 2 \\
#     \end{aligned}\right.
# \end{equation*}

# **！解！**：
# \begin{equation*}
#     (A,b) = \begin{bmatrix}
#         1            & \frac{2}{3}  &  \frac{1}{3}  & 2  \\
#         \frac{9}{20} & 1            & \frac{11}{20} & 2  \\
#         \frac{2}{3}  & \frac{1}{3}  & 1             & 2  \\
#     \end{bmatrix}
#     \Longrightarrow
#     \begin{bmatrix}
#                 1            & \frac{2}{3}   &  \frac{1}{3}  & 2  \\
#                 0            & \frac{7}{10}  & \frac{2}{5}   & \frac{11}{10}  \\
#                 0            & -\frac{1}{9}  & \frac{7}{9}   & \frac{2}{3} \\
#             \end{bmatrix}
# \end{equation*} 
# 
# \begin{equation*}
#     \Longrightarrow\begin{bmatrix}
#         1            & \frac{2}{3}   &  \frac{1}{3}  & 2  \\
#         0            & \frac{7}{10}  & \frac{2}{5}   & \frac{11}{10}  \\
#         0            & 0             & \frac{53}{63} & \frac{53}{63}  \\
#     \end{bmatrix}
#     \Longrightarrow
#     \left\{\begin{aligned}
#         x_3 &= 1 \\
#         x_2 &= \frac{11}{7} - \frac{4}{7} x_3 = 1   \\
#         x_1 &= 2 - \frac{2}{3} x_2 - \frac{1}{3} x_3 = 1 \\
#     \end{aligned} \right.
# \end{equation*}

# #### 列主元消元法（Gauss Elimination with Partial Pivoting）

# 在以上的$Gauss$消元法中，消元过程能进行的条件是主元素$a_{ii}^{(i)} \neq 0$。例如，若$a_{11}^{(1)} = 0$，消元过程的第$1$步就不能进行。

# 有时，虽然$a_{ii}^{(i)} \neq 0$，但是$| a_{ii}^{(i)} |$很小，这时计算过程的舍入误差导致消去法数值不稳定，以致结果不可靠。

# **！例！**：用三位十进制浮点运算求解
# \begin{equation*}
#     \left\{\begin{aligned}
#         1.00\times10^{-5} x_1 + 1.00 x_2 &= 1.00 \\
#         1.00 x_1 + 1.00 x_2 &= 2.00
#     \end{aligned}\right.
# \end{equation*}

# **！解！**： 这个方程的解显然接近$(1.00,1.00)^T$，但是系数$a_{11}$是个小主元。如果用$Gauss$消元法求解，则有
# \begin{equation*}
#     \begin{aligned}
#         m_{21} &= a_{21}/a_{11} = 1.00\times10^{5} \\
#         a_{22}^{(2)} &= a_{22} - m_{21}a_{12} = 1.00 - 1.00\times10^{5} \\
#         b_{2}^{(2)} &= b_{2} - m_{21} b_{1} = 2.00 - 1.00\times10^{5}
#     \end{aligned}
# \end{equation*}

# 在三位十进制运算的限制下，得到$x_2 = b_{2}^{(2)} / a_{22}^{(2)} = 1.00$，代回第$1$个方程得$x_1 = 0$，这显然不是正确的解。因为使用了小主元$a_{11}$做除法，使得乘数$m_{21}$是个大数，在$a_{22}^{(2)}$的计算中，$a_{22}$的值完全被掩盖了。

# 如果先把两个方程的次序交换，再用$Gauss$消元法，就不会出现上述问题，解得$x_1 =1.00$，$x_2 =1.00$，这就是<font color="red">列主元消元法的思想</font>。

# <font color="magenta">列主元消去法</font>也称按列部分主元的消元法。一般地，在完成第$k-1$步消元运算后，在$\left( A^{(k)}, b^{(k)} \right)$的第$k$列元素$a_{kk}^{(k)}$之下的所有元素中选一个绝对值最大的元素作为主元素，即若
# \begin{equation*}
#     \left| a_{i_k, k}^{(k)} \right| = \max_{k \leq i \leq n} \left| a_{i, k}^{(k)} \right|
# \end{equation*}
# 则以$a_{i_k, k}^{(k)}$为主元素，这里$i_k \geq k$。由于$A^{(k)}$非奇异，有$a_{i_k, k}^{(k)} \neq 0$。这样，$|m_{ik}| = \left| a_{ik}^{(k)} \right| \big/ \left| a_{i_k,k}^{(k)} \right| \leq 1 $有达到控制舍入误差的作用。
# 
# 
# 选出主元素后，则进行顺序$Gauss$消元法的第$k$步：若$i_k > k$，则将$\left( A^{(k)}, b^{(k)} \right)$的第$i_k$行与第$k$行交换，然后进行消元运算。
# 
# 
# 完成了$n-1$步定主元，换行与消元运算后，得到$\left( A^{(n)}, b^{(n)} \right)$，这是与原方程等价的方程组，$A^{(n)}$是一个上三角阵，在回代求解。这就是<font color="magenta">列主元消元法的计算过程</font>。

# **！例！**：使用列主元消去法解方程组$Ax=b$，计算过程中取五位有效数字进行计算，其中
# \begin{equation*}
#     (A,b) = \begin{bmatrix}
#         -0.002 & 2        & 2  & 0.4    \\
#         1      & 0.78125  & 0  & 1.3816 \\
#         3.996  & 5.5625   & 4  & 7.4178 \\
#     \end{bmatrix}
# \end{equation*}

# **！解！**：记$(A^{(1)} , b^{(1)}) = (A,b)$。第一步选列主元为$a_{31}^{(1)} = 3.996$，交换第$1$行与第$3$行，再消元计算得
# \begin{equation*}
#     \left( A^{(2)},b^{(2)} \right) = \begin{bmatrix}
#         3.996 & 5.5625   & 4       & 7.4178    \\
#         0     & -0.61077 & -1.0010  & -0.47471 \\
#         0     & 2.0028   & 2.0020   & 0.40371  \\
#     \end{bmatrix}
# \end{equation*}

# 第二步选列主元为$a_{32}^{(2)} = 2.0028$，交换第$2$行与第$3$行，再消元计算得
# \begin{equation*}
#     \left( A^{(3)},b^{(3)} \right) = \begin{bmatrix}
#         3.996 & 5.5625   & 4         & 7.4178    \\
#         0     & 2.0028   & 2.0020    & 0.40371  \\
#         0     & 0        & -0.39047  & -0.35159 \\
#     \end{bmatrix}
# \end{equation*}
# 消元过程到此结束。

# 回代计算依次得到解
# \begin{equation*}
#     x_3 = 0.90043,\quad x_2 = -0.69850,\quad x_1 = 1.9273
# \end{equation*}
# 本题的精确解是
# \begin{equation*}
#     x_3 = 0.900423,\quad x_2 = -0.698496,\quad x_1 = 1.92730
# \end{equation*}
# 而使用不选主元的顺序$Gauss$消元法，得到的解是
# \begin{equation*}
#     x_3 = 0.88888,\quad x_2 = -0.68695,\quad x_1 = 1.9300
# \end{equation*}

# **！例！**：分别用$Gauss$消去法和列主元消去法求解线性方程组
# \begin{equation*}
#     \begin{bmatrix}
#          0.001   & 2.000   & 3.000 \\
#         -1.000   & 3.712   & 4.623 \\
#         -2.000   & 1.072   & 5.643 \\
#     \end{bmatrix}
#     \begin{bmatrix}
#          x_1   \\
#          x_2   \\
#          x_3   \\
#     \end{bmatrix}=
#     \begin{bmatrix}
#          1.000   \\
#          2.000   \\
#          3.000   \\
#     \end{bmatrix}
# \end{equation*}
# 用$4$位浮点数进行计算，精确解舍入到$4$位有效数字为$x^* = [-0.4904, -0.05104, 0.3675]^T$

# **！解！**：
# - 用$Gauss$消去法求解
# \begin{equation}
#     (A^{(0)}, b^{(0)}) = \begin{bmatrix}
#          0.001   & 2.000   & 3.000  & 1.000 \\
#         -1.000   & 3.712   & 4.623  & 2.000 \\
#         -2.000   & 1.072   & 5.643  & 3.000 \\
#     \end{bmatrix}
# \end{equation}
# 
# \begin{equation}
#     (A^{(1)}, b^{(1)}) = \begin{bmatrix}
#          0.001   & 2.000   & 3.000  & 1.000 \\
#          0       & 2004    & 3005   & 1002  \\
#          0       & 4001    & 6006   & 2003  \\
#     \end{bmatrix}
# \end{equation}
# 
# 计算解为
# \begin{equation}
#     \bar{x} = [-0.4000, -0.09980, 0.4000]^T
# \end{equation}
# 
# - 用列主元消去法求解
# \begin{equation}
#     (A^{(0)}, b^{(0)}) = \begin{bmatrix}
#         -2.000   & 1.072   & 5.643  & 3.000 \\
#         -1.000   & 3.712   & 4.623  & 2.000 \\
#          0.001   & 2.000   & 3.000  & 1.000 \\
#     \end{bmatrix}
# \end{equation}
# 
# \begin{equation}
#     (A^{(1)}, b^{(1)}) = \begin{bmatrix}
#         -2.000   & 1.072   & 5.643  & 3.000  \\
#          0.000   & 3.176   & 1.801  & 0.5000 \\
#          0.001   & 2.001   & 3.003  & 1.002  \\
#     \end{bmatrix}
# \end{equation}
# 
# \begin{equation}
#     (A^{(2)}, b^{(2)}) = \begin{bmatrix}
#         -2.000   & 1.072   & 5.643  & 3.000   \\
#          0.000   & 3.176   & 1.801  & 0.5000  \\
#          0.001   & 0.000   & 1.858  & 0.6870  \\
#     \end{bmatrix}
# \end{equation}
# 
# 计算得解为
# \begin{equation}
#     x^\star = [-0.4900, -0.05113, 0.3678]^T
# \end{equation}
# 
# 对比两种方法的解与准确解
# 
# \begin{equation}
#     \left\{\begin{aligned}
#         x^*     &= [-0.4904, -0.05104, 0.3675]^T \\
#         \bar{x} &= [-0.4000, -0.09980, 0.4000]^T  \\
#         x^\star &= [-0.4900, -0.05113, 0.3678]^T  \\
#     \end{aligned}\right.
# \end{equation}

# #### 全主元消元法（Gauss Elimination with Complete Pivoting）

# 除了列主元的消元法外，还有一种\textcolor{red}{全主元消元法}。在其过程的第$k$步($k \leq 1$)，不是按列来选主元，而是在$A^{(k)}$右下角的$n-k+1$阶子阵中选主元$a_{i_k, j_k}^{(k)}$，即
# \begin{equation*}
#     \left| a_{i_k, j_k}^{(k)} \right| = \max_{k\leq i,j \leq n} \left| a_{i, j}^{(k)} \right|
# \end{equation*}
# 然后将$\left( A^{(k)}, b^{(k)} \right)$的第$i_k$行与第$k$行交换，将第$j_k$列与第$k$列交换，同时将自变量$x_k$与$x_{j_k}$的位置交换并记录自变量的排列顺序。直到消去法完成后，再按记录恢复自变量为自然次序。
# 
# 全主元消去法比列主元消元法的运算量大得多，且需要额外存储变量的顺序，而实际的运算过程中列主元消去法的舍入误差一般已经比较小，因此<font color="red">实际计算中多采用列主元法</font>。

# #### 高斯-约旦消元法（Gauss-Jordan Elimination）

# 我们考虑$Gauss$消元法的一种修正：消去对角线下方和上方的元素，并称这种方法为<font color="red">$Gauss-Jordan$消去法</font>。
# 
# 设用$Gauss-Jordan$消去法已经完成$k-1$步，得到与方程$Ax = b$等价的方程组$A^{(k)}  x = b^{(k)}$，此时对应的增广矩阵为
# \begin{equation*}
#     \left( A^{(k)}, b^{(k)} \right) =
#     \begin{bmatrix}
#         1   &        &    & a_{1k}^{k}     & \cdots &  b_1^{k}      &  \\
#             & \ddots &    & \vdots         &        &  \vdots       &  \\
#             &        &  1 & a_{k-1,k}^{k}  & \cdots &  b_{k-1}^{k}  &  \\
#             &        &    & a_{kk}^{k}     & \cdots &  b_{k}^{k}    &  \\
#             &        &    & \vdots         &        &  \vdots       &  \\
#             &        &    & a_{nk}^{k}     & \cdots &  b_{n}^{k}    &  \\
#     \end{bmatrix}
# \end{equation*}
# 
# 在第$k$步计算时，考虑对上述矩阵的第$k$列中的第$k$行上下都进行消元计算。若用列主元消去法，仍然是第$k$列元素$a_{kk}^{k}$之下的所有元素中选一个绝对值最大的元素作为主元素，即
# \begin{equation*}
#     \left| a_{i_k,k} \right|= \max_{k \leq i \leq n} \left| a_{i,k} \right|
# \end{equation*}
# 但是，将第$k$行与第$i_k$行交换后，要通过主行将第$k$列的第$i\ (i=1,\cdots,k-1,k+1,\cdots,n)$个元素化为$0$，再将主行的对角线上元素化为$1$。最后得到$( A^{(k+1)}, b^{(k+1)} )$，这里$A^{(k+1)}$是单位矩阵，从而$b^{(k+1)}$就是计算解。
#  
# 可见，$Gauss-Jordan$消去法用不着回代求解，其计算量大约需要$n^3/2$次乘除法运算，要比$Gauss$消去法的计算量大。但是用$Gauss-Jordan$消去法求一个矩阵的逆矩阵是很合适的。
# 

# **！例！**： 用$Gauss-Jordan$消去法求下列矩阵的逆矩阵
#     \begin{equation*}
#         A = \begin{bmatrix}
#             1 & 2 & 3 \\
#             2 & 4 & 5 \\
#             3 & 5 & 6 \\
#         \end{bmatrix}
#     \end{equation*}

# **！解！**：
# 
# 用$Gauss-Jordan$消元法有
# \begin{equation*}
#     C = C^{(1)} = (A,I) = A = \begin{bmatrix}
#             1 & 2 & 3 & 1 & 0 & 0 \\
#             2 & 4 & 5 & 0 & 1 & 0 \\
#             3 & 5 & 6 & 0 & 0 & 1 \\
#         \end{bmatrix}
# \end{equation*}
# \begin{equation*}
#     \Longrightarrow C^{(2)} = \begin{bmatrix}
#             1 & 5/3 & 0 & 0 & 0 & 1/3 \\
#             0 & 2/3 & 1 & 0 & 1 & -2/3 \\
#             0 & 1/3 & 1 & 1 & 0 & -1/3 \\
#         \end{bmatrix}
# \end{equation*}
# \begin{equation*}
#     \Longrightarrow C^{(3)} = \begin{bmatrix}
#             1 & 0 & -1/2 & 0 & -5/2 &  2 \\
#             0 & 1 &  3/2 & 0 &  3/2 & -1 \\
#             0 & 0 &  1/2 & 1 & -1/2 &  0 \\
#         \end{bmatrix}
# \end{equation*}
# \begin{equation*}
#     \Longrightarrow C^{(4)} = \begin{bmatrix}
#             1 & 0 & 0 &  1 & -3 &  2 \\
#             0 & 1 & 0 & -3 &  3 & -1 \\
#             0 & 0 & 1 &  2 & -1 &  0 \\
#         \end{bmatrix}
#         = (I, A^{-1})
# \end{equation*}
# 故而有
# \begin{equation*}
#     A^{-1} = \begin{bmatrix}
#               1 & -3 &  2 \\
#              -3 &  3 & -1 \\
#               2 & -1 &  0 \\
#         \end{bmatrix}
# \end{equation*}

# #### 消元法的python实现

# 远期目标是，我们会有四个版本的消元法求解线性方程组。
# - 直接Gauss消元法
# - 列主元消元法
# - 全主元消元法
# - Gauss-Jordan消元法
# 
# 但目前，受到时间精力限制，只能暂时从网上寻找一些开放的代码，以后时间精力允许的时候会补齐。

# <font color="magenta"> 也非常欢迎学有余力的xiao huo ba </font>

# In[1]:


def myGauss(m):
    #eliminate columns
    for col in range(len(m[0])):
        for row in range(col+1, len(m)):
            r = [(rowValue * (-(m[row][col] / m[col][col]))) for rowValue in m[col]]
            m[row] = [sum(pair) for pair in zip(m[row], r)]
    #now backsolve by substitution
    ans = []
    m.reverse() #makes it easier to backsolve
    for sol in range(len(m)):
            if sol == 0:
                ans.append(m[sol][-1] / m[sol][-2])
            else:
                inner = 0
                #substitute in all known coefficients
                for x in range(sol):
                    inner += (ans[x]*m[sol][-2-x])
                #the equation is now reduced to ax + b = c form
                #solve with (c - b) / a
                ans.append((m[sol][-1]-inner)/m[sol][-sol-2])
    ans.reverse()
    return ans


# In[5]:



print( myGauss([[-3.0,2.0,-6.0,6.0],
               [5.0,7.0,-5.0,6.0],
               [1.0,4.0,-2.0,8.0]])
     )

print( str(myGauss([[2.0,4.0,6.0,8.0,10.0,0.0],
               [1.0,3.0,5.0,8.0,3.0,-1.0],
               [3.0,8.0,9.0,20.0,3.0,5.0],
               [4.0,8.0,9.0,-2.0,3.0,8.0],
               [5.0,-3.0,3.0,-2.0,1.0,0]])) == '[1.8835063437139565, 1.7012687427912341, -1.4160899653979238, -0.050749711649365627, -0.16695501730103807]'
     )

print( 'example from the wikipedia' )

print( myGauss([[2.0,1.0,-1.0,8.0],
               [-3.0,-1.0,2.0,-11.0],
               [-2.0,1.0,2.0,-3.0]])
     )
print( myGauss([[1.0,4.0,-2.0,8.0],
               [5.0,7.0,-5.0,6.0],
               [-3.0,2.0,-6.0,6.0]])
     )


# In[12]:


import numpy as np
def gaussElimination(a,b):
    n = len(b)
    # Elimination phase
    for k in range(0,n-1):
        for i in range(k+1,n):
            if a[i,k] != 0.0:
                #if not null define λ
                lam = a [i,k]/a[k,k]
                #we calculate the new row of the matrix
                a[i,k+1:n] = a[i,k+1:n] - lam*a[k,k+1:n]
                #we update vector b
                b[i] = b[i] - lam*b[k]
                # backward substitution
    for k in range(n-1,-1,-1):
        b[k] = (b[k] - np.dot(a[k,k+1:n],b[k+1:n]))/a[k,k]
    
    return b

#initial coefficients
a=np.array([[1.0,1.0,1.0],[1.0,-1.0,-1.0],[1.0,-2.0,3.0]])
b=np.array([1.0,1.0,-5.0])
aOrig = a.copy() # save original matrix A
bOrig = b.copy() #save original vector b
x = gaussElimination(a,b)
#print A transformed for check
print(a)
print("x =\n",x)
#det = np.prod(np.diagonal(a)) #determinant
#print("\ndet =",det)
#check result and numerical precision
print("\nCheck result: [a]{x} - b =\n",np.dot(aOrig,x) - bOrig)


# In[14]:


import numpy as np

def GEPP(A, b, doPricing = True):
    '''
    Gaussian elimination with partial pivoting.
    
    input: A is an n x n numpy matrix
           b is an n x 1 numpy array
    output: x is the solution of Ax=b 
            with the entries permuted in 
            accordance with the pivoting 
            done by the algorithm
    post-condition: A and b have been modified.
    '''
    n = len(A)
    if b.size != n:
        raise ValueError("Invalid argument: incompatible sizes between"+
                         "A & b.", b.size, n)
    # k represents the current pivot row. Since GE traverses the matrix in the 
    # upper right triangle, we also use k for indicating the k-th diagonal 
    # column index.
    
    # Elimination
    for k in range(n-1):
        if doPricing:
            # Pivot
            maxindex = abs(A[k:,k]).argmax() + k
            if A[maxindex, k] == 0:
                raise ValueError("Matrix is singular.")
            # Swap
            if maxindex != k:
                A[[k,maxindex]] = A[[maxindex, k]]
                b[[k,maxindex]] = b[[maxindex, k]]
        else:
            if A[k, k] == 0:
                raise ValueError("Pivot element is zero. Try setting doPricing to True.")
        #Eliminate
        for row in range(k+1, n):
            multiplier = A[row,k]/A[k,k]
            A[row, k:] = A[row, k:] - multiplier*A[k, k:]
            b[row] = b[row] - multiplier*b[k]
    # Back Substitution
    x = np.zeros(n)
    for k in range(n-1, -1, -1):
        x[k] = (b[k] - np.dot(A[k,k+1:],x[k+1:]))/A[k,k]
    return x

if __name__ == "__main__":
    A = np.array([[1.,-1.,1.,-1.],[1.,0.,0.,0.],[1.,1.,1.,1.],[1.,2.,4.,8.]])
    b =  np.array([[14.],[4.],[2.],[2.]])
    print( GEPP(np.copy(A), np.copy(b), doPricing = False) )
    print( GEPP(A,b) )


# In[21]:


import numpy as np

def GENP(A, b):
    '''
    Gaussian elimination with no pivoting.
    % input: A is an n x n nonsingular matrix
    %        b is an n x 1 vector
    % output: x is the solution of Ax=b.
    % post-condition: A and b have been modified. 
    '''
    n =  len(A)
    if b.size != n:
        raise ValueError("Invalid argument: incompatible sizes between A & b.", b.size, n)
    for pivot_row in range(n-1):
        for row in range(pivot_row+1, n):
            multiplier = A[row][pivot_row]/A[pivot_row][pivot_row]
            #the only one in this column since the rest are zero
#             A[row][pivot_row] = multiplier
            A[row][pivot_row] = 0
            for col in range(pivot_row + 1, n):
                A[row][col] = A[row][col] - multiplier*A[pivot_row][col]
            #Equation solution column
            b[row] = b[row] - multiplier*b[pivot_row]
    print(A)
    print(b)
    x = np.zeros(n)
    k = n-1
    x[k] = b[k]/A[k,k]
    while k >= 0:
        x[k] = (b[k] - np.dot(A[k,k+1:],x[k+1:]))/A[k,k]
        k = k-1
    return x

def GEPP(A, b):
    '''
    Gaussian elimination with partial pivoting.
    % input: A is an n x n nonsingular matrix
    %        b is an n x 1 vector
    % output: x is the solution of Ax=b.
    % post-condition: A and b have been modified. 
    '''
    n =  len(A)
    if b.size != n:
        raise ValueError("Invalid argument: incompatible sizes between A & b.", b.size, n)
    # k represents the current pivot row. Since GE traverses the matrix in the upper 
    # right triangle, we also use k for indicating the k-th diagonal column index.
    for k in range(n-1):
        #Choose largest pivot element below (and including) k
        maxindex = abs(A[k:,k]).argmax() + k
        if A[maxindex, k] == 0:
            raise ValueError("Matrix is singular.")
        #Swap rows
        if maxindex != k:
            A[[k,maxindex]] = A[[maxindex, k]]
            b[[k,maxindex]] = b[[maxindex, k]]
        for row in range(k+1, n):
            multiplier = A[row][k]/A[k][k]
            #the only one in this column since the rest are zero
#             A[row][k] = multiplier
            A[row][k] = 0
            for col in range(k + 1, n):
                A[row][col] = A[row][col] - multiplier*A[k][col]
            #Equation solution column
            b[row] = b[row] - multiplier*b[k]
    print(A)
    print(b)
    x = np.zeros(n)
    k = n-1
    x[k] = b[k]/A[k,k]
    while k >= 0:
        x[k] = (b[k] - np.dot(A[k,k+1:],x[k+1:]))/A[k,k]
        k = k-1
    return x

if __name__ == "__main__":
    A = np.array([[1.,-1.,1.,-1.],[1.,0.,0.,0.],[1.,1.,1.,1.],[1.,2.,4.,8.]])
    b =  np.array([[14.],[4.],[2.],[2.]])
#     print( GEPP(np.copy(A), np.copy(b), doPricing = False) )
    print( GEPP(np.copy(A), np.copy(b)) )
    print( GEPP(A,b) )


# In[ ]:





# In[ ]:





# In[ ]:





# ### 矩阵分解法

# #### 高斯消元法与矩阵分解（Gauss Elimination as Matrix Decomposition）

# #### 矩阵的LU分解（LU decomposition of matrices）

# #### LU分解法解线性方程组

# #### 矩阵的PLU分解

# #### PLU分解法解线性方程组

# #### 对称矩阵及对称正定矩阵的分解

# #### 矩阵分解法的python实现

# ### 迭代法求线性方程组

# #### 迭代法的基本构造方法

# #### 迭代法的收敛特性

# #### Gauss-Seidel迭代

# #### Jacobi迭代

# #### 超松弛(SOR)迭代

# ## 小结

# ## 思考和习题

# 本文档在编制过程中，得到了选修我主讲的《数值计算方法课程》的各班学生帮助，在此一并感谢并列举如下：
# 

# In[ ]:




