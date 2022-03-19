#!/usr/bin/env python
# coding: utf-8

# # <center> 第19章: 非线性方程求根</center>
# <center>（Chapter 19: Roots of Nonlinear Equations）</center>

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#引言" data-toc-modified-id="引言-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>引言</a></span></li><li><span><a href="#容差（Tolerance）" data-toc-modified-id="容差（Tolerance）-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>容差（Tolerance）</a></span><ul class="toc-item"><li><span><a href="#准确度和精密度" data-toc-modified-id="准确度和精密度-2.1"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>准确度和精密度</a></span></li><li><span><a href="#误差、精度和容差" data-toc-modified-id="误差、精度和容差-2.2"><span class="toc-item-num">2.2&nbsp;&nbsp;</span>误差、精度和容差</a></span></li></ul></li><li><span><a href="#二分法（Bisection-Method）" data-toc-modified-id="二分法（Bisection-Method）-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>二分法（Bisection Method）</a></span><ul class="toc-item"><li><span><a href="#二分法的基本原理" data-toc-modified-id="二分法的基本原理-3.1"><span class="toc-item-num">3.1&nbsp;&nbsp;</span>二分法的基本原理</a></span></li><li><span><a href="#二分法的示例" data-toc-modified-id="二分法的示例-3.2"><span class="toc-item-num">3.2&nbsp;&nbsp;</span>二分法的示例</a></span></li><li><span><a href="#二分法的Python实现" data-toc-modified-id="二分法的Python实现-3.3"><span class="toc-item-num">3.3&nbsp;&nbsp;</span>二分法的Python实现</a></span><ul class="toc-item"><li><span><a href="#二分法的Python函数" data-toc-modified-id="二分法的Python函数-3.3.1"><span class="toc-item-num">3.3.1&nbsp;&nbsp;</span>二分法的Python函数</a></span></li><li><span><a href="#二分法的Python实现示例" data-toc-modified-id="二分法的Python实现示例-3.3.2"><span class="toc-item-num">3.3.2&nbsp;&nbsp;</span>二分法的Python实现示例</a></span></li></ul></li><li><span><a href="#思考题" data-toc-modified-id="思考题-3.4"><span class="toc-item-num">3.4&nbsp;&nbsp;</span>思考题</a></span></li></ul></li><li><span><a href="#不动点迭代法-（Fixed-Point-Iteration-Method）" data-toc-modified-id="不动点迭代法-（Fixed-Point-Iteration-Method）-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>不动点迭代法 （Fixed-Point Iteration Method）</a></span><ul class="toc-item"><li><span><a href="#不动点迭代法的基本原理" data-toc-modified-id="不动点迭代法的基本原理-4.1"><span class="toc-item-num">4.1&nbsp;&nbsp;</span>不动点迭代法的基本原理</a></span></li><li><span><a href="#不动点迭代法的示例" data-toc-modified-id="不动点迭代法的示例-4.2"><span class="toc-item-num">4.2&nbsp;&nbsp;</span>不动点迭代法的示例</a></span></li><li><span><a href="#不动点迭代法的收敛性" data-toc-modified-id="不动点迭代法的收敛性-4.3"><span class="toc-item-num">4.3&nbsp;&nbsp;</span>不动点迭代法的收敛性</a></span><ul class="toc-item"><li><span><a href="#全局收敛性判断定理" data-toc-modified-id="全局收敛性判断定理-4.3.1"><span class="toc-item-num">4.3.1&nbsp;&nbsp;</span>全局收敛性判断定理</a></span></li><li><span><a href="#收敛性判断示例" data-toc-modified-id="收敛性判断示例-4.3.2"><span class="toc-item-num">4.3.2&nbsp;&nbsp;</span>收敛性判断示例</a></span></li><li><span><a href="#局部收敛性判断" data-toc-modified-id="局部收敛性判断-4.3.3"><span class="toc-item-num">4.3.3&nbsp;&nbsp;</span>局部收敛性判断</a></span></li></ul></li><li><span><a href="#不动点迭代法的Python实现" data-toc-modified-id="不动点迭代法的Python实现-4.4"><span class="toc-item-num">4.4&nbsp;&nbsp;</span>不动点迭代法的Python实现</a></span></li></ul></li><li><span><a href="#牛顿法（Newton-Method-or-Newton-Raphson-Method）" data-toc-modified-id="牛顿法（Newton-Method-or-Newton-Raphson-Method）-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>牛顿法（Newton Method or Newton-Raphson Method）</a></span><ul class="toc-item"><li><span><a href="#Newton法的基本原理" data-toc-modified-id="Newton法的基本原理-5.1"><span class="toc-item-num">5.1&nbsp;&nbsp;</span>Newton法的基本原理</a></span></li><li><span><a href="#Newton法的收敛性" data-toc-modified-id="Newton法的收敛性-5.2"><span class="toc-item-num">5.2&nbsp;&nbsp;</span>Newton法的收敛性</a></span></li><li><span><a href="#Newton法的示例" data-toc-modified-id="Newton法的示例-5.3"><span class="toc-item-num">5.3&nbsp;&nbsp;</span>Newton法的示例</a></span></li><li><span><a href="#Newton法的变种" data-toc-modified-id="Newton法的变种-5.4"><span class="toc-item-num">5.4&nbsp;&nbsp;</span>Newton法的变种</a></span><ul class="toc-item"><li><span><a href="#简化的Newton法" data-toc-modified-id="简化的Newton法-5.4.1"><span class="toc-item-num">5.4.1&nbsp;&nbsp;</span>简化的Newton法</a></span></li><li><span><a href="#Newton下山法" data-toc-modified-id="Newton下山法-5.4.2"><span class="toc-item-num">5.4.2&nbsp;&nbsp;</span>Newton下山法</a></span></li></ul></li><li><span><a href="#Newton法的Python实现" data-toc-modified-id="Newton法的Python实现-5.5"><span class="toc-item-num">5.5&nbsp;&nbsp;</span>Newton法的Python实现</a></span><ul class="toc-item"><li><span><a href="#Python代码" data-toc-modified-id="Python代码-5.5.1"><span class="toc-item-num">5.5.1&nbsp;&nbsp;</span>Python代码</a></span></li><li><span><a href="#Python代码使用实例" data-toc-modified-id="Python代码使用实例-5.5.2"><span class="toc-item-num">5.5.2&nbsp;&nbsp;</span>Python代码使用实例</a></span></li><li><span><a href="#Python代码使用训练题" data-toc-modified-id="Python代码使用训练题-5.5.3"><span class="toc-item-num">5.5.3&nbsp;&nbsp;</span>Python代码使用训练题</a></span></li></ul></li></ul></li><li><span><a href="#迭代法的收敛速度及其加速-（Convergence-and-Acceleration)" data-toc-modified-id="迭代法的收敛速度及其加速-（Convergence-and-Acceleration)-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>迭代法的收敛速度及其加速 （Convergence and Acceleration)</a></span><ul class="toc-item"><li><span><a href="#迭代法的收敛加速" data-toc-modified-id="迭代法的收敛加速-6.1"><span class="toc-item-num">6.1&nbsp;&nbsp;</span>迭代法的收敛加速</a></span></li><li><span><a href="#Python示例" data-toc-modified-id="Python示例-6.2"><span class="toc-item-num">6.2&nbsp;&nbsp;</span>Python示例</a></span></li></ul></li><li><span><a href="#其他复杂方法-（Other-Complex-Methods）" data-toc-modified-id="其他复杂方法-（Other-Complex-Methods）-7"><span class="toc-item-num">7&nbsp;&nbsp;</span>其他复杂方法 （Other Complex Methods）</a></span><ul class="toc-item"><li><span><a href="#割线法（Secant-Method）" data-toc-modified-id="割线法（Secant-Method）-7.1"><span class="toc-item-num">7.1&nbsp;&nbsp;</span>割线法（Secant Method）</a></span><ul class="toc-item"><li><span><a href="#割线法作为二分法的变种" data-toc-modified-id="割线法作为二分法的变种-7.1.1"><span class="toc-item-num">7.1.1&nbsp;&nbsp;</span>割线法作为二分法的变种</a></span></li><li><span><a href="#割线法作为Newton法的变种" data-toc-modified-id="割线法作为Newton法的变种-7.1.2"><span class="toc-item-num">7.1.2&nbsp;&nbsp;</span>割线法作为Newton法的变种</a></span></li><li><span><a href="#其他实现" data-toc-modified-id="其他实现-7.1.3"><span class="toc-item-num">7.1.3&nbsp;&nbsp;</span>其他实现</a></span></li></ul></li><li><span><a href="#反向二次插值法(Inverse-Quadratic-Interpolation-Method)" data-toc-modified-id="反向二次插值法(Inverse-Quadratic-Interpolation-Method)-7.2"><span class="toc-item-num">7.2&nbsp;&nbsp;</span>反向二次插值法(Inverse Quadratic Interpolation Method)</a></span></li><li><span><a href="#Brent法（Brent's-Method）" data-toc-modified-id="Brent法（Brent's-Method）-7.3"><span class="toc-item-num">7.3&nbsp;&nbsp;</span>Brent法（Brent's Method）</a></span><ul class="toc-item"><li><span><a href="#Preparing-initial-values-and-conditions" data-toc-modified-id="Preparing-initial-values-and-conditions-7.3.1"><span class="toc-item-num">7.3.1&nbsp;&nbsp;</span>Preparing initial values and conditions</a></span></li><li><span><a href="#The-iterative-process" data-toc-modified-id="The-iterative-process-7.3.2"><span class="toc-item-num">7.3.2&nbsp;&nbsp;</span>The iterative process</a></span></li><li><span><a href="#Finding-b_{k+1}" data-toc-modified-id="Finding-b_{k+1}-7.3.3"><span class="toc-item-num">7.3.3&nbsp;&nbsp;</span>Finding b_{k+1}</a></span></li><li><span><a href="#Rate-of-convergence" data-toc-modified-id="Rate-of-convergence-7.3.4"><span class="toc-item-num">7.3.4&nbsp;&nbsp;</span>Rate of convergence</a></span></li></ul></li></ul></li><li><span><a href="#利用Python对函数进行求根" data-toc-modified-id="利用Python对函数进行求根-8"><span class="toc-item-num">8&nbsp;&nbsp;</span>利用Python对函数进行求根</a></span></li><li><span><a href="#小结" data-toc-modified-id="小结-9"><span class="toc-item-num">9&nbsp;&nbsp;</span>小结</a></span></li><li><span><a href="#习题和讨论" data-toc-modified-id="习题和讨论-10"><span class="toc-item-num">10&nbsp;&nbsp;</span>习题和讨论</a></span></li></ul></div>

# ## 引言

# 对函数$f(x)$而言，其**根**或者**零点**是使得
# \begin{equation}
#     f(x_r)=0
# \end{equation}
# 的$x_r$，这里$x_r$可以为**实数**或者**复数**。

# 1） 对一些函数而言，我们可以列出函数的根的解析表达式。例如函数
# \begin{equation}
#     f(x) = x^2 -9
# \end{equation}
# 而言，其根为$x_1 = 3,\quad x_2 = -3$。

# 2） 而对于另外的一些函数，我们无法列出函数的根的解析表达式。例如，对函数
# \begin{equation}
#     f(x) = \cos(x)  - x
# \end{equation}
# 而言，我们无法写出根的解析表达式。

# 3） 另一些情况下，函数的形式特别复杂，根的解析表达式也比较复杂，无法精确获知。例如，对于解析根
# \begin{equation}
#     x_r = \frac{e^{2\pi/5} + \sin(5\pi/7) }{20 + \cos(3\pi/7) }
# \end{equation}
# 尽管我们能够获得解析表达式，但是该表达式比较复杂，我们往往更关注$x_r$的具体数值。这就必须借助于数值计算。因为我们看到，该表达式中涉及到的无理数$\pi$和$e$并没有解析计算方法，需要依靠数值计算的方法获得给定精度的近似值。

# In[1]:


import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2, 2, 1000)

# four examples of nonlinear functions
f1 = x**2 - x - 1
f2 = x**3 - 3 * np.sin(x)
f3 = np.exp(x) - 2
f4 = 1 - x**2 + np.sin(50 / (1 + x**2))

# plot each function
fig, axes = plt.subplots(1, 4, figsize=(12, 3), sharey=True)

for n, f in enumerate([f1, f2, f3, f4]):
    axes[n].plot(x, f, lw=1.5)
    axes[n].axhline(0, ls=':', color='k')
    axes[n].set_ylim(-5, 5)
    axes[n].set_xticks([-2, -1, 0, 1, 2])
    axes[n].set_xlabel(r'$x$', fontsize=18)

axes[0].set_ylabel(r'$f(x)$', fontsize=18)

titles = [r'$f(x)=x^2-x-1$', r'$f(x)=x^3-3\sin(x)$',
          r'$f(x)=\exp(x)-2$', r'$f(x)=\sin\left(50/(1+x^2)\right)+1-x^2$']
for n, title in enumerate(titles):
    axes[n].set_title(title)
    
fig.tight_layout()
# fig.savefig('ch5-nonlinear-plot-equations.pdf')


# 这时，利用数值方式获得某个函数的根的近似值是很有必要的。

# ## 容差（Tolerance）

# 在工程实践中，有几组关于计算或者测量的结果的精确程度的描述的名词需要关注：
# - 准确度（Accuracy）和精密度（Precision）；
# - 误差（Error）和容差（Tolerance）；

# ### 准确度和精密度
# 在工程测量和计算过程中，准确度和精密度是用来衡量测量/计算的质量的重要参数
# - **准确度**刻画了近似值与精确值之间的接近程度。
# - **精密度**刻画了近似值本身的精确程度，可以理解为表示近似值的数值的有效位数等等。

# # ![Accuracy_and_Precision.png](images/Accuracy_and_Precision.jpeg)
#  (a) inaccurate and imprecise, (b) accurate and imprecise,(c) Inaccurate and precise, (d) accurate and precise

# ### 误差、精度和容差

# 具体到数值计算领域，我们一般不用准确度和精密度的概念，转而采用针对性更强的**误差**、**精度**和**容差**的概念
# - **误差**衡量了近似值与精确值之间的偏离程度。从这个意义上来说，误差和准确度是同一个对象的不同方面。
# - **精度**表示了近似值本身的数值精确程度，是衡量一个数在计算机中的表示准确度的重要指标。
# - **容差**表示了我们对给定误差度量的容许程度，相当于在实际应用中给定了误差的允许上限。

# ## 二分法（Bisection Method）

# ### 二分法的基本原理

# 二分法是非线性方程求根的最简单的办法。其基本原理是，首先确定方程的一个有根区间，然后通过不断地对有原有根区间进行二分，并确定所获得的两个子区间中的新的有根子区间。理论上，只要能够确定初始的有根区间，一定能够通过二分法获得任意精度的解。

# 根据以上描述，可以获得二分法的算法流程如下：

# 1. 确定一个有根区间$[a_0,b_0]$，使得它满足$f(a_0) f(b_0) <0$;
# 1. 计算区间的中点$m_0 = \frac{a_0+b_0}{2}$并求$f(m_0)$的值；
# 1. 利用二分法求得下一个有根区间$[a_1,b_1]$：
#     1. 如果$f(a_0) f(m_0) <0$，则取$a_1 = a_0$, $b_1 = m_0$，新的有根区间为$[a_1,b_1]$.
#     1. 如果$f(m_0) f(b_0) <0$，则取$a_1 = m_0$, $b_1 = b_0$，新的有根区间为$[a_1,b_1]$.
# 1. 重复第(2)和第(3)步直到获得最终的有根区间$[a_N,b_N]$.
# 1. 求得最终有根区间$[a_N,b_N]$的中点$m_N = \frac{a_N+b_N}{2}$作为根的最终近似解。

# **!TIPS：** 上述二分法的执行过程需要设定一个结束条件，原因有二。一是求根的最终目的是利用合理的资源获得一定精度的根。这里面涉及到计算机的时间和内存消耗，以及所求根的精度。这些是对二分法实际使用的限制。二是计算机的有限精度存储和计算过程，使得二分过程本质上也无法获得完全精确的解，这也使得有限的二分法执行过程，或者说后续的其他迭代计算过程。

# **!TIPS：** 常见的执行过程结束条件可以从三个方面来设定：
# 1. 所求的数值近似根$x_s$与方程的理论精确根$x_r$之间的差距满足一定的条件，即
# \begin{equation}
#     |x_s - x_r| \leq tolroot
# \end{equation}
# 其中**tolroot**是人为设定的根近似程度要求。
# 2. 所求的数值近似根$x_s$使得原函数$f(x)$的绝对值满足一定条件，即
# \begin{equation}
#     |f(x_s)| \leq tolfunc
# \end{equation}
# 其中**tolfunc**是人为设定的函数值$f(x)$为零的判别条件。
# 3. 二分迭代次数$N$不超过预先设定的最大迭代次**maxiter**，主要是为了防止出现未知bug，也是为了获得对程序执行时间的控制。

# **!TIPS：** 大多数的情况下，其实在程序中不太关注函数值$𝑓(𝑥)$为零的判别条件，而是直接采用python本身内置的零值判定标准。这是由一般计算机的$Finite\ Precision\ Computation$机制决定的。计算机中能够表示的数并不是真的和实数一样在数轴上是均匀连续分布的，而是离散的，相邻两个可表示实数之间的差也是不定的。这就造成了一个后果，给定一个机器可表示的实数$x_c$，与其差距最小的两个实数分别为$x_l$和$x_r$。
# 
# 具体到求根而言，一般需要关注如何判断函数值为零。而在一般的有限精度表示系统中，与零最接近的数的大小表示了改表示系统的机械精度，一般用$eps$表示。在python的numpy数值计算包中，可以获得某一个表示浮点数的数据类型的机械精度如下：**np.finfo(np.float64).eps**。实际的工程应用中，其实大多数时候并不需要那么高精度的零值判断。因此，一般会人为设置一个零值判断精度。

# **!TIPS：** 对求根而言，我们的目的寻找$x_r$使得$f(x_r)=0$。
# 
# - 但实际上在有限精度计算机中我们只能使得$f(x_r)$尽可能接近$0$。因此，从求根误差的角度，$|f(x_r)|$是一个可选的度量。原则上$|f(x_r)|$越小，$x_r$越接近于精确根$x_s$。
# - 此外在迭代求根的过程中，我们会在每一个迭代步获得精确根$x_s$的一个近似值$x_i$。在算法设计合理的情况下，$|x_{i+1} - x_i|$是另一个可能的求根误差的度量。原因在于，合理的算法设计会使得$x_i$随着$i$的不断增加越来越接近精确根$x_s$，从而使得$|x_{i+1} - x_i|$越来越小。（这个观察其实来源于数列极限的相关定理，也来源于有关数列极限定理的$Cauchy$方式。）
# - 当然，如果我们能够找到一中方式在迭代计算的过程中定量的描述$|x_i - x_s|$的上限，那么我们实际上也可以近似用这个上限来表征每一步迭代获得的近似解$x_i$与精确解$x_s$之间的差距。
# - **例**：假定求根误差用$e = |f(x)|$来衡量，并用$tol$来表示可接受的误差的大小。也就是说，当某个数$x_r$满足$e = |f(x_r)| \leq tol$时，我们可以认为在可接受的误差范围内，我们找到了一个近似根$x_r$。那么如果令$f(x) = x^2 + tol / 2$，很明显$f(x)$没有实根。但是考虑到$|f(0)| = |tol/2| \leq tol$，满足设定的求根条件，我们可以认为在利用程序求根时，$x_r=0$时函数$f(x)$的一个零点。 <span style="color:red"> 这里请注意，我们的计算机程序有可能对一个本来理论上没有实数根的函数求出一个实数根 </span>.
# - **例**：假定求根误差用$e = |x_{i+1} - x_i|$来衡量，并用$tol$来表示可接受的误差的大小。考虑函数$f(x)= 1/ x$，很明显$f(x)$没有实数根。但是，某个计算机程序在第$i$步计算时获得$x_i = -tol/4$，在第$i+1$步计算时获得$x_{i+1} = tol/4$，那么所得的误差为$e = |x_{i+1} - x_i|=tol/2 \leq tol$，因此可以认为第$i+1$迭代获得的近似根为原函数$f(x)$的一个根。
# <span style="color:red"> 这里请注意，我们的计算机程序有可能对一个本来理论上没有实数根的函数求出一个实数根 </span>.

# **!TIPS：** 在实际计算和编程过程中，需要注意的是初始下标的数值。如果初始下标为$[a_0,b_0]$，则最终的迭代次数和下标相等；如果初始下标为$[a_1,b_1]$，则最终的迭代次数等与下标减1。关于在最终考试中的取法，请参考教材上的惯例。

# ### 二分法的示例

# **例(1)** 考虑函数
# \begin{equation}
#     f(x) = x^3 + x^2 - 5
# \end{equation}
# **求解初始有根区间**。

# **解：**
# - 首先，很明显函数$f(x)$是一个连续函数
# - 其次，根据简单的数值计算可知$f(1) = -3 <0$, $f(2) = 7 >0$
# - 再次，考虑$f(x)$的导函数$f'(x) = 3x^2 + 2x$在区间$[1,2]$上恒大于零，对应于$f(x)$的严格单调递增
# - 最后，根据以上结果和介值定理，我们可以得到$f(x)$在有根区间$[1,2]$上存在唯一的实根

# **例(2)** 考虑函数
# \begin{equation}
#     f(x) = x^3 - x - 1
# \end{equation}

# 首先，可以获得$f(x)$的有根区间为$[1,2]$，且$f(x)$在有根区间上的根唯一。

# 其次，针对有根区间$[1,2]$，要求近似解与精确解之间的差距不大于$10^{-3}$。

# 使用二分法进行迭代求根计算的过程如下（注意改表格中初始迭代下标为0）：
# 
# | <div style="width:10pt"> $k$  </div>   | $a_k$  | $b_k$ | $x_k$  | <div style="width:30pt"> $f(x_k)$  </div>        | <div style="width:80pt"> $f(x_k)$的符号  </div>       | 
# | --- | ------- | ------ | ------ | --------------: | :---: |
# |  0  | 1       | 2      | 1.5    |  0.8750000000   |   +  |
# |  1  | 1       | 1.5    | 1.25   | -0.2968750000   |   -  |
# |  2  | 1.25    | 1.5    | 1.375  |  0.224609375    |   +  |
# |  3  | 1.25    | 1.375  | 1.3125 | -0.0515136719   |   -  |
# |  4  | 1.3125  | 1.375  | 1.3438 |  0.0826110840   |   +  |
# |  5  | 1.3125  | 1.3438 | 1.3282 |  0.0145759583   |   +  |
# |  6  | 1.3125  | 1.3282 | 1.3204 | -0.0187106133   |   -  |
# |  7  | 1.31204 | 1.3282 | 1.3243 | -0.0021279454   |   -  |
# |  8  | 1.31243 | 1.3282 | 1.3263 |  0.0062088296   |   +  |
# |  9  | 1.31243 | 1.3263 | 1.3253 |  0.0024835453   |   +  |
# 
# 最终获得的近似解为$x_s = 1.3253$。

# 再次，如果要求最终获得的近似解$x_s$和精确解$x_r$满足$| x_s - x_r | \leq 10^{-6}$，则所需要的最少二分迭代次数为$k$。$k$应该满足
# \begin{equation}
#      |x_{k} - x_r| \leq \frac{b-a}{2^{k+1}} \leq 10^{-6}
# \end{equation}
# 即
# \begin{equation}
#     k \geq \frac{\log(b-a) + 6 \log(10) }{\log(2)} - 1 \approx 19.932.
# \end{equation}
# 从而二分迭代$20$次即可达到精度要求。

# **例(3)** 使用二分法求解方程$f(x) = x^3 - x - 1 = 0$，选取初始有根区间为$[1,1.5]$，则如果要求最终求根误差为$0.005$，所需要的最小迭代次数为多少？

# **解：** 根据前述的计算过程，可得最小迭代次数为$k$

# \begin{equation}
#     k \geq \frac{\log(b-a) - \log(0.005) }{\log(2)} - 1 \approx 5.644.
# \end{equation}

# 从而二分迭代$6$次即可达到精度要求。

# ### 二分法的Python实现

# #### 二分法的Python函数

# In[2]:


import numpy as np

"""
Find the numerical approximation xs of the actual solution xr 
of a function f with starting inverval [a,b]
Arguments:
    f:       A function to be sovled
    a:       Root-enclosing interval, left end
    b:       Root-enclosing interval, right end
    tolroot: Absolute tolerance for the root
                   |xs - xr| < tolroot
    torfunc: Absolute tolerance for the function zero
                   | f(xs) | < tolfunc
    maxiter: Maximum number of bisections to be done
Returns:
    The approximated root xs
"""

def bisection(f, a, b, tolroot=1e-3, tolfunc=1e-3, maxiter=20, fprint = False):
    
    if np.sign(f(a))  == np.sign(f(b)):
        raise Exception("The interval [a,b] does not bracket a root")
    if np.abs(f(a)) < tolfunc:
        xs = a; return xs 
    if np.abs(f(b)) < tolfunc:
        xs = b; return xs
    
    for k in range(1, maxiter+1):
        xm =  (a + b)/2
        if np.abs(f(xm)) < tolfunc or np.abs((a-b)/2) < tolroot:
            xs = xm; return xs
        if np.sign(f(a)) == np.sign(f(xm)):
            a = xm
        else:
            b = xm
        
#         print("%d, %12.10f, %12.10f, %12.10f, %12.10f, %12.10f, %12.10f, %14.10f" \
#               %(k, a, b,(b-a)/2, f(a), f(b), xm, f(xm)))
        
        if fprint == True:
            print("iter {0:d}： {1:>12.10f}  {2:>12.10f} {3:>12.10f} {4:>12.10f} {5:>12.10f} {6:>12.10f}  {7:>13.10f}"              .format(k,a,b,(b-a)/2, f(a), f(b), xm, f(xm)))
    xs = xm
    
    return xs

g = lambda x: np.cos(x) - x
a, b = 0.5, 1
bisection(g,a,b)


ff = lambda x: x * np.cos(x) + 1
a,b = -3, 4
bisection(ff,a,b)

gg = lambda x: x**3  - x - 1
a,b = 1, 2
bisection(gg,a,b,fprint=True)


# In[3]:


import numpy as np
import matplotlib.pyplot as plt
hh = lambda x: np.exp(10*np.sin(x)) + np.exp(1)*np.cos(x)
hh(-1)

x = np.linspace(-2*np.pi,2*np.pi,1000)
y = hh(x)
plt.plot(x,y)
plt.grid(True)
plt.show()


# #### 二分法的Python实现示例
# 以下以函数
# \begin{equation}
#    f(x) = x\ \cos(x) + 1
# \end{equation}
# 为例，调用以上二分法求解函数求区间$[-3,4]$内的一个根

# - 单纯调用显示中间迭代结果

# In[4]:


fun = lambda x: x * np.cos(x) + 1
x_real = bisection(fun, -3, 4, fprint=True)
print(x_real)


# - 调用计算最终结果并且可视化

# In[5]:


import numpy as np
import matplotlib.pyplot as plt
          
fun = lambda x: x * np.cos(x) + 1
x_real = bisection(fun, -3, 4)


print("x_real = ", "{:7.6f}".format(x_real))            
# 绘制结果
x = np.linspace(-3, 5, 500)

plt.figure(figsize=(12,6))
plt.plot(x,fun(x), 'b-', linewidth=2, label=r"$f(x) = x \ cosx + 1$")
plt.plot(x_real, fun(x_real), 'o-r', markersize=15, label="Approximated root")
plt.xlabel(r"$x$", fontsize=20, fontname="Times New Roman")
plt.ylabel(r"$f(x) = x\ cosx + 1$", fontsize=20, fontname="Times New Roman")
plt.title("Root finding by bisection", fontsize=20, fontname="Times New Roman")
plt.legend(fontsize=20)
plt.xlim((-3, 5))
plt.xticks(np.arange(-3, 6, 1))
plt.grid(True, linestyle='-.')

plt.show()


# ### 思考题

# 1. 考虑方程
# $$x^5=x^2+10$$
# 
#     1. 确定一个区间$[a,b]$，使得区间长度为$1$，而且其中存在该方程的一个根。
#     1. 根据所确定的初始区间，利用二分法进行两次迭代计算，获得对应的有跟区间。
#     1. 确定求得绝对误差不超过$10^{-10}$的根所需要的二分迭代操作的次数。
#     1. 利用上述的二分法代码，求得绝对误差不超过$10^{-10}$的根。

# 2. Find the 4th approximation of the positive root of the function $f(x)=x^4−7$ using the bisection method .

# 3. Find the third approximation of the root of the function $f(x)=\frac{1}{2}x − \sqrt[3]{x+1}$ using the bisection method .

# 4. Approximate the negative root of the function $f(x)=x^2−7$ to within $0.1$ of its actual value.

# 5. 黄金分割比
# $$\phi = \frac{\sqrt{5} - 1}{2} \approx 0.618\cdots $$
# 是函数$f(x)= x^2 - x - 1$的一个根。选定初始有根区间$[1,2]$，求迭代计算次数$N=25$后的近似区间和近似根。

# 6. Approximate the value of the root of $f(x)=−3x^3+5x^2+14x−16$ near $x=3$ to within $0.05$ of its actual value.

# 7. Find the 4th approximation to the solution of the equation below using the bisection method .
# $$x^2−x−2=x$$

# 8. Find the 5th approximation to the solution to the equation below, using the bisection method .
# $$x^4−2=x+1$$

# 9. The equation below should have a solution that is larger than 5. Use the bisection method to approximate this solution to within $0.1$ of its actual value.
# $$x^3+18x−6=9x^2−2x+7$$

# ## 不动点迭代法 （Fixed-Point Iteration Method）
# 前述的二分法向我们展示了非线性方程求根的一种方法。二分法有很多种解读的角度。
# - 一是我们从实际操作上讲，利用了不断对有限区间进行长度对分，最终使得包含根的区间长度越来越小，区间中点所对应的数也就越来越接近于非线性方程的根。
# - 二是可以从迭代的角度来讲，二分法实际上是寻求一个近似序列$x_i$ $\{ x_i \}_{i=1}^{\infty}$，使得该近似序列的极限趋于方程的精确解$x_r$
# \begin{equation}
#     \lim_{n \to \infty} x_i = x_r
# \end{equation}
# 从这个角度来讲，二分法的操作流程相当于确定了一个由$x_i$到$x_{i+1}$的变换规则。
# 
# 从更大的范围来讲，利用计算机进行数值计算时，经常或者说必须采用的一种思路就是**迭代法**，也就是通过建立由某一个近似解获得另一个近似解的方法
# \begin{equation}
#     x_i  \Longrightarrow_{(by\ some\ rules)} x_{i+1}
# \end{equation}
# （也就是**迭代规则**），构造一个近似序列
# \begin{equation}
#     \{ x_i \}_{i=1}^{\infty}
# \end{equation}
# （也就是**迭代序列**），最后只要经过合理的算法设计，使得迭代序列的极限是所需要求的精确解即可。

# ### 不动点迭代法的基本原理
# 
# **不动点迭代法**的核心是通过对非线性方程
# \begin{equation}
#     f(x) = 0
# \end{equation}
# 进行改造获得一个合适的迭代规则
# \begin{equation}
#     x = g(x)
# \end{equation}
# 又称为**迭代函数**，从而获得迭代格式
# \begin{equation}
#     x_{i+1} = g(x_i),\quad i =0,1,2,\cdots
# \end{equation}
# 及对应的迭代序列
# \begin{equation}
#     x_0, x_1, x_2, \cdots, x_i, x_{i+1}, \cdots
# \end{equation}

# ### 不动点迭代法的示例

# **例1**  用不动点迭代法求解方程
# $$x^2 - 10 =  0$$

# **解** 
# - 首先是要构造迭代函数$x=g(x)$。针对给出的方程，我们在这里选出的迭代函数是
# \begin{equation}
#    f(x) = x^2 - 10 =  0 \Longrightarrow  x = \frac{1}{2}\left( x + \frac{10}{x} \right) = g(x)
# \end{equation}
# - 从而我们获得的迭代格式是
# \begin{equation}
#   x_{i+1} = \frac{1}{2}\left( x_i + \frac{10}{x_i} \right)
# \end{equation}
# - 选定一个迭代计算用的初始值。这里我们简单的选$x_0 = 1$
# - 依次进行迭代计算可得$x_1$,$x_2$,$\cdots$, $x_9$如下  <br>
# > x[0] :=   1.00000000 <br>
# x[1] :=   5.50000000 <br>
# x[2] :=   3.65909091 <br>
# x[3] :=   3.19600508 <br>
# x[4] :=   3.16245562 <br>
# x[5] :=   3.16227767 <br>
# x[6] :=   3.16227766 <br>
# x[7] :=   3.16227766 <br>
# x[8] :=   3.16227766 <br>
# x[9] :=   3.16227766 <br>
# 
# 对应的python代码如下
# 
# ``` python
# import numpy as np
# 
# g = lambda x: (x + 10.0/x) / 2.0
# x0 = 1.0
# x = np.zeros(10)
# x[0] = x0
# for i in range(1,len(x)):
#     x[i] = g(x[i-1])
# for i in range(len(x)):
#     print("x[%d] := %12.8f" %(i, x[i]))
# ```

# **例2**  用不动点迭代法求解方程
# $$x^3 - x - 1 =  0$$

# **解** 首先可以画出该函数的图像如下：

# In[6]:


import numpy as np
import matplotlib.pyplot as plt

g = lambda x: x**3 - x - 1
x = np.linspace(1,2,100)
y = g(x)
plt.figure(figsize=(12,6))
plt.plot(x,y)
plt.grid(True)
plt.xlabel("x")
plt.ylabel("g(x0)")
plt.show()


# 其次，我们可以构造出三种迭代函数
# \begin{equation}
#     g_1 (x) = \sqrt[3]{x+1},\quad g_2 (x) = x^3 - 1，\quad g_3(x) = \frac{x+1}{x^2}
# \end{equation}
# **!TIPS** 请验证一下$g_1(x)$，$g_2(x)$和$g_3(x)$符合上述方程。

# 再次，选取初始值$x_0=1.5$，可以对上述迭代公式进行迭代求解，获得如下表的结果
# 
# |迭代公式  | $g_1(x)$   |   $g_2(x)$   |    $g_3(x)$   |
# |---|-- -|--- | --- |
# |$x_0$| 1.50000000 |  1.50000000 |  1.50000000 |
# |$x_1$| 1.35720881 |  2.37500000 |  1.11111111 |
# |$x_2$| 1.33086096 | 12.39648438 |  1.71000000 |
# |$x_3$| 1.32588377 |1904.00277223 |  0.92678089 |
# |$x_4$| 1.32493936 |6902441412.88919163 |  2.24325265 |
# |$x_5$| 1.32476001 |328857830399801008433274028032.00000000 |  0.64450220 |
# |$x_6$| 1.32472595 | --- |  3.95900139 |
# |$x_7$| 1.32471947 |--- |  0.31639013 |
# |$x_8$| 1.32471825 |         inf | 13.15039424 |
# |$x_9$| 1.32471801 |         inf |  0.08182594 |
# 

# ``` python
# import numpy as np
# 
# g1 = lambda x: (x+1)**(1.0/3)
# g2 = lambda x: x**3.0 - 1
# g3 = lambda x: (x + 1.0) / x**2.0
# x0 = 1.5
# x1 = np.zeros(10)
# x2 = np.zeros(10)
# x3 = np.zeros(10)
# x1[0] = x0
# x2[0] = x0
# x3[0] = x0
# for i in range(1,len(x1)):
#     x1[i] = g1(x1[i-1])
#     x2[i] = g2(x2[i-1])
#     x3[i] = g3(x3[i-1])
# for i in range(len(x1)):
#     print(" %12.8f |%12.8f |%12.8f |" %(x1[i],x2[i],x3[i]))
# ``` 

# **!TIPS** 根据以上过程可知，<font color=red>$g(x)$的选择对于最终是否能够顺利求得精确解，甚至说能否求得一个解至关重要</font>。

# ### 不动点迭代法的收敛性
# 从几何上看，不动点迭代法的操作过程是求函数$y=g(x)$与直线$y=x$的交点$P$的横坐标$x_p$。

# In[7]:


import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2,2,1000)
y = x**3.0 - 1
plt.figure(figsize=(6,6))
plt.plot(x,x,'r--',label=r'$y=x$')
plt.plot(x,y,'b-',label=r'$y=x^3 - 1$')
plt.xlabel("x");plt.ylabel("y");
plt.ylim([-2,2])
plt.xlim([-2,2])
plt.grid(True)
plt.legend()
plt.show()


# 通过前面的示例，我们能够很明确的发现：利用不动点迭代法$x_{k+1} = g(x_k)$求非线性方程$f(x)=0$的根时，$g(x)$的形式决定了迭代过程的收敛特性以及最终结果的准确性。下图表示了不同$g(x)$所对应的迭代过程。

# ![fixed_point_example.jpg](./images/fixed_point_example.jpg)

# #### 全局收敛性判断定理

# **定理（不动点迭代法的收敛性条件）**  设函数$\varphi(x)$在闭区间$[a,b]$上连续，并且满足
# 
# <a name="item:theorem1_condition1"></a> <font color="red">条件1</font>: 对任意的$x\in [a,b]$，都有$\varphi(x) \in [a,b]$；
# 
# <a name="item:theorem1_condition2"></a> <font color="red">条件2</font>: 存在正数$L < 1$，使得对任意$x,y \in [a,b]$，有：
# \begin{equation*}
#  |\varphi(x) - \varphi(y)| \leq L |x-y|.
# \end{equation*}
# 
# 则对于方程$x = \varphi(x)$而言，有
# 
# <a name="item:theorem1_result1"></a> <font color="blue">结论1</font>：函数$\varphi(x)$在闭区间$[a,b]$上存在唯一的不动点$x^*$；
# 
# <a name="item:theorem1_result2"></a> <font color="blue">结论2</font>：对于任何初值$x_0 \in [a,b]$，由迭代法$x_{k+1} = \varphi(x_k)$生成的序列$\{x_k\}$收敛到不动点$x^*$；
# 
# <a name="item:theorem1_result3"></a> <font color="blue">结论3</font>：存在如下的误差估计式
# \begin{equation*}
#  |x_k - x^*| \leq \frac{L}{1-L}|x_k - x_{k-1}|.
# \end{equation*}
# \begin{equation*}
#  |x_k - x^*| \leq \frac{L^k}{1-L}|x_1 - x_0|.
# \end{equation*}

# **证明 part 1（不动点的存在性）**
# 根据前述情况，显然有$x_k \in [a,b],\ k=0,1,\cdots$，进而有
#  \begin{equation*}
#      \begin{aligned}
#          |x_k - x^*| &= |\varphi(x_{k-1}) - \varphi(x^*)| \\
#                      &\leq L |x_{k-1} - x^*| \leq \cdots \leq L^k |x_{0} - x^*|
#      \end{aligned}
#  \end{equation*}
#  从而
#  \begin{equation*}
#      \lim_{k \to \infty}|x_k - x^*| = 0
#  \end{equation*}
#  即$$\lim_{k \to \infty}x_k = x^*$$
#  
#  **证明 part 2（不动点的唯一性）**
# 现假设$\varphi(x)$在区间$[a,b]$上有两个不同的不动点$x_1^*$和$x_2^*$，则有
# \begin{equation*}
#     |x_1^* - x_2^*| = |\varphi(x_1^*) - \varphi(x_2^*)| \leq L |x_1^* - x_2^*| < |x_1^* - x_2^*|
# \end{equation*}
# 该式存在矛盾，因此$\varphi(x)$在区间$[a,b]$上只有一个不动点
# 
# **证明  part 3（迭代序列的收敛性）**
# 根据前述情况，显然有$x_k \in [a,b],\ k=0,1,\cdots$，进而有
#  \begin{equation*}
#      \begin{aligned}
#          |x_k - x^*| &= |\varphi(x_{k-1}) - \varphi(x^*)| \\
#                      &\leq L |x_{k-1} - x^*| \leq \cdots \leq L^k |x_{0} - x^*|
#      \end{aligned}
#  \end{equation*}
#  从而
#  \begin{equation*}
#      \lim_{k \to \infty}|x_k - x^*| = 0
#  \end{equation*}
#  即$$\lim_{k \to \infty}x_k = x^*$$
#  
#  **证明  part 4（迭代序列的收误差估计）**
# 根据前述情况，显然有
# \begin{equation*}
#     |x_{k+1} - x_k| = |\varphi(x_{k}) - \varphi(x_{k-1})| \leq L |x_{k} - x_{k-1}|
# \end{equation*} 
# 进而，对任意的正整数$p$可得
# \begin{equation*}
#  \begin{aligned}
#      |x_{k+p} - x_k| &\leq |x_{k+p} - x_{k+p-1}| + \cdots + |x_{k+2} - x_{k+1}| + |x_{k+1} - x_k| \\
#                      &\leq \left( L^{p-1} + \cdots + L + 1 \right) |x_{k+1} - x_k|
#  \end{aligned}
# \end{equation*}
# 因为$0 < L < 1$，从而$(1-L)^{-1} = \sum_{k=0}^\infty L^k > 1 + L + \cdots + L^{p-1}$。由此，
# \begin{equation*}
#     |x_{k+p} - x_k| \leq \frac{1}{1-L} |x_{k+1} - x_k| \leq \frac{L}{1-L} |x_{k} - x_{k-1}|
# \end{equation*}
# 令$p \to \infty$并由前述证明的序列收敛性，即可得 
# \begin{equation*}
#  |x^* - x_k| \leq \frac{L}{1-L} |x_{k} - x_{k-1}|
# \end{equation*}
# 继续往下迭代可知
# \begin{equation*}
#      |x^* - x_k| \leq \frac{L}{1-L} |x_{k} - x_{k-1}| \leq \frac{L^2}{1-L} |x_{k-1} - x_{k-2}| \leq \cdots \leq \frac{L^k}{1-L} |x_{1} - x_{0}| 
# \end{equation*}

# **!TIPS** 1： 如果函数$\varphi(x)$在区间$(a,b)$内可微，那么上述定理中的[条件1](#item:theorem1_condition1)可以用更强的条件代替： 
#  \begin{equation*}
#      |\varphi^{\prime}(x)| \leq L < 1,\quad \forall x \in (a,b)
#  \end{equation*}
#  事实上，若上式成立，则根据微分中值定理，对任何$x,y \in [a,b]$都有 
#  \begin{equation*}
#      |\varphi(x) - \varphi(y)| = |\varphi^{\prime}(\xi) (x-y)| \leq L(x-y),
#  \end{equation*}
#  其中$\xi$在$x$与$y$之间，从而[条件2](#item:theorem1_condition2)成立。

# **!TIPS** 2： 以上两个结论中的收敛性与初始值的选取无关!只要初始值在区间$(a,b)$内，我们都能通过迭代达到最终的准确值$x^*$，这种收敛性我们称之为全局收敛。

# **!TIPS** 3： 根据上述定理的[结论3](#item:theorem1_result3)：
#  \begin{equation*}
#      |x_k - x^*| \leq \frac{L}{1-L}|x_k - x_{k-1}|. 
#  \end{equation*}
# 只要相邻两次计算结果的偏差$|x_{k} - x_{k-1}|$足够小，且$L$不很接近于$1$，即可以保证近似值$x_k$具有足够的精度。因此，可以通过检查$|x_{k} - x_{k-1}|$的大小来判断迭代过程是否终止。

# **!TIPS** 4： 同样根据上述定理的[结论3](#item:theorem1_result3)，我们可以得到
#  \begin{equation*}
#      |x_k - x^*| \leq \frac{L}{1-L}|x_k - x_{k-1}| \leq \cdots \leq \frac{L^k}{1-L}|x_1 - x_{0}|.
#  \end{equation*}
# 如果能恰当计算出$L$的值，我们可以由上式对给定的计算精度要求确定出所需要迭代的次数。

# #### 收敛性判断示例

# **!例**： 对于方程$f(x) = x^3 - x - 1 = 0$在区间$[1,2]$列出两种迭代格式，并分别分析其收敛性。

# **!解**： 
# 
# 第一种迭代格式为$\varphi_1(x) = \sqrt[3]{x+1}$，即
# \begin{equation*}
#     x_{k+1} = \sqrt[3]{x_k+1}.
# \end{equation*}
# 而其导数为$\varphi_1^\prime(x) = \frac{1}{3}(x+1)^{-2/3}$。从而，我们容易验证，对任意的$x \in [1,2]$有
# \begin{equation*}
#     \varphi_1(x) \in [1.26, 1.45] \subset [1,2],\quad \varphi_1^\prime(x) \leq 0.21 < 1.
# \end{equation*}
# 因此，对于任何初值$x_0 \in [1,2]$，由$\varphi_1(x) $给出的迭代格式都收敛到区间$[1,2]$上的唯一不动点$x^*$。
# 
# 第二种迭代格式为$\varphi_2(x) = x^3 + 1 $，即
# \begin{equation*}
#     x_{k+1} = x_k^3 + 1 .
# \end{equation*}
# 而其导数为$\varphi_2^\prime(x) = 3 x^2$。显然，对于$x \in [1,2]$有
# \begin{equation*}
#     \varphi_2(x) \in [0,7],\quad \varphi_2^\prime(x) \in [3, 12],
# \end{equation*}
# 不满足定理的[条件1](#item:theorem1_condition1)。再结合几何图形可以说明，只要初值$x_0 \neq x^*$，该迭代法发散。
# 

# **!TIPS**： 有时，对于一些不满足上述定理条件的问题，可以通过转化，变成满足定理的迭代格式。这需要针对具体情况进行讨论。

# #### 局部收敛性判断

# 前述定理讨论的是不动点迭代法的全局收敛性。但是一般而言，全局收敛性的基本条件不易检验，不容易得到满足，所以我们经常需要讨论在$x^*$附近的收敛性问题。为此，我们给出如下定义：
# 
# **!<font color='magenta'>定义</font>**： 设$x^*$是$\varphi(x)$的不动点，若存在$x^*$的某个$\delta$-邻域$N_\delta(x^*) = [x^* - \delta, x^* + \delta]$，$\delta > 0$，使得对于任何初值$x_0 \in N_\delta(x^*)$，由迭代格式
#  \begin{equation*}
#      x_{k+1} = \varphi(x_k)
#  \end{equation*}
# 生成的序列$\{ x_k \}_{k=1}^\infty$满足：$x_k \in N_\delta(x^*)$，且收敛到$x^*$，则称该迭代格式是<font color='magenta'>局部收敛的</font>。

# **!定理**： 设$x^*$是$\varphi(x)$的一个不动点，$\varphi^\prime(x)$在$x^*$的某个邻域上连续，并且有$|\varphi^\prime(x^*)|<1$，则迭代格式$x_{k+1} = \varphi(x_k)$是局部收敛的。

# **证明**
# 由于$\varphi^\prime(x)$在$x^*$处连续，且$|\varphi^\prime(x^*)|<1$，所以存在$x^*$的某一个闭邻域$[x^* - \delta, x^* + \delta]$，在其上有$|\varphi^\prime(x^*)| \leq L < 1$，并且有
#          \begin{equation*}
#              |\varphi(x) - x^*| = |\varphi(x) - \varphi(x^*)| \leq L |x - x^*| < \delta
#          \end{equation*}
#          即对一切$x \in [x^* - \delta, x^* + \delta]$，有$\varphi(x) \in [x^* - \delta, x^* + \delta]$。则依据全局收敛定理，对任意$x_0 \in [x^* - \delta, x^* + \delta]$，迭代格式$x_{k+1} = \varphi(x_k)$收敛。

# **!<font color='magenta'>定义（收敛阶）</font>**： 设迭代序列$\{x_k\}$收敛到$\varphi(x)$的不动点$x^*$，记误差$e_k = x_k - x^*$。若存在实数$p \geq 1$和$C \neq 0$，使得
#  \begin{equation*}
#      \lim_{k \to \infty} \frac{e_{k+1}}{e_k^p} = C
#  \end{equation*}
#  则称该迭代序列$\{x_k\}$是$p$阶收敛的。
#  
#  - 当$ p =1 $且$ 0< C < 1$时称为<font color='magenta'>线性收敛</font>
#  - 当$ p =2 $时称为<font color='magenta'>二次收敛</font>，或<font color='magenta'>平方收敛</font>
#  - 当$ p >1 $或$ p=1$且$ C=0 $时称为<font color='magenta'>超线性收敛</font>
# 
# 若$0 < |\varphi^\prime(x^*)| < 1$，则不动点迭代$x_{k+1} = \varphi(x_k)$<font color='magenta'>局部线性收敛</font>。

# **!定理**： 设$x^*$是$\varphi(x)$的不动点，若有正整数$p \geq 2$，使得$\varphi^{(p)}(x)$在$x^*$的邻域上连续，并且满足
# \begin{equation*}
#  \begin{aligned}
#      \varphi^{\prime}(x^*) &= \varphi^{\prime\prime}(x^*) = \cdots = \varphi^{(p-1)}(x^*) = 0, \\
#      \varphi^{(p)}(x^*) & \neq 0,
#  \end{aligned}
# \end{equation*}
# 则称该迭代序列$\{x_k\}$是$p$阶局部收敛的，且有
#  \begin{equation*}
#      \lim_{k \to \infty}\frac{x_{k+1} - x^*}{(x_k - x^*)^p} = \frac{\varphi^{(p)}(x^*)}{p!}
#  \end{equation*}

# **证明**
# 因为$\varphi^\prime(x^*) = 0$，根据局部收敛定理，该迭代格式是局部收敛的。
#          取充分接近于$x^*$的$x_0$，设$x_0 \neq x^*$，则有$x_k \neq x^*,\ k=1,2,\cdots$.根据$Taylor$展开式，有 
#          \begin{equation*}
#              \begin{aligned}
#                  x_{k+1} &= \varphi(x_k) \\
#                          &= \varphi(x^*) + \varphi^{\prime}(x^*) (x_k - x^*) + \cdots \\
#                          &+ \frac{\varphi^{(p-1)}(x^*)}{(p-1)!}(x_k - x^*)^{p-1} + \frac{\varphi^{(p)}(\xi_k)}{p!}(x_k - x^*)^{p}
#              \end{aligned}
#          \end{equation*}
#          其中$\xi_k$在$x_k$与$x^*$之间。从而根据题设条件有
#          \begin{equation*}
#              x_{k+1} - x^* = \frac{\varphi^{(p)}(\xi_k)}{p!}(x_k - x^*)^{p}
#          \end{equation*}
#          再由$\varphi^{(p)}(x)$的连续性，当$k \to \infty$时，原定理得证。

# **!例**： 分析方程$f(x) = x^2 - 3 = 0$的不同迭代格式在求正根$x^* = \sqrt{3}$时的收敛性。

# **解** 
# - 第一种格式，取$\varphi(x) = x^2 - 3 + x$，则有$\varphi^{\prime}(x^*) = 2 \sqrt{3} + 1 > 1$，无法判断其局部收敛性。
# - 第二种格式，取$\varphi(x) = x - \frac{x^2 - 3}{4}$，则有$\varphi^{\prime}(x^*) = 1 - \frac{\sqrt{3}}{2} < 1$，迭代格式是一阶局部收敛的。  
# - 第三种格式，取$\varphi(x) = \frac{1}{2} \left( x + \frac{3}{x} \right)$，则有$\varphi^{\prime}(x^*) = 0,\ \varphi^{\prime\prime}(x^*) = \frac{2}{\sqrt{3}} \neq 0 $，迭代格式是二阶局部收敛的。 
# 

# **!TIPS**： 一般而言，$|\varphi^{\prime}(x^*)|$越小，迭代格式$x_{k+1} = \varphi(x_k)$的收敛速度越快。

# ### 不动点迭代法的Python实现

# In[8]:


import numpy as np

def fixedPointIteration(func, x0, tol=1e-3, maxiter=10):
    iters = 0
    xprev = x0
    xnext = func(xprev)
    print(f"iters = {iters}, x{iters} = {xprev: 0.8f}, f(x{iters}) = {xnext: 0.8f}")
    for i in range(0, maxiter):
        if np.abs(xnext - xprev) < tol:
            print(f'ROOT: {xnext} obtained at ITERATION: {iters+1}')
            return xnext
        iters = iters + 1
        xprev = xnext
        xnext = func(xprev)
        print(f"iters = {iters}, x{iters} = {xprev: 0.8f}, f(x{iters}) = {xnext: 0.8f}")
    
    if iters == maxiter and np.abs(xnext - xprev) > tol:
        print("Maximum iterations reached without root!")
    else:
        print(f'ROOT: {xnext} obtained at ITERATION: {iters+1}')
    
    return xnext

ff = lambda x: np.exp(x) - 3
fixedPointIteration(ff, 1.5)


# 例：
# \begin{equation}
#     f(x) = \frac{1}{2} ( \sin(x) + \cos(x) ) - x,\quad g(x) = \frac{1}{2} ( \sin(x) + \cos(x) )
# \end{equation}

# In[9]:


f = lambda x: (np.sin(x) + np.cos(x))/2
fixedPointIteration(f, -0.3, tol = 1e-3)


# 例：
# \begin{equation}
#     f(x) = \frac{1}{\tan(x)} - \frac{1}{x},\quad g(x) = \frac{1}{\tan(x)} - \frac{1}{x} + x
# \end{equation}

# In[10]:


import numpy as np
import matplotlib.pyplot as plt

gg = lambda x: (1/np.tan(x)) - (1/x) + x
xsol = fixedPointIteration(gg, x0=4.0, tol=1e-3, maxiter=20)
print(xsol)

x = np.linspace(4,5,300)
plt.figure(figsize=(6,6))
plt.plot(x,x,'r--')
plt.plot(x,gg(x),'b-')
plt.plot(xsol,gg(xsol),'ko', markersize=20)
plt.grid(True)
plt.show()


# 例：
# \begin{equation}
#     f(x) = \sin(\sqrt{x}) - x,\quad g(x) = \sin(\sqrt{x})
# \end{equation}

# In[11]:


import numpy as np
import matplotlib.pyplot as plt

gg = lambda x: np.sin(np.sqrt(x))
xsol = fixedPointIteration(gg, x0=4.0, tol=1e-3, maxiter=20)
print(xsol)

x = np.linspace(0,2,1000)
plt.figure(figsize=(6,6))
plt.plot(x,x,'r--', label=r'$y=x$')
plt.plot(x,gg(x),'b-', label=r'$y=\sin(\sqrt{x})$')
plt.plot(xsol,gg(xsol),'ko', markersize=12, label=r'Root of $x=\sin(\sqrt{x})$')
plt.grid(True)
plt.legend()
plt.show()


# 例：
# \begin{equation}
#     f(x) = \arcsin(x) - x^2,\quad g(x) = \sin(x^2)
# \end{equation}

# In[12]:


import numpy as np
import matplotlib.pyplot as plt

gg = lambda x: np.sin(x**2.0)
xsol = fixedPointIteration(gg, x0=4.0, tol=1e-3, maxiter=20)
print(xsol)

x = np.linspace(-2,2,1000)
plt.figure(figsize=(6,6))
plt.plot(x,x,'r--', label=r'$y=x$')
plt.plot(x,gg(x),'b-', label=r'$y=\sin(x^2)$')
plt.plot(xsol,gg(xsol),'ko', markersize=12, label=r'Root of $x=\sin(x^2)$')
plt.grid(True)
plt.legend()
plt.show()


# 例：
# \begin{equation}
#     f(x) = \sin(x) - x^3,\quad g(x) = \arcsin(x^3)
# \end{equation}

# In[13]:


import numpy as np
import matplotlib.pyplot as plt

gg = lambda x: np.arcsin(x**3.0)
xsol1 = fixedPointIteration(gg, x0=0.1, tol=1e-3, maxiter=20)
print(xsol1)
xsol2 = fixedPointIteration(gg, x0=0.75, tol=1e-3, maxiter=20)
print(xsol2)

x = np.linspace(-1,1,1000)
plt.figure(figsize=(6,6))
plt.plot(x,x,'r--', label=r'$y=x$')
plt.plot(x,gg(x),'b-', label=r'$y=\arcsin(x^3)$')
plt.plot(xsol1,gg(xsol1),'ko', markersize=12, label=r'Root 1 of $x=\arcsin(x^3)$')
plt.grid(True)
plt.legend()
plt.show()


# 例：
# \begin{equation}
#     f(x) = e^{-x} - 3 \ln(x),\quad g(x) = e^{-x} - 3 \ln(x) + x
# \end{equation}

# In[14]:


import numpy as np
import matplotlib.pyplot as plt

gg = lambda x: -3*np.log(x) + np.exp(-x) + x
xsol1 = fixedPointIteration(gg, x0=1.1, tol=1e-3, maxiter=20)
print(xsol1)

x = np.linspace(1,2,1000)
plt.figure(figsize=(6,6))
plt.plot(x,x,'r--', label=r'$y=x$')
plt.plot(x,gg(x),'b-', label=r'$y=-3\ln(x) + e^{-x} + x$')
plt.plot(xsol1,gg(xsol1),'ko', markersize=12, label=r'Root 1 of $x=-3\ln(x) + e^{-x} + x$')
plt.grid(True)
plt.legend()
plt.show()


# 例：
# \begin{equation}
#     f(x) = e^{-x} - 3 \ln(x),\quad g(x) = e^{e^{-x}/3}
# \end{equation}
#  

# In[15]:


import numpy as np
import matplotlib.pyplot as plt

gg = lambda x: np.exp(np.exp(-x)/3)
xsol1 = fixedPointIteration(gg, x0=1.5, tol=1e-3, maxiter=20)
print(xsol1)

x = np.linspace(1,2,1000)
plt.figure(figsize=(6,6))
plt.plot(x,x,'r--', label=r'$y=x$')
plt.plot(x,gg(x),'b-', label=r'$y=e^{e^{-x}/3}$')
plt.plot(xsol1,gg(xsol1),'ko', markersize=12, label=r'Root 1 of $x= e^{e^{-x}/3}$')
plt.grid(True)
plt.legend()
plt.show()


# ## 牛顿法（Newton Method or Newton-Raphson Method）

# ### Newton法的基本原理

# - $Newton$法的基本思想是将非线性方程线性化。
# 
# 设$x_k$是$f(x)=0$的近似根，将$f(x)$在$x_k$处$Taylor$展开
#  \begin{equation*}
#      \begin{aligned}
#          f(x) &= f(x_k) + f^\prime(x_k)(x-x_k) + \frac{f^{\prime\prime}(\xi) }{2!}(x-x_k)^2 + h.o.t \\
#               &\approx f(x_k) + f^\prime(x_k)(x-x_k) \triangleq P(x).
#      \end{aligned}
#  \end{equation*}
#  令$P(x) = 0$，当$\boxed{f^\prime(x) \neq 0}$时，我们可以得到
#  \begin{equation*}
#      x_{k+1} = x_k - \frac{f(x_k)}{f^\prime(x_k)}
#  \end{equation*}

# -  $Newton$法的几何意义如下：
# 
# $x_{k+1}$为函数$f(x)$在点$x_k$处的切线与横坐标轴的交点。因此$Newton$迭代法也称为切线法。
# 
# ![newton_iteration_show.jpg](./images/newton_iteration_show.jpg)

# - $Newton$法的基本算法流程：
# 
# 1. 任取迭代初始值$x_0$
# 1. 计算$x_1 = x_0 - \frac{f(x_0)}{f^\prime(x_0)}$ 
# 1. 判断收敛性：如果$|x_1 - x_0| < \epsilon$或者$|f(x_1)| < \epsilon$，则算法收敛，停止计算，输出近似解$x_1$
# 1. 令$x_0 \leftarrow x_1$，返回第二步

# ### Newton法的收敛性

# **!定理**： 设$f(x^*) = 0$，$f^\prime(x^*) \neq 0$，且$f(x)$在包含$x^*$的某个区间上二阶连续可微，则$Newton$迭代法至少二阶收敛，且
# \begin{equation*}
#     \lim_{k \to \infty} \frac{x_{k+1} - x^*}{(x_k - x^*)^2} = \frac{f^{\prime\prime}(x^*)}{2 f^\prime(x^*)}
# \end{equation*}

# **证明**
# 将$Newton$迭代法改写成一般的不动点迭代法格式，有
# \begin{equation*}
#     \varphi(x) = x - \frac{f(x)}{f^\prime(x)},\quad \varphi^\prime(x) = \frac{f(x)f^{\prime\prime}(x)}{[f^\prime(x)]^2}
# \end{equation*}
# 很明显，由于$\varphi(x^*) = 0$，$\varphi^\prime(x^*) = 0$，$Newton$迭代法至少二阶收敛。此外
# \begin{equation*}
#     \lim_{k \to \infty} \frac{x_{k+1} - x^*}{(x_k - x^*)^2} = \lim_{k \to \infty} \frac{f^{\prime\prime}(\xi)}{2 f^\prime(\xi)} = \frac{f^{\prime\prime}(x^*)}{2 f^\prime(x^*)}
# \end{equation*}

# **!例**： 用$Newton$法求$f(x) = x^2 - C = 0$的正根。

# **!解**： 
# 
# $f(x)$的$Newton$迭代格式为
# \begin{equation*}
#     x_{k+1} = \frac{1}{2}\left( x_k + \frac{C}{x_k} \right)
# \end{equation*}
# 从而有
# \begin{equation*}
#     \frac{x_{k+1} - \sqrt{C}}{x_{k+1} + \sqrt{C}} = \left( \frac{x_{k} - \sqrt{C}}{x_{k} + \sqrt{C}} \right)^2 = \left( \frac{x_{0} - \sqrt{C}}{x_{0} + \sqrt{C}} \right)^{2^{k+1}} \triangleq q^{2^{k+1}}
# \end{equation*}
# \begin{equation*}
#     x_{k} - \sqrt{C} = 2 \sqrt{C} \frac{q^{2^k}}{1 - q^{2^k}} 
# \end{equation*}
# 
# 从而，对任意$x_0>0$，总有$|q|<1$，即牛顿法收敛。

# **!TIPS**： 牛顿迭代法的优点：至少二阶局部收敛，收敛速度较快，特别是当迭代点充分靠近精确解时。

# **!TIPS**： <font color="magenta">牛顿法是目前求解非线性方程 (组) 的主要方法</font>

# **!TIPS**： 牛顿迭代法的缺点：
# - 对重根收敛速度较慢（线性收敛）
# - 对初值的选取很敏感，要求初值相当接近真解
# - 每一次迭代都需要计算导数！

# **!TIPS**： <font color="magenta">实际使用过程中，一般先用其它算法获取一个近似解，然后使用牛顿法</font>

# ### Newton法的示例

# 

# ### Newton法的变种

# #### 简化的Newton法

# 其基本思想是：用$f^\prime(x_0)$替代所有的$f^\prime(x_k)$
# \begin{equation}
#     x_{k+1} = x_k - \frac{f(x_k)}{f^\prime(x_0)}
# \end{equation}
# 该迭代格式是线性收敛的：
# - 好处：只需要计算一次导数，即$f^\prime(x_0)$
# - 缺点：只有线性收敛速度（假定方法是收敛的）

# #### Newton下山法

# 其基本思想是：要求每一步迭代满足下降条件
# \begin{equation*}
#     |f(x_{k+1})| < |f(x_{k})|
# \end{equation*}
# 从而保证全局收敛性。
# 
# 具体的做法是：在迭代格式中增加下山因子$\lambda$
# \begin{equation*}
#     x_{k+1} = x_k - \lambda \frac{f(x_k)}{f^\prime(x_k)}
# \end{equation*}
# 
# 其中下山因子的取法为
# 
# 从$\lambda=1$开始，逐次减半，直到满足下降条件为止。

# ### Newton法的Python实现

# #### Python代码

# In[16]:


def newtonRaphson(f,Df,x0,epsilon,max_iter):
    '''Approximate solution of f(x)=0 by Newton's method.

    Parameters
    ----------
    f : function
        Function for which we are searching for a solution f(x)=0.
    Df : function
        Derivative of f(x).
    x0 : number
        Initial guess for a solution f(x)=0.
    epsilon : number
        Stopping criteria is abs(f(x)) < epsilon.
    max_iter : integer
        Maximum number of iterations of Newton's method.

    Returns
    -------
    xn : number
        Implement Newton's method: compute the linear approximation
        of f(x) at xn and find x intercept by the formula
            x = xn - f(xn)/Df(xn)
        Continue until abs(f(xn)) < epsilon and return xn.
        If Df(xn) == 0, return None. If the number of iterations
        exceeds max_iter, then return None.

    Examples
    --------
    >>> f = lambda x: x**2 - x - 1
    >>> Df = lambda x: 2*x - 1
    >>> newton(f,Df,1,1e-8,10)
    Found solution after 5 iterations.
    1.618033988749989
    '''
    xn = x0
    for n in range(0,max_iter):
        fxn = f(xn)
        if abs(fxn) < epsilon:
            print('Found solution after',n,'iterations.')
            return xn
        Dfxn = Df(xn)
        if Dfxn == 0:
            print('Zero derivative. No solution found.')
            return None
        xn = xn - fxn/Dfxn
    print('Exceeded maximum iterations. No solution found.')
    return None


# #### Python代码使用实例

# In[17]:


p = lambda x: x**3 - x**2 - 1
Dp = lambda x: 3*x**2 - 2*x
approx = newtonRaphson(p,Dp,1,1e-10,10)
print(approx)


# In[18]:


f = lambda x: x**(1/3)
Df = lambda x: (1/3)*x**(-2/3)
approx = newtonRaphson(f,Df,0.1,1e-2,100)


# #### Python代码使用训练题

# Let $p(x) = x^3 - x - 1$. The only real root of $p(x)$ is called the <font color="magenta">plastic number</font> and is given by
# \begin{equation}
#     \frac{\sqrt[3]{108+12\sqrt{69}} + \sqrt[3]{108-12\sqrt{69}}}{6}  
# \end{equation}
# 1. Choose $x_0 = 1$ and implement $2$ iterations of Newton's method to approximate the plastic number.
# 1. Use the exact value above to compute the absolute error after $2$ iterations of Newton's method.
# 1. Starting with the subinterval $[1,2]$, how many iterations of the bisection method is required to achieve the same accuracy?

# 

# ## 迭代法的收敛速度及其加速 （Convergence and Acceleration)

# ### 迭代法的收敛加速

# 对于线性收敛的迭代法，常常收敛速度很慢，所以一般要在基本不动点迭代法的基础上考虑加速收敛的方法。
# 
#  设$\{ x_k \}$线性收敛到$x^*$，则迭代误差$e_k = x_k - x^*$满足
#  \begin{equation*}
#      \lim_{k \to \infty} \frac{e_{k+1}}{e_k} = \lim_{k \to \infty} \frac{x_{k+1} - x^*}{x_k - x^*} = C \neq 0
#  \end{equation*}
#  因此，当$k$充分大的时候，有
#  \begin{equation*}
#      \frac{x_{k+1} - x^*}{x_k - x^*} \approx \frac{x_{k+2} - x^*}{x_{k+1} - x^*} \approx C,
#  \end{equation*}
#  从式中解出$x^*$可得
#  \begin{equation*}
#      x^* \approx x_{k} - \frac{(x_{k+1} - x_{k})^2}{x_{k+2} - 2 x_{k+1} + x_k}
#  \end{equation*}

# 由此，我们取新数列$\{ \hat{x}_k \}_{k=0}^\infty$定义如下：
#  \begin{equation*}
#      \hat{x}_k \equiv x_{k} - \frac{(x_{k+1} - x_{k})^2}{x_{k+2} - 2 x_{k+1} + x_k}.
#  \end{equation*}
#  可证明该数列$\{ \hat{x}_k \}_{k=0}^\infty$的收敛速度要比$\{ x_k \}_{k=0}^\infty$快，即 
#  \begin{equation*}
#      \lim_{k \to \infty} \frac{\hat{x}_k - x^*}{x_k - x^*} = 0
#  \end{equation*}
# 这种通过改变数列的定义方式来提高收敛速度的方法称为<font color="magenta">$Aitken$加速法</font>，在改进线性收敛数列的收敛速度上经常采用。[Pomeranz, S. B. (2017). Aitken's $\Delta^2$ method extended. Cogent Mathematics, 4(1), 1308622.]

#  将$Aitken$加速法与不动点迭代法结合起来，我们就能够获得<font color="magenta">$Steffensen$迭代法</font>：
#  \begin{equation*}
#      \left\{\begin{aligned}
#          y_k     &= \varphi(x_k) \\
#          z_k     &= \varphi(y_k) \\
#          x_{k+1} &= x_k - \frac{(y_k - x_k)^2}{z_k - 2 y_k + x_k}
#      \end{aligned}\right.
#  \end{equation*}
#  其对应的迭代函数$\psi(x)$为
#  \begin{equation*}
#      \boxed{x_{k+1} = \psi(x_k),\quad \psi(x) = x - \frac{(\varphi(x) - x)^2}{\varphi(\varphi(x)) - 2 \varphi(x) + x}}
#  \end{equation*}

# **!例**： 求方程$f(x) = x e^x - 1 = 0$的根。

# **解** 
# 若采用$Steffensen$迭代法，仍取初始值$x_0 = 0.5$，则
# \begin{equation*}
#     \begin{aligned}
#         y_k &= e^{-x_k},\ z_k = e^{-y_k},\\
#         x_{k+1} &= x_k - \frac{(y_k - x_k)^2}{z_k - 2 y_k + x_k}
#     \end{aligned}
# \end{equation*}
# 计算结果列于下表
# 
# | $k$ | $0$ | $1$ | $2$ | $3$ | $4$ |
# |-----|-----|-----|-----|-----|-----|
# | $x_k$ | $0.5$ |  $0.567623876$ | $0.567143314$ | $0.567143290$ | $0.567143290$ |
# 
# 比较而言，可以发现，$Steffensen$迭代法比原不动点迭代法收敛得快得多，仅迭代$4$次就达到了原方法$29$次的结果。

# **!定理**： 设函数$\varphi(x)$和$\psi(x)$按之前的定义，即
#  \begin{equation*}
#      \psi(x) = x - \frac{(\varphi(x) - x)^2}{\varphi(\varphi(x)) - 2 \varphi(x) + x}
#  \end{equation*}
#  则我们可以对$Steffensen$迭代法获得如下结论：
# 1. 若$x^*$是$\varphi(x)$的不动点，$\varphi(x)$在$x^*$处连续，且$\varphi^\prime(x^*) \neq 1$，则$x^*$也是$\psi(x)$的不动点；反之，若$x^*$是$\psi(x)$的不动点，则$x^*$也是$\varphi(x)$的不动点。
# 1. 若$x^*$是$\varphi(x)$的不动点，$\varphi^{\prime\prime}(x)$在$x^*$处连续，且$\varphi^\prime(x^*) \neq 1$，则$Steffensen$迭代法至少具有二阶局部收敛性。
# 

# **证明**
# （1）若$x^* = \varphi(x^*)$，则当$x= x^*$时，$\psi$时没有定义的，其分子分母都为零。采用$L'Hospitale$法则，由于$\varphi^\prime(x^*) \neq 1$，可以得到
# 
# \begin{equation*}
#     \begin{aligned}
#         \lim_{x\to x^*}\psi(x) &= \lim_{x\to x^*} \frac{\varphi(\varphi(x)) + x \varphi^\prime(\varphi(x)) \varphi^\prime(x) - 2 \varphi(x) \varphi^\prime(x)}{\varphi^\prime(\varphi(x))\varphi^\prime(x) - 2 \varphi^\prime(x) + 1} \\
#         &= \frac{x^* \left[ \varphi^\prime(x^*) - 1 \right]^2}{ \left[ \varphi^\prime(x^*) - 1 \right]^2 } = x^*
#     \end{aligned}
# \end{equation*}
# 
# 从而$x^* = \psi(x^*)$。反之，若$x^* = \psi(x^*)$，则根据$\psi(x)$的定义式得知$x^* = \varphi(x^*)$。
# 
# （2）由(1)可知，$x^*$是$\psi(x)$的不动点，因此，根据前述的局部收敛阶定理，只需要证明$\varphi^{\prime}(x) = 0$。为此，我们对$\psi(x)$的定义式进行求导，可得
# \begin{equation*}
#     1 - \psi^\prime(x) = \frac{p(x)}{q(x)},
# \end{equation*}
# 其中：
# \begin{equation*}
#     \begin{aligned}
#         p(x) &= 2 [\varphi(x) - x][\varphi^{\prime}(x) - 1][\varphi(\varphi(x)) - 2 \varphi(x) + x] \\
#              &- \left[ \varphi(x) - x \right]^2 \left[ \varphi^{\prime}(\varphi(x)) \varphi^{\prime}(x) - 2 \varphi^{\prime}(x) + 1 \right]\\
#         q(x) &= \left[ \varphi(\varphi(x)) - 2 \varphi(x) + x \right]^2
#     \end{aligned}
# \end{equation*}
# 
# 容易算出
# \begin{equation*}
#     p^{\prime\prime}(x^*) = q^{\prime\prime}(x^*) = 2 \left[ \varphi^{\prime}(x^*) - 1 \right]^4
# \end{equation*}
# 于是，由于$|\varphi^{\prime}(x^*)| \neq 1$，可知
# $$p^{\prime\prime}(x^*) = q^{\prime\prime}(x^*) \neq 0$$
# 从而再次使用$L'Hospitale$法则可知
# \begin{equation*}
#     1 - \psi^\prime(x^*) = \lim_{x \to x^*} [ 1 - \psi^\prime(x)] = \lim_{x \to x^*} \frac{p(x)}{q(x)} = \lim_{x \to x^*} \frac{p^{\prime\prime}(x)}{q^{\prime\prime}(x)} = 1
# \end{equation*}
# 从而$\psi^\prime(x^*) = 0$。定理得证。 

# **！TIPS**：若原迭代格式是$p$阶收敛的，则对应的$Steffensen$迭代是$p+1$阶收敛的。

# ### Python示例

# 

# ## 其他复杂方法 （Other Complex Methods）

# ### 割线法（Secant Method）
# 割线法与前述的迭代法（二分法，不动点迭代法，Newton迭代法）的主要不同是，每一步迭代的时候需要提供两个已知值。割线法的处理方式和理解方式主要有两种：
# - 作为二分法的变种
# - 作为Newton法的变种

# #### 割线法作为二分法的变种
# [作为二分法变种的割线法](https://personal.math.ubc.ca/~pwalls/math-python/roots-optimization/secant/)与二分法的基本条件一致：对于在区间$[a,b]$上的连续函数$f(x)$，要求$f(a)f(b)<0$，则根据中值定理，在区间$[a,b]$内某一点$x^*$处必然有$f(x^*)=0$。
# 
# 所不同的是，二分法利用对区间的不断对分来更新有根子区间并逐步逼近$x^*$，而割线法则利用连接$(a,f(a))$和$(b,f(b))$两点的割线与$x$轴的交点来不断更新有根子区间并逼近$x^*$。
# 
# - 首先，连接$(a,f(a))$和$(b,f(b))$两点的割线方程为
# \begin{equation}
#     y = \frac{f(b) - f(a)}{b-a}(x-a) + f(a)
# \end{equation}
# - 其次，考虑该割线与$x$轴的交点，在上式中令$y=0$，即
# \begin{equation}
#     0 = \frac{f(b) - f(a)}{b-a}(x-a) + f(a)
# \end{equation}
# 可得交点的横坐标为
# \begin{equation}
#     x = a - f(a)\frac{b-a}{f(b) - f(a)}
# \end{equation}

# 这种情况下，割线法的算法与二分法一致，唯一的区别在于确定有根子区间的方法。基本的<font color='red'>算法步骤</font>如下
# 1. 确定一个有根区间$[a_0,b_0]$，使得它满足$f(a_0) f(b_0) <0$;
# 1. 计算$f(x_0)$，其中$x_0$是割线与$x$轴的交点：
# \begin{equation}
#     x_0 = a_0 - f(a_0)\frac{b_0-a_0}{f(b_0) - f(a_0)}
# \end{equation}
# 1. 确定下一个有根区间$[a_1,b_1]$：
#     1. 如果$f(a_0) f(x_0) <0$，则取$a_1 = a_0$, $b_1 = x_0$，新的有根区间为$[a_1,b_1]$.
#     1. 如果$f(x_0) f(b_0) <0$，则取$a_1 = x_0$, $b_1 = b_0$，新的有根区间为$[a_1,b_1]$.
# 1. 重复第(2)和第(3)步直到获得最终的有根区间$[a_N,b_N]$达到预设目标.
# 1. 求得第$N$个有根区间中求得的割线与与$x$轴的交点$x_N$。

# 在这种情况下，割线法的代码如下：

# In[19]:


def secantIteration(func, a, b, maxiter=30, tol=1e-3):
    '''Approximate solution of f(x)=0 on interval [a,b] by the secant method.

    Parameters
    ----------
    func : function
        The function for which we are trying to approximate a solution f(x)=0.
    a,b : numbers
        The interval in which to search for a solution. The function returns
        None if f(a)*f(b) >= 0 since a solution is not guaranteed.
    tol : number
        The interval length or the absolute value of $f(x)$ which are thought 
        to be zero. Sometimes it is represented by two numbers tolfunc
        and tolroot.
    maxiter: (positive) integer
        The number of iterations to implement.

    Returns
    -------
    xN : number
        The x intercept of the secant line on the the Nth interval
            xn = an - f(an)*(bn - an)/(f(bn) - f(an))
        The initial interval [a0,b0] is given by [a,b]. If f(xn) == 0
        for some intercept xn then the function returns this solution.
        If all signs of values f(an), f(bn) and f(xn) are the same at any
        iterations, the secant method fails and return None.

    Examples
    --------
    >>> f = lambda x: x**2 - x - 1
    >>> secantIteration(f,1,2,5)
    1.6180257510729614
    '''
    if func(a)*func(b) >= 0:
        print("Secant method fails.")
        return None
    an, bn = a, b
    for n in range(1, maxiter+1):
        xn = an - func(an)*(bn - an)/(func(bn) - func(an))
        if func(an)*func(xn) < 0:
            an, bn = an, xn
        elif func(bn)*func(xn) < 0:
            an, bn = xn, bn
        elif func(xn) == 0:
            print("Found exact solution.")
            return xn
        else:
            print("Secant method fails.")
            return None
    return an - func(an)*(bn - an)/(func(bn) - func(an))


# In[20]:


f = lambda x: x**2 - x - 1
secantIteration(f, 1, 2)


# In[21]:


pp = lambda x: x**3 - x**2 - 1
supergolden = (1 + ((29 + 3*93**0.5)/2)**(1/3) + 
               ((29 - 3*93**0.5)/2)**(1/3))/3
approx = secantIteration(pp, 1, 2)
print(approx)
print(supergolden)
print(np.abs(supergolden - approx))


# #### 割线法作为Newton法的变种
# [作为Newton法变种的割线法](https://mmas.github.io/secant-julia)，可以看作是将$Newton$法
# \begin{equation}
#     x_{k+1} = x_k - \frac{f(x_k)}{f^\prime(x_k)}
# \end{equation}
# 中的导数项$f^\prime(x_k)$用经过函数$f(x)$图像上的点$(x_k,f(x_k))$和$(x_{k-1},f(x_{k-1}))$的割线的斜率
# \begin{equation}
#     \frac{f(x_{k-1}) - f(x_k)}{x_{k-1} - x_k}
# \end{equation}
# 来代替。由此，我们获得了如下迭代公式
# \begin{equation}
#     x_{k+1} = x_{k} - f(x_{k})\frac{x_{k} - x_{k-1}}{f(x_{k}) - f(x_{k-1})}
# \end{equation}.

# In[22]:


import numpy as np
def secant(func, x0, x1, atol = 1e-3, maxiter = 30):
    for i in range(0, maxiter):
        y1 = func(x1)
        y0 = func(x0)
        x  = x1 - y1 * (x1-x0)/(y1-y0)
        if np.abs(x-x1) < atol:
            return x
        x0 = x1
        x1 = x
    error("Max iteration exceeded")


# In[23]:


ff = lambda x: x**2 - 10
x0, x1 = 1., 2.
xsol1 =  secant(ff, x0, x1)
x0, x1 = 1., -2.
xsol2 = secant(ff, x0, x1)
xsol3 = np.sqrt(10)
print(f'xsol1 = {xsol1:2.10f}, with starting points x0 = 1.0, x1 = 2.0')
print(f'xsol2 = {xsol2:2.10f}, with starting points x0 = 1.0, x1 = -2.0')
print(f'xsol3 = {xsol3:2.10f}, accurate solution')


# In[24]:


pp = lambda x: x**3 - x**2 - 1
supergolden = (1 + ((29 + 3*93**0.5)/2)**(1/3) + 
               ((29 - 3*93**0.5)/2)**(1/3))/3
approx = secant(pp, 1, 2)
print(approx)
print(supergolden)
print(np.abs(supergolden - approx))


# #### 其他实现

# In[25]:


def secant_method(f, x0, x1, iterations):
    """Return the root calculated using the secant method."""
    for i in range(iterations):
        x2 = x1 - f(x1) * (x1 - x0) / float(f(x1) - f(x0))
        x0, x1 = x1, x2
    return x2

def f_example(x):
    return x ** 2 - 612

root = secant_method(f_example, 10, 30, 5)

print("Root: {}".format(root))  # Root: 24.738633748750722


# ### 反向二次插值法(Inverse Quadratic Interpolation Method)
# 反向二次插值法很少直接用来对非线性方程进行求根，一般作为Brent法的一部分。

# 反向二次插值法中，函数$f(x)$在三个点$x_0$，$x_1$和$x_2$处进行求值，其中$x_0$，$x_1$和$x_2$属于某个有根区间。对函数$f(x)$和$x$进行反向二次插值有
# \begin{equation}
#     g(y) = \frac{(y - f(x_1))(y - f(x_2))}{(f(x_0) - f(x_1))(f(x_0) - f(x_2))} x_0 + \frac{(y - f(x_0))(y - f(x_2))}{(f(x_1) - f(x_0))(f(x_1) - f(x_2))} x_1 + \frac{(y - f(x_0))(y - f(x_1))}{(f(x_2) - f(x_0))(f(x_2) - f(x_1))} x_2
# \end{equation}
# 此时，令$y=0$，我们可以得到
# \begin{equation}
#     g(y) = x = \frac{f(x_1) f(x_2)}{(f(x_0) - f(x_1))(f(x_0) - f(x_2))} x_0 + \frac{ f(x_0) f(x_2)}{(f(x_1) - f(x_0))(f(x_1) - f(x_2))} x_1 + \frac{f(x_0) f(x_1)}{(f(x_2) - f(x_0))(f(x_2) - f(x_1))} x_2
# \end{equation}
# 在每次迭代计算之后，$x_0$，$x_1$和$x_2$的更新规则如下：
# - $x_0$  $\Leftarrow$ $x_1$
# - $x_1$  $\Leftarrow$ $x_2$
# - $x_2$  $\Leftarrow$ $x$

# In[26]:


import numpy as np
def invquadinterp(f, x0, x1, x2, xtol = 1e-5, ytol = 1e-10, maxiter = 50):
    y0, y1, y2 = f(x0), f(x1), f(x2)
    for i in range(1, maxiter+1):
        x = x0*y1*y2/((y0-y1)*(y0-y2)) +             x1*y0*y2/((y1-y0)*(y1-y2)) +             x2*y0*y1/((y2-y0)*(y2-y1))
        # x-tolerance.
        if np.abs(x-x0) < xtol or np.abs(x-x1) < xtol or np.abs(x-x2) < xtol:
            return x
        y = f(x)
        # y-tolerance.
        if np.abs(y) < ytol:
            return x
        x0, x1, x2 = x1, x2, x
        y0, y1, y2 = y1, y2, y
    error("Max iteration exceeded")


# In[27]:


f = lambda x: x**4 - 2*x**2 + 1/4.; 
xapp = invquadinterp(f, 0, 0.5, 1)
xsol = np.sqrt(1-np.sqrt(3)/2)
print(f'xapp={xapp:2.10f}\nxsol={xsol:2.10f}')


# ### Brent法（Brent's Method）
# [Brent法](https://mmas.github.io/brent-julia)或者Wijngaarden-Brent-Dekker法是一种综合使用二分法，割线法和反向二次插值法的非线性方程求根方法。只要求解区间上存在根，该方法总是能够获得最终的精确根的。
# 
# 给定函数$f(x)$和有根区间$[x_0,x_1]$，可以获得两个新的点$x_2$和$x_3$。这一过程中如果$|f(x_0)|< |f(x_1)|$，则需要将$x_0$和$x_1$的值调换。
# 
# 然后在每次迭代中，如果函数$f(x)$在$x_0$，$x_1$和$x_2$处的函数值是不同（在指定的误差范围内），则使用反向二次插值法获得新的$x$值。反之，则使用割线法获得新的$x$。此后，如果下列条件中的某一个满足，我们重新利用二分法来求$x$的值：
# - 如果$x$不是介于$(3x_0+x_1)/4$和$x_1$之间；
# - 如果前一步迭代中使用了二分法，或本次迭代为首次迭代且$|x-x_1|\geq \frac{1}{2}|x_1 - x_2|$；
# - 如果前一步迭代中使用了二分法，或本次迭代为首次迭代且$|x_1-x_2|< |\delta|$，其中$\delta$为设定的误差因数；
# - 如果前一步迭代中未使用二分法，且$|x-x_1|\geq \frac{1}{2}|x_2 - x_3|$；
# - 如果前一步迭代中未使用二分法，且$|x_2 - x_3| < |\delta|$，其中$\delta$为设定的误差因数。
# 
# 上述过程中我们定义$\delta = 2 \epsilon x_1$，其中$\epsilon$是机械精度。
# 
# 最后，新的$x_3$等于现在的$x_2$，新的$x_2$等于现在的$x_1$。如果$f(x)f(x_0) <0$，则新的$x_1$取现在的$x$，否则新的$x_2$取现在的$x$。此时，如果对新的$x_0$和$x_1$而言，$|f(x_0)|< |f(x_1)|$，则二者的值交换。该算法一直执行到$f(x)$或者$|x_1 - x_0|$小于给定的误差因数 。

# In[28]:


import numpy as np
def brent(f, x0, x1, xtol=1e-7, ytol=2e-10,maxiter=50):
    EPS = np.finfo(float).eps
    y0, y1 = f(x0), f(x1)
    if np.abs(y0) < np.abs(y1):
        # Swap lower and upper bounds.
        x0, x1 = x1, x0
        y0, y1 = y1, y0
    x2 = x0
    y2 = y0
    x3 = x2
    bisection = True
    for k in range(1, maxiter+1):
        # x-tolerance.
        if np.abs(x1-x0) < xtol:
            return x1
        # Use inverse quadratic interpolation if f(x0)!=f(x1)!=f(x2)
        # and linear interpolation (secant method) otherwise.
        if np.abs(y0-y2) > ytol and np.abs(y1-y2) > ytol:
            x = x0*y1*y2/((y0-y1)*(y0-y2)) +                 x1*y0*y2/((y1-y0)*(y1-y2)) +                 x2*y0*y1/((y2-y0)*(y2-y1))
        else:
            x = x1 - y1 * (x1-x0)/(y1-y0)

        # Use bisection method if satisfies the conditions.
        delta = np.abs(2*EPS*np.abs(x1))
        min1 = np.abs(x-x1)
        min2 = np.abs(x1-x2)
        min3 = np.abs(x2-x3)
        if (x < (3*x0+x1)/4 and x > x1) or            (bisection and min1 >= min2/2) or            (not bisection and min1 >= min3/2) or            (bisection and min2 < delta) or            (not bisection and min3 < delta):
            x = (x0+x1)/2
            bisection = True
        else:
            bisection = False

        y = f(x)
        # y-tolerance.
        if np.abs(y) < ytol:
            return x
        x3 = x2
        x2 = x1
        if np.sign(y0) != np.sign(y):
            x1, y1 = x, y
        else:
            x0, y0 = x, y

        if np.abs(y0) < np.abs(y1):
            # Swap lower and upper bounds.
            x0, x1 = x1, x0
            y0, y1 = y1, y0

    error("Max iteration exceeded")


# In[29]:


f = lambda x: x**4 - 2*x**2 + 1/4.; x0=0; x1=1; 
print(brent(f,x0,x1))
np.sqrt(1-np.sqrt(3)/2)


# #### Preparing initial values and conditions
# We need an initial bracket to use Brent’s method. There are also multiple conditions that we must actively maintain. A summary of relevant variables will precede discussion of conditions.
# 
# k = the iteration number.
# 
# a_k = an endpoint of the bracket.
# 
# b_k = an endpoint of the bracket, and also the current iterate.
# 
# b_{k-1} = previous iterate, initially set to a_{0}.
# 
# \delta = a tolerance value that is relatively small
# 
# One condition is that the roots must be bracketed between a and b:
# 
# f(a_{k})*f(b_{k})<0
# 
# The intermediate value theorem guarantees that the root will be bracketed if f(x) is continuous within this interval.
# 
# We also want |f(b)|<|f(a)| to be true such that b is a better guess for the root than a. If necessary, switch values a and b. Then initialize a third point c such that b_{k-1} = a.

# #### The iterative process
# Now we have a, b, and b_{k-1} such that b_{k}\neq b_{k-1}. The following conditions need to be maintained and updated to prepare for subsequent iterations.
# 
# f(b_{k})*f(b_{k-1}) < 0 to reduce size of our bracket.
# |f(b_{k})| \leq |f(b_{k-1})| to make b our best approximate solution.
# a_k is either distinct from b_k and c_k, or a_k = b_{k-1} and is the immediate past value of b_k.
# At the end of each iteration, we have another condition that checks to see if we have an acceptable solution.
# 
# If |b_k-b_{k-1}| < \delta, return b_k.
# Else, find b_{k+1}.

# #### Finding b_{k+1}
# We have two different cases if we’re trying to find b_{k+1}. Steps 3 and 4 are rather complicated, and I won’t be covering the intermediate steps as I’m still trying to understand what happens there.
# 
# If a_k=b_{k-1}, then use secant interpolation to find b_{k+1}=\frac{a_k f(b_k) - b_k f(a_k)}{f(b_k)-f(a_k)}.
# Else use inverse quadratic interpolation to find b_{k+1}.
# Adjust or replace b_{k+1} with bisection method if necessary.
# Adjust a_k, b_{k-1}, b_k, and b_{k+1} for next iteration if needed.
# 

# #### Rate of convergence
# 
# In the worst case, Brent’s method will use no more than N^{2} iterations where N is the number of iterations had this method been purely bisection. Otherwise, this algorithm can converge superlinearly such that:
# 
# \lim_{k\rightarrow \infty} \frac{\left |x_{k+1}-L \right |}{\left |x_k - L\right |} = \mu 
# 
# and
# 
# \mu_{k}\rightarrow 0 as k\rightarrow \infty
# 
# where
# 
# \mu is the rate of convergence, and
# 
# L is the number that we’re converging to.

# ## 利用Python对函数进行求根

# TRY IT! Using fsolve function from scipy to compute the root of $𝑓(𝑥)=cos(𝑥)−𝑥$ near $−2$. Verify that the solution is a root (or close enough).

# In[30]:


import numpy as np
from scipy import optimize

f = lambda x: np.cos(x) - x
r = optimize.fsolve(f, -2)
print("r =", r)

# Verify the solution is a root
result = f(r)
print("result=", result)


# TRY IT! The function $𝑓(𝑥)=\frac{1}{x}$ has no root. Use the fsolve function to try to compute the root of $𝑓(𝑥)=\frac{1}{x}$. Turn on the "full_output" option to see what's going on. Remember to check the documentation for details.

# In[31]:


f = lambda x: 1/x

r, infodict, ier, mesg = optimize.fsolve(f, -2, full_output=True)
print("r =", r)

result = f(r)
print("result=", result)

print(mesg)


# We can see that, the value $r$ we got is not a root, even though the $f(r)$ is a very small number. Since we turned on the full_output, which have more information. A message will be returned if no solution is found, and we can see mesg details for the cause of failure: 
# 
# "The number of calls to function has reached maxfev = 400."

# In[32]:


"""
Brent's method
================

Illustration of 1D optimization: Brent's method
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

x = np.linspace(-1, 3, 100)
x_0 = np.exp(-1)

def f(x):
    return (x - x_0)**2 + epsilon*np.exp(-5*(x - .5 - x_0)**2)

for epsilon in (0, 1):
    plt.figure(figsize=(3, 2.5))
    plt.axes([0, 0, 1, 1])

    # A convex function
    plt.plot(x, f(x), linewidth=2)

    # Apply brent method. To have access to the iteration, do this in an
    # artificial way: allow the algorithm to iter only once
    all_x = list()
    all_y = list()
    for iter in range(30):
        result = optimize.minimize_scalar(f, bracket=(-5, 2.9, 4.5), method="Brent",
                    options={"maxiter": iter}, tol=np.finfo(1.).eps)
        if result.success:
            print('Converged at ', iter)
            break

        this_x = result.x
        all_x.append(this_x)
        all_y.append(f(this_x))
        if iter < 6:
            plt.text(this_x - .05*np.sign(this_x) - .05,
                    f(this_x) + 1.2*(.3 - iter % 2), iter + 1,
                    size=12)

    plt.plot(all_x[:10], all_y[:10], 'k+', markersize=12, markeredgewidth=2)

    plt.plot(all_x[-1], all_y[-1], 'rx', markersize=12)
    plt.axis('off')
    plt.ylim(ymin=-1, ymax=8)

    plt.figure(figsize=(4, 3))
    plt.semilogy(np.abs(all_y - all_y[-1]), linewidth=2)
    plt.ylabel('Error on f(x)')
    plt.xlabel('Iteration')
    plt.tight_layout()

plt.show()


# ## 小结

# 

# ## 习题和讨论

# 

# In[ ]:




