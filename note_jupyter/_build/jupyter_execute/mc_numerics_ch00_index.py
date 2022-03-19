#!/usr/bin/env python
# coding: utf-8

# # <center> 数值计算方法 - Python实现</center>
# <center>（Numerical Computational Methods based on Python Language）</center>

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#序言" data-toc-modified-id="序言-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>序言</a></span><ul class="toc-item"><li><span><a href="#课程目标" data-toc-modified-id="课程目标-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>课程目标</a></span></li><li><span><a href="#先修内容" data-toc-modified-id="先修内容-1.2"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>先修内容</a></span></li><li><span><a href="#内容组织" data-toc-modified-id="内容组织-1.3"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>内容组织</a></span></li><li><span><a href="#怎么阅读和学习本文档" data-toc-modified-id="怎么阅读和学习本文档-1.4"><span class="toc-item-num">1.4&nbsp;&nbsp;</span>怎么阅读和学习本文档</a></span></li><li><span><a href="#为什么选择Python作为本课程的语言？" data-toc-modified-id="为什么选择Python作为本课程的语言？-1.5"><span class="toc-item-num">1.5&nbsp;&nbsp;</span>为什么选择Python作为本课程的语言？</a></span></li><li><span><a href="#Python和其中package的版本" data-toc-modified-id="Python和其中package的版本-1.6"><span class="toc-item-num">1.6&nbsp;&nbsp;</span>Python和其中package的版本</a></span></li></ul></li><li><span><a href="#致谢" data-toc-modified-id="致谢-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>致谢</a></span></li></ul></div>

# ## 序言
# 本课程的文档都开源公布在一下网址：
# > [https://gitee.com/zhoumaoying/numerical_analysis/tree/master/note-py](https://gitee.com/zhoumaoying/numerical_analysis/tree/master/note-py)
# 
# 大家有两种方式对该课程的内容进行学习：
# - 直接在网页上选定对应章节的内容，在网页端打开。这种方式可能会使文档的格式有所变化，且无法执行文档中嵌入的代码。
# - 从网页上下载所有的.ipynb文件（注意要包含所有的文件夹的内容，本文中的图片都是利用相对路径方式添加）。这种方式能够自由修改文档（但请提前保存），而且能够实时执行文档中嵌入的代码，前提是正确在电脑上配置了python开发环境。

# ### 课程目标

# 本文档主要配合针对本科生开设的《数值计算方法》课程。本文档的主要内容参考了开源文档[Python Programming and Numerical Methods - A Guide for Engineers and Scientists](https://pythonnumericalmethods.berkeley.edu/notebooks/Index.html) （参见[Berkeley Python Numerical Methods](https://pythonnumericalmethods.berkeley.edu/notebooks/Index.html) )目前阶段，本文档主要是该开源文档的中文翻译和简化，以适应本课程的学习。在未来的时间里，本文档的最终目标是能够完全自主化。

# 本教程主要讲解利用python编程语言进行数值计算方法课程的教学，其目的有三：
# + 一是简单介绍python编程语言及其在工程实践和科学研究中的应用；
# + 二是结合python语言的特性更好地展现数值计算方法的内容；
# + 三是通过将程序编写、运行和结果可视化融入到数值计算方法的讲解中，更好地讲解计算机在数值计算中的应用。
# 
# 从心理上讲，本课程还有一个比较远大似乎不切实际的目标，就是希望能够带着同学们适应计算机化的工业时代，也就是熟悉利用计算机表达真实世界的各种方法，掌握运用计算机处理真实世界问题的各种途径，适应在工程中运用计算机工具从事各种工作。

# ### 先修内容

# 本文档的写作初衷是向无任何背景知识的同学介绍基于编程的数值计算方法。尽管如此，我们还是希望同学们在学习本课程的时候能够具备一些基本知识，包括
# + 基础的计算机编程操作，如命令行工具（command line tool），bash操作等
# + 基本的windows操作系统知识，如环境变量，文档结构等
# + 基本的线性代数
# + 微积分基础知识
# 
# 在未来的文档更新中，我们可能会更新一些基础知识的小短文。
# 

# ### 内容组织

# 本文档总的来说分为两个部分：第一部分以python语言为例介绍了基本的编程概念；第二部分以python为载体介绍工程常用的数值计算方法。

# 第一部分包括第01章到第13章，分别包含以下内容
# + 第01章：介绍Python语言和Jupyter Notebook，以便于后期文档的阅读，操作，以及日常作业的提交等
# + 第02章：Python中的变量和基本数据结构 （Variables and Data Structures）
# + 第03章：Python中函数的定义与使用（Function Definitions and Calls）
# + 第04章：Python中的逻辑操作与程序分支（Logic Operations and Program Branching）
# + 第05章：Python中的迭代（Iteration）
# + 第06章：Python中的递归（Recursion）
# + 第07章：Python中的面向对象编程（Object Oriented Programming， OOP）
# + 第08章：程序和算法的复杂度（Time and Space Complexity）
# + 第09章：数的计算机表示（Representation of Numbers）
# + 第10章：程序错误，编程规范与程序调试（Errors, Good Programming Practices, and Debugging）
# + 第11章：数据读写操作（I/O and Documents）
# + 第12章：可视化与数据做图（Visualization and Plotting）
# + 第13章：Python中程序的并行化（Parallelization）

# 第二部分包括第14章到第25章，分别包含以下内容
# + 第14章：线性代数与线性方程组（Systems of Linear Equations）
# + 第15章：特征值与特征向量（Eigenvalues and Eigenvectors）
# + 第16章：逼近与插值（Approximations and Interpolation）
# + 第17章：逼近与最小二乘拟合（Approximations and Least-Square Fitting）
# + 第18章：级数（Series）
# + 第19章：非线性方程求解（Roots of Nonlinear Functions）
# + 第20章：数值微分(Numerical Differentiation)
# + 第21章：数值积分(Numerical Integration)
# + 第22章：常微分方程-初始值问题(Ordinary Differential Equations - Initial Value Problems)
# + 第23章：常微分方程-边界值问题(Ordinary Differential Equations - Boundary Value Problems
# + 第24章：傅立叶变换和谱方法（Fourier Transform and Spectral Method）
# + 第25章：机器学习简介（An Introduction to Machine Learning）
# 

# 注意到：理想而言，数值计算方法应该需要构成一个利用计算机语言解决工程问题的课程群：
# + 数学建模 (Mathematical Modeling in Engineering Applications)
# + 算法设计与分析 (Algorithm Design and Analysis)
# + 计算机编程 （Programming）
# + 数值计算与分析（有限精度计算，Finite Precision Computation）
# + 高性能计算 （High Perormance Computation: Parallelization; Large-Scale Computation）
# + 可视化（Visualization; Discretization; Computer Graphics）
# 
# 但是构建这么一个庞大的课程群并非易事，只能留到后面徐图之。

# ### 怎么阅读和学习本文档

# 这里其实分为两个部分：关于编程的部分和关于数值计算的部分。

# 针对编程部分，最好的方法就是不断练习和熟悉。
# 1. 在浏览本文档的过程中，希望你能够借助Jupyter notebook 不断地联系文档中给出的各个示例。记住，读10遍文档不如按照文档敲代码1遍
# 2. 文档的内容还是需要配合教师的课堂讲解进行理解。希望大家能够相互比较借鉴，从而能够提高学习效率。

# 针对数值计算方法部分，最好的办法是不断应用
# 1. 数值计算方法都需要针对特定的数学问题进行设计，这个一定要牢记
# 2. 本质上来说，数值计算方法的内容可以分为一下几个部分：数值线性代数、数值求根、数值近似、数值微分方程
# 3. 任何理论学习一定要结合具体问题进行分析。数值计算方法的发展是应工程问题解决过程中所需要了解的问题而产生的。所以我们一定要知道不同的方法的来龙去脉
# 4. 有机会的话，希望能够在日常的学习和工作过程中对数值计算方法进行应用

# ### 为什么选择Python作为本课程的语言？

# 实际上，从最早的编程语言以来，大量的语言都可以用进行数值计算，简单列举如下：
# + Fortran
# + C/C++
# + Matlab
# + Python
# + Julia
# + Mathematica
# + Maple
# 
# 这些语言各有特点。本课程采用python的主要理由是Jupyter Notebook的优良特性，以及在现代化过程中丰富的packages。

# 从学习和应用的角度，不同语言之间的区别没那么大，主要是语法和编程方式的区别。因此希望大家以某一种语言作为主要载体，对其他语言大略了解其基本特征即可。

# ### Python和其中package的版本

# Python 版本：Python 3.9.10 (main, Jan 15 2022, 11:48:04)

# Python中所使用的主要package的版本：（pip3 list）
# 
# + jupyter - 4.9.2
# + ipython - 8.1.0
# + numpy - 1.16.4
# + scipy - 1.8.0
# + matplotlib - 3.5.1
# + pandas - 1.3.5

# ## 致谢

# 本文档在编制过程中，得到了选修我主讲的《数值计算方法课程》的各班学生帮助，在此一并感谢并列举如下：
# 

# In[ ]:




